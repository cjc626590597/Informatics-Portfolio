from datetime import datetime

from sqlalchemy import Sequence, PrimaryKeyConstraint
from werkzeug.security import generate_password_hash, check_password_hash
from init import db


class testData(db.Model):
    Phone_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Phone_name = db.Column(db.String(200))
    Phone_price = db.Column(db.FLOAT)
    Phone_factory_system_kernel = db.Column(db.String(200))
    Phone_screen_size = db.Column(db.FLOAT)
    Phone_OS = db.Column(db.String(200))
    Phone_resolution = db.Column(db.String(200))
    Phone_frequency = db.Column(db.FLOAT)
    Phone_kernel_num = db.Column(db.FLOAT)
    Phone_RAM_capacity = db.Column(db.FLOAT)
    Phone_ROM_capacity = db.Column(db.FLOAT)
    Phone_battery_capacity = db.Column(db.FLOAT)
    Phone_rear_camera = db.Column(db.FLOAT)
    Phone_front_camera = db.Column(db.FLOAT)
    Phone_pic_URL = db.Column(db.String(400))
    Phone_brand = db.Column(db.String(400))
    Phone_target_group = db.Column(db.String(400))

class traingData(db.Model):
    Phone_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Phone_name = db.Column(db.String(200))
    Phone_price = db.Column(db.FLOAT)
    Phone_factory_system_kernel = db.Column(db.String(200))
    Phone_screen_size = db.Column(db.FLOAT)
    Phone_OS = db.Column(db.String(200))
    Phone_resolution = db.Column(db.String(200))
    Phone_frequency = db.Column(db.FLOAT)
    Phone_kernel_num = db.Column(db.FLOAT)
    Phone_RAM_capacity = db.Column(db.FLOAT)
    Phone_ROM_capacity = db.Column(db.FLOAT)
    Phone_battery_capacity = db.Column(db.FLOAT)
    Phone_rear_camera = db.Column(db.FLOAT)
    Phone_front_camera = db.Column(db.FLOAT)
    Phone_pic_URL = db.Column(db.String(400))
    Phone_brand = db.Column(db.String(400))
    Phone_target_group = db.Column(db.String(400))


class allData(db.Model):
    Phone_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Phone_name = db.Column(db.String(200))
    Phone_price = db.Column(db.FLOAT)
    Phone_factory_system_kernel = db.Column(db.String(200))
    Phone_screen_size = db.Column(db.FLOAT)
    Phone_OS = db.Column(db.String(200))
    Phone_resolution = db.Column(db.String(200))
    Phone_frequency = db.Column(db.FLOAT)
    Phone_kernel_num = db.Column(db.FLOAT)
    Phone_RAM_capacity = db.Column(db.FLOAT)
    Phone_ROM_capacity = db.Column(db.FLOAT)
    Phone_battery_capacity = db.Column(db.FLOAT)
    Phone_rear_camera = db.Column(db.FLOAT)
    Phone_front_camera = db.Column(db.FLOAT)
    Phone_pic_URL = db.Column(db.String(400))
    Phone_brand = db.Column(db.String(400))
    Phone_target_group = db.Column(db.String(400))


db.create_all()
