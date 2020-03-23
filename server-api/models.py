from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date, Float,ForeignKey

Base = declarative_base()

class SensorData(Base):
    __tablename__ = 'sensor_data'
    id = Column(Integer, primary_key=True)
    plant_id = Column(Integer, ForeignKey('plant.id'))
    temp = Column(Float)
    humidity = Column(Float)
    moisture = Column(Float)
    light_intensity = Column(Float)
    img_url = Column(String)
    time_recorded = Column(Date)    
    
    def __repr__(self):
        return "<SensorData(plant_id='{}', temp='{}', humidity='{}', moisture='{}', light_intensity={},img_url='{}', time_recorded='{}')>"\
                .format(self.plant_id, self.temp, self.humidity, self.moisture, self.light_intensity, self.img_url, self.time_recorded)

class PlantType(Base):
    __tablename__ = 'plant_type'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    water_requirement = Column(Integer)
   
    
    def __repr__(self):
        return "<PlantType(name='{}', water_requirement='{}')>"\
                .format(self.name, self.water_requirement)

class Plant(Base):
    __tablename__ = 'plant'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    type_id = Column(Integer, ForeignKey('plant_type.id'))
    date_added = Column(Date) 
   
    
    def __repr__(self):
        return "<Plant(name='{}', type_id='{}', date_added='{}')>"\
                .format(self.name, self.type_id, self.date_added)
