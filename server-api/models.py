import os

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from passlib.apps import custom_app_context as pwd_context
from itsdangerous import (
    TimedJSONWebSignatureSerializer as Serializer,
    BadSignature, SignatureExpired
)

SECRET_KEY = os.environ['APP_SECRET_KEY']
db = SQLAlchemy()


class PlantData(db.Model):
    __tablename__ = 'sensor_data'
    id = db.Column(db.Integer, primary_key=True)
    plant_id = db.Column(db.Integer, db.ForeignKey('plant.id'))
    temp = db.Column(db.Float)
    humidity = db.Column(db.Float)
    moisture = db.Column(db.Float)
    light_intensity = db.Column(db.Float)
    img_url = db.Column(db.String)
    state = db.Column(db.String, nullable=True)  # TODO change data type
    time_recorded = db.Column(
        db.DateTime(timezone=True),
        server_default=func.now())
    # Preferrably store time related data in UTC,
    # and do timezone conversions when presenting data
    plant = db.relationship('Plant')

    def __init__(
        self, plant_id, temp, humidity, moisture,
        light_intensity, img_url, state):
        #
        self.plant_id = plant_id
        self.temp = temp
        self.humidity = humidity
        self.moisture = moisture
        self.light_intensity = light_intensity
        self.img_url = img_url
        self.state = state

    def __repr__(self):
        return (
            f"<PlantData(plant_id={self.plant_id}, "
            f"temp={self.temp}, "
            f"humidity={self.humidity}, "
            f"moisture={self.moisture}, "
            f"light_intensity={self.light_intensity}, "
            f"img_url='{self.img_url}', "
            f"state='{self.state}', "
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
    date_added = db.Column(
        db.DateTime(timezone=True),
        server_default=func.now()
    )
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


class User(db.Model):
    types = {
        0: 'admin',
        1: 'regular',
        2: 'machine',
    }
    __tablename__ = 'api_user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), index=True)
    password_hash = db.Column(db.String(128))
    usertype = db.Column(db.Integer)
    time_created = db.Column(
        db.DateTime(timezone=True),
        server_default=func.now()
    )

    def __init__(self, username, role):
        self.username = username
        self.role = role

    @property
    def role(self):
        return User.types[self.usertype]

    @role.setter
    def role(self, value):
        self.usertype = [key for (key, val) in User.types.items()
                         if val == value][0]

    def hash_password(self, password):
        self.password_hash = pwd_context.encrypt(password)

    def verify_password(self, password):
        return pwd_context.verify(password, self.password_hash)

    def generate_auth_token(self, expiration=600):
        s = Serializer(SECRET_KEY, expires_in=expiration)
        return s.dumps({'username': self.username})

    @staticmethod
    def verify_auth_token(token):
        s = Serializer(SECRET_KEY)
        try:
            data = s.loads(token)
        except SignatureExpired:
            return None
        except BadSignature:
            return None
        user = (
            db.session
            .query(User)
            .filter_by(username=data['username'])
            .first()
        )
        return user

    def __repr__(self):
        return (
            f"<User(username={self.username}, "
            f"usertype={self.role}>"
        )
