from website import db

<<<<<<< Updated upstream
class phone(db.Model):
    phone_id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
=======
class all_data(db.Model):
    _tablename_ = 'all_data'
    Phone_id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    Phone_name = db.Column(db.String(100), nullable = False)
    Phone_price = db.Column(db.Integer, nullable = False)
    Phone_factory_system_kernel = db.Column(db.String(20), nullable = False)
    Phone_screen_size = db.Column(db.Float, nullable = False)
    Phone_screen_size = db.Column(db.String(20), nullable = False)
    Phone_resolution = db.Column(db.String(5), nullable = False)
    Phone_frequency = db.Column(db.Float, nullable = False)
    Phone_kernel_num = db.Column(db.Integer, nullable = False)
    Phone_RAM_capacity = db.Column(db.Integer, nullable = False)
    Phone_ROM_capacity = db.Column(db.Integer, nullable = False)
    Phone_battery_capacity = db.Column(db.Integer, nullable = False)
    Phone_rear_camera = db.Column(db.Integer, nullable = False)
    Phone_front_camera = db.Column(db.Integer, nullable = False)
    Phone_pic_URL = db.Column(db.String(100), nullable = False)
    Phone_brand = db.Column(db.String(10), nullable = False)
    Phone_target_group = db.Column(db.String(20), nullable = False)
>>>>>>> Stashed changes

