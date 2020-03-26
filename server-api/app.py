import os

from flask import Flask, request, jsonify
from flask_migrate import Migrate
from models import db, Plant, SensorData

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
# migrate = Migrate(app, db)

@app.route('/')
def hello():
    return {'app': 'plantinum api'}


@app.route('/plants/<int:plant_id>', methods=['GET'])
def fetch_plant(plant_id):
    # TODO
    pass


@app.route('/plants', methods=['GET'])
def fetch_plant_list(plant_id):
    # TODO
    pass


@app.route('/plants', methods=['POST'])
def add_new_plant(plant_id):
    # TODO
    pass

@app.route('/plants/<int:plant_id>/sensor_data', methods=['GET'])
def fetch_data_list(plant_id):
    # TODO
    # fetch a specific number of sensor data rows in db
    # parse params to get the number
    pass


@app.route('/plants/<int:plant_id>/sensor_data', methods=['POST'])
def receive_sensor_data(plant_id):
    if request.is_json:
        data = request.get_json()
        ss_data = SensorData(
            plant_id=plant_id,
            temp=data['temp'],
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
        return {"error": "The request payload is not in JSON format"}


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
        "lightIntensity": latest_ss_data.light_intensity,
        "imgurl": latest_ss_data.img_url
    })


if __name__ == '__main__':
    app.run(debug=True)
