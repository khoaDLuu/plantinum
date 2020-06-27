import os

from flask import Flask, request, jsonify, g, url_for, abort
from flask_httpauth import HTTPBasicAuth
from models import db, PlantType, Plant, PlantData, User

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
auth = HTTPBasicAuth()


@app.before_first_request
def init_admin_account():
    admin = (
        db.session
        .query(User)
        .filter_by(username=app.config['ADMIN_USERNAME'])
        .first()
    )
    if admin is None:
        admin = User(username=app.config['ADMIN_USERNAME'], role='admin')
        admin.hash_password(app.config['ADMIN_PASSWORD'])
        db.session.add(admin)
        db.session.commit()


@auth.get_user_roles
def get_roles(auth):
    # TODO reduce the number of db queries
    user = db.session.query(User).filter_by(username=auth.username).first()
    return user.role


@auth.verify_password
def verify_password(username_or_token, password):
    user = User.verify_auth_token(username_or_token)
    if not user:
        user = (
            db.session.query(User)
            .filter_by(username=username_or_token)
            .first()
        )
        if not user or not user.verify_password(password):
            return False
    g.user = user
    return True


@app.route('/')
def hello():
    return {'app': 'plantinum api'}


@app.route('/users', methods=['POST'])
@auth.login_required(role='admin')
def add_user():
    # TODO implement JSON validation with decorators
    # TODO implement logging with decorators

    username = request.json.get('username')
    password = request.json.get('password')
    role = request.json.get('role')

    data_missing = None in (username, password, role)
    if data_missing:
        abort(400)
    
    role_invalid = role not in User.types.values()
    if role_invalid:
        abort(400)
    
    user_existing = (
        db.session
        .query(User)
        .filter_by(username=username)
        .first()
    ) is not None
    if user_existing:
        abort(400)
    
    user = User(username=username, role=role)
    user.hash_password(password)
    db.session.add(user)
    db.session.commit()

    return (
        jsonify({'username': user.username}),
        201,
        {'Location': url_for(
            'retrieve_user',
            username=user.username,
            _external=True
        )}
    )


@app.route('/users/<username>', methods=['GET'])
@auth.login_required(role='admin')
def retrieve_user(username):
    user = db.session.query(User).filter_by(username=username).first()
    if not user:
        abort(400)
    return jsonify({
        'id': user.id,
        'username': user.username,
        'role': user.role
    })


@app.route('/users', methods=['GET'])
@auth.login_required(role='admin')
def retrieve_user_list():
    offset = request.args.get('offset', 0)
    limit = request.args.get('limit', 5)
    role = request.args.get('role', '')
    
    role_codes = (next(
        (tcode for tcode, tname in User.types.items() if tname == role), None
    ),)
    if None in role_codes:
        role_codes = tuple(User.types.keys())

    user_list = (
        db.session.query(User)
        .filter(User.usertype.in_(role_codes))
        .order_by(User.id.asc())
        .offset(offset)
        .limit(limit)
        .all()
    )
    users = [{'id': user.id, 'username': user.username, 'role': user.role}
             for user in user_list]
    return jsonify(users)


@app.route('/token', methods=['GET'])
@auth.login_required
def make_auth_token():
    token = g.user.generate_auth_token(720)
    return jsonify({'token': token.decode('ascii'), 'duration': 720})


@app.route('/plants/<int:plant_id>', methods=['GET'])
@auth.login_required
def fetch_plant(plant_id):
    plant = (
        db.session.query(Plant)
        .filter_by(id=plant_id)
        .first()
    )
    return jsonify({
        "id": plant.id,
        "name": plant.name,
        "date_added": plant.date_added
    })


@app.route('/plants', methods=['GET'])
@auth.login_required
def fetch_plant_list():
    type_name = request.args.get('type', 'all')
    
    # FIXME bug in .filter(PlantType.name in type_names)
    if type_name == 'all':
        # type_names = 'flower', 'succulent', 'foliageplant', 'palmplant'
        results = (
            db.session.query(Plant, PlantType)
            .filter(Plant.type_id == PlantType.id)
            # .filter(PlantType.name in type_names)
            .order_by(Plant.id.desc())
            .all()
        )
    else:
        # type_names = (type_name,)
        results = (
            db.session.query(Plant, PlantType)
            .filter(Plant.type_id == PlantType.id)
            .filter(PlantType.name == type_name)
            .order_by(Plant.id.desc())
            .all()
        )

    plant_list = [
        {
            'id': plant.id,
            'name': plant.name,
            'type': plant_type.name,
            'date_added': plant.date_added
        }
        for plant, plant_type in results
    ]

    return jsonify(plant_list)


