import os

from flask import Flask, request, jsonify
from flask_migrate import Migrate
from models import db, Plant, SensorData

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


@app.route('/')
def hello():
    return {'app': 'plantinum api'}


@app.route('/plants/<int:type_id>/plant', methods=['GET'])
def fetch_plant(type_id):
    latest_ss_plant = (
        db.session.query(Plant)
        .filter_by(type_id=type_id)
        .order_by(Plant.id.desc())
        .first()
    )
    return jsonify({
        "name": latest_ss_plant.name,
        "date_added": latest_ss_plant.date_added
    })


@app.route('/plants/<int:type_id>/plantlist', methods=['GET'])
def fetch_plant_list(type_id):
    plants = (
        db.session.query(Plant)
        .filter_by(type_id=type_id)
        .order_by(Plant.id.desc())
        .all()
    )

    plant_list = []
    for plant in plants:
        plant_list.append({
            'date_added': f'{plant.date_added}',
            'name' : f'{plant.name}'
        })

    return jsonify(plant_list)


@app.route('/plants/<int:type_id>/plant', methods=['POST'])
def add_new_plant(type_id):
    if request.is_json:
        plant_data = request.get_json()
       
        ss_data = Plant(
            name= plant_data['name'],
            type_id=type_id,
        )
        db.session.add(ss_data)
        db.session.commit()
        return {
            "message": (f"plant with id {ss_data.type_id}"
                        " has been inserted successfully")}
    else :
        return {
            "error": ("The request payload is not in JSON format"
                      " or the data is not complete")
        }


@app.route('/plants/<int:plant_id>/sensor_data', methods=['GET'])
def fetch_data_list(plant_id):
    data_plant = (
        db.session.query(SensorData)
        .filter_by(plant_id=plant_id)
        .order_by(SensorData.id.desc())
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
        return {
            "error": ("The request payload is not in JSON format"
                      " or the data is not complete")
        }


@app.route('/plants/<int:plant_id>/sensor_data/last', methods=['GET'])
def retrieve_latest(plant_id):
    latest_ss_data = (
        db.session.query(SensorData)
        .filter_by(plant_id=plant_id)
        .order_by(SensorData.id.desc())
        .first()
    )
    return jsonify({
        "temperature": latest_ss_data.temp,
        "humidity": latest_ss_data.humidity,
        "moisture": latest_ss_data.moisture,
        "light_intensity": latest_ss_data.light_intensity,
        "img_url": latest_ss_data.img_url
    })


if __name__ == '__main__':
    app.run(debug=True)
