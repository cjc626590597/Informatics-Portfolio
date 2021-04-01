from datetime import datetime

from sqlalchemy import Sequence, PrimaryKeyConstraint
from werkzeug.security import generate_password_hash, check_password_hash
from init import db


class Phone(db.Model):
    Phone_id= db.Column(db.Integer, primary_key=True, autoincrement=True)
    Phone_name = db.Column(db.String(200))
    Phone_price = db.Column(db.String(200))
    Phone_factory_system_kernel = db.Column(db.String(200))
    Phone_screen_size=db.Column(db.String(200))
    Phone_OS = db.Column(db.String(200))
    Phone_resolution = db.Column(db.String(200))
    Phone_frequency=db.Column(db.String(200))
    Phone_kernel_num = db.Column(db.String(200))
    Phone_RAM_capacity = db.Column(db.String(200))
    Phone_ROM_capacity = db.Column(db.String(200))
    Phone_battery_capacity = db.Column(db.String(200))
    Phone_rear_camera = db.Column(db.String(200))
    Phone_front_camera = db.Column(db.String(200))
    Phone_pic_URL = db.Column(db.String(400))


db.create_all()