from flask_wtf import FlaskForm
from wtforms import StringField, SelectMultipleField, IntegerField, SubmitField,SelectField,RadioField
from wtforms.validators import InputRequired, Email, Length, EqualTo, ValidationError,DataRequired

class IndexForm(FlaskForm):
    price = SelectField(
        label='*Price',
        validators=[DataRequired('Please select the price range')],
        choices=[(0,''),(1, '1000-2000'), (2, '2000-3000'), (3, '3000-4000'), (4, '4000-5000'), (5, '5000-6000'),
                 (6, '6000-7000')],
        default = 0,
        coerce=int
    )
    factory_system = RadioField(
        label='*Factory System',
        validators=[DataRequired('Please select the Factory System')],
        choices=[(1, 'Android'), (2, 'IOS')],
        coerce=int
    )
    phone_screen = SelectField(
        label='*Phone Screen',
        validators=[DataRequired('Please select the screen size')],
        choices=[(0,''),(1, '2~2.8 inches'), (2, '4.2~4.7 inches'), (3, '5.05~5.99 inches'), (4, '6.0~6.9 inches'),
                 (5, '7.09~7.92 inches'), (6, '8 inches')],
        default=0,
        coerce=int
    )
    phone_OS = SelectField(
        label='Phone Operate System',
        choices=[(0,''),(1, 'Harmony'), (2, 'TiJOS'), (3, 'Android'), (4, 'Droi'),
                 (5, 'samsung'), (6, 'ZUI'), (7, 'ZenUI'), (8, 'water'), (9, 'Surface Duo UI'), (10, 'Surface Duo UI'),
                 (11, 'Smartisan'),(12, 'ROG UI'),(13, 'Redmagic'),(14, 'realme UI'),(15, 'Oxygen OS'),(16, 'OneUI'),
                 (17, 'nubia UI'),(18, 'MY UI'),(19, 'moto UI'),(20, 'MIUI'),(21, 'MiFavor'),(22, 'Magic'),
                 (23, 'LG UX'),(24, 'Legion'),(25, 'Kai'),(26, 'JOYUI'),(27, 'iQOO'),(28, 'IOS'),(29, 'HydrogenOS'),
                 (30, 'Hydrogen'),(31, 'HALO'),(32, 'H2OS'),(33, 'Google Android Pie'),(34, 'Funtouch OS'),
                 (35, 'Flyme OS'),(36, 'EMUI'),(37, 'COOL UI'),(38, 'ColorOS'),(39, '360 OS')],
        default=0,
        coerce=int
    )
    phone_resolution = SelectField(
        label='Phone Resolution',
        choices=[(0,''),(1,'720P'),(2,'1080P'),(3,'2K'),(4,'4K')],
        default=0,
        coerce=int
    )
    phone_frequency = SelectField(
        label='Phone Frequency',
        choices=[(0,''),(1,'1.0~1.5 GHz'),(2,'1.5~2.0 GHz'),(3,'2.0~2.2 GHz'),(4,'2.2~2.4 GHz'),(5,'2.4~2.6 GHz'),
                 (6,'2.6~2.8 GHz'),(7,'2.8~3.0GHz')],
        default = 0,
        coerce = int
    )
    phone_kernel_num = SelectField(
        label='Phone Kernel Num',
        choices=[(0,''),(1,'4 kernel'),(2,'6 kernel'),(3,'8 kernel')],
        default=0,
        coerce=int
    )
    phone_RAM_capacity = SelectField(
        label='Phone Random Access Memory',
        choices=[(0,''),(1,'2GB'),(2,'3GB'),(3,'4GB'),(4,'6GB'),(5,'8GB'),(6,'12GB')],
        default=0,
        coerce=int
    )
    phone_ROM_capacity = SelectField(
        label='Phone Read Only Memory',
        choices=[(0,''),(1,'32GB'),(2,'64GB'),(3,'128GB'),(4,'256GB'),(5,'512GB'),(6,'1TB')],
        default=0,
        coerce=int
    )
    phone_battery_capacity = SelectField(
        label='Phone Battery Capacity',
        choices=[(0,''),(1,'1000~2000mAh'),(2,'2000~3000mAh'),(3,'3000~4000mAh'),(4,'4000~5000mAh'),(5,'5000~6000mAh'),
                 (6,'10000mAh')],
        default=0,
        coerce=int
    )
    phone_rear_camera = SelectField(
        label='Phone Rear Camera',
        choices=[(0,''),(1,'8 million pixels'),(2,'12 million pixels'),(3,'13 million pixels'),(4,'16 million pixels'),
                 (5,'20 million pixels'),(6,'24 million pixels'),(7,'40 million pixels'),(8,'48 million pixels'),
                 (9,'50 million pixels'),(10,'64 million pixels'),(11,'100 million pixels'),(12,'108 million pixels')],
        default=0,
        coerce=int
    )
    phone_front_camera = SelectField(
        label='Phone Front Camera',
        choices=[(0,''),(1,'5 million pixels'),(2,'7 million pixels'),(3,'8 million pixels'),(4,'10 million pixels'),
                 (5,'12 million pixels'),(6,'13 million pixels'),(7,'16 million pixels'),(8,'20 million pixels'),
                 (9,'24 million pixels'),(10,'24.8 million pixels'),(11,'25 million pixels'),(12,'32 million pixels'),
                 (13,'40 million pixels'),(14,'44 million pixels')],
        default=0,
        coerce=int
    )
    submit = SubmitField('Search')
