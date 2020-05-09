import datetime

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship

db = SQLAlchemy()


class SensorData(db.Model):
    __tablename__ = 'sensor_data'
    id = db.Column(db.Integer, primary_key=True)
    plant_id = db.Column(db.Integer, db.ForeignKey('plant.id'))
    temp = db.Column(db.Float)
    humidity = db.Column(db.Float)
    moisture = db.Column(db.Float)
    light_intensity = db.Column(db.Float)
    img_url = db.Column(db.String)
    time_recorded = db.Column(
        db.DateTime(timezone=True),
        default=datetime.datetime.utcnow
    )
    plant = db.relationship('Plant')

    def __init__(
        self, plant_id, temp, humidity, moisture,
        light_intensity, img_url):
        #
        self.plant_id = plant_id
        self.temp = temp
        self.humidity = humidity
        self.moisture = moisture
        self.light_intensity = light_intensity
        self.img_url = img_url

    def __repr__(self):
        return (
            f"<SensorData(plant_id={self.plant_id}, "
            f"temp={self.temp}, "
            f"humidity={self.humidity}, "
            f"moisture={self.moisture}, "
            f"light_intensity={self.light_intensity}, "
            f"img_url='{self.img_url}', "
            f"time_recorded={self.time_recorded})>"
        )


class PlantType(db.Model):
    __tablename__ = 'plant_type'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    water_requirement = db.Column(db.Integer)

    def __init__(self, name, water_requirement):
        self.name = name
        self.water_requirement = water_requirement

    def __repr__(self):
        return (
            f"<PlantType(name='{self.name}', "
            f"water_requirement={self.water_requirement})>"
        )


class Plant(db.Model):
    __tablename__ = 'plant'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    type_id = db.Column(db.Integer, db.ForeignKey('plant_type.id'))
    date_added = db.Column(db.DateTime, default=datetime.datetime.utcnow) 
    plant_type = db.relationship('PlantType')

    def __init__(self, name, type_id):
        self.name = name
        self.type_id = type_id

    def __repr__(self):
        return (
            f"<Plant(name='{self.name}', "
            f"type_id={self.type_id}, "
            f"date_added={self.date_added})>"
        )