@app.route('/plants', methods=['POST'])
@auth.login_required(role=['admin', 'machine'])
def add_new_plant():
    if request.is_json:
        plant_info = request.get_json()

        # NOTE HARDCODED DATA
        type_codes = {
            'flower': 1,
            'succulent': 2,
            'foliageplant': 3,
            'palmplant': 4
        }
        type_id = type_codes[plant_info['type']]

        new_plant = Plant(
            name= plant_info['name'],
            type_id=type_id,
        )
        db.session.add(new_plant)
        db.session.commit()
        return (
            jsonify({'plant_id': new_plant.id}),
            201,
            {'Location': url_for(
                'fetch_plant',
                plant_id=new_plant.id,
                _external=True
            )}
        )
    else:
        return {
            "error": ("The request payload is not in JSON format"
                      " or the data is not complete")
        }


@app.route('/plants/<int:plant_id>/sensor_data', methods=['GET'])
@auth.login_required
def fetch_data_list(plant_id):
    # TODO Implement query param to fetch a number of data rows

    data_plant = (
        db.session.query(PlantData)
        .filter_by(plant_id=plant_id)
        .order_by(PlantData.id.desc())
        .all()
    )

    data_list = []
    for data in data_plant:
        data_list.append({
            'temperature': f'{data.temp}',
            'humidity': f'{data.humidity}',
            'moisture': f'{data.moisture}',
            'light_intensity': f'{data.light_intensity}',
            'img_url' : f'{data.img_url}'
        })

    return jsonify(data_list)


@app.route('/plants/<int:plant_id>/sensor_data', methods=['POST'])
@auth.login_required(role=['admin', 'machine'])
def receive_sensor_data(plant_id):
    if request.is_json:
        data = request.get_json()
        ss_data = SensorData(
            plant_id=plant_id,
            temp=data['temperature'],
            humidity=data['humidity'],
            moisture=data['moisture'],
            light_intensity=data['light_intensity'],
            img_url=data['img_url']
        )
        db.session.add(ss_data)
        db.session.commit()

        return {
            "message": (f"Sensor data of plant with id {ss_data.plant_id}"
                        "has been inserted successfully")
        }
    else:
        return (
            {"error": ("The request payload is not in JSON format"
                      " or the data is incomplete")},
            400
        )


@app.route('/plants/<int:plant_id>/sensor_data/latest', methods=['GET'])
@auth.login_required
def retrieve_latest(plant_id):
    # TODO write error handling

    latest_ss_data = (
        db.session.query(PlantData)
        .filter_by(plant_id=plant_id)
        .order_by(PlantData.id.desc())
        .first()
    )

    return jsonify({
        "temperature": latest_ss_data.temp,
        "humidity": latest_ss_data.humidity,
        "moisture": latest_ss_data.moisture,
        "light_intensity": latest_ss_data.light_intensity,
        "img_url": latest_ss_data.img_url
    })


@app.route('/plants_with_data', methods=['GET'])
@auth.login_required
def fetch_plants_with_data():
    results = (
        db.session.query(Plant, PlantType)
        .filter(Plant.type_id == PlantType.id)
        # .filter(PlantType.name in type_names)
        .order_by(Plant.id.desc())
        .all()
    )

    plant_list = [
        {
            'id': plant.id,
            'name': plant.name,
            'type': plant_type.name,
            'date_added': plant.date_added
        }
        for plant, plant_type in results
    ]

    plants_with_data = []
    for plant in plant_list:  #! TODO fix querying in loop
        latest_ss_data = (
            db.session.query(PlantData)
            .filter_by(plant_id=plant['id'])
            .order_by(PlantData.id.desc())
            .first()
        )
        plants_with_data.append({
            'id': plant['id'],
            'name': plant['name'],
            'type': plant['type'],
            'date_added': plant['date_added'],
            "temperature": latest_ss_data.temp,
            "humidity": latest_ss_data.humidity,
            "moisture": latest_ss_data.moisture,
            "light_intensity": latest_ss_data.light_intensity,
            "img_url": latest_ss_data.img_url
        })

    return jsonify(plants_with_data)


if __name__ == '__main__':
    app.run(debug=True)
