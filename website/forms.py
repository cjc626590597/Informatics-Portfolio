from flask_wtf import FlaskForm
from wtforms import StringField, SelectMultipleField, IntegerField, SubmitField,SelectField,RadioField
from wtforms.validators import InputRequired, Email, Length, EqualTo, ValidationError,DataRequired

class IndexForm(FlaskForm):
    price = SelectField(
        label='*Price',
        validators=[DataRequired('Please select the price range')],
        choices=[(0,''),(1, '0-1000'),(2, '1000-2000'), (3, '2000-3000'), (4, '3000-4000'), (5, '4000-5000'), (6, '5000-6000'),
                 (7, '6000-7000')],
        default = 2,
        coerce=int
    )
    factory_system = RadioField(
        label='*Factory System kernel',
        validators=[DataRequired('Please select the Factory System')],
        choices=[(1, 'IOS'),(2, 'Android')],
        default= 2,
        coerce=int
    )
    phone_screen = SelectField(
        label='*Phone Screen size',
        validators=[DataRequired('Please select the screen size')],
        choices=[(0,''),(1, '2.0~3.0 inches'), (2, '4.0~5.0 inches'), (3, '5.0~6.0 inches'), (4, '6.0~7.0 inches'),
                 (5, '7.0~8.0 inches')],
        default=4,
        coerce=int
    )
    phone_OS = SelectField(
        label='Phone Operate System',
        choices=[(0,''),(1, '360'), (2, 'Android'), (3, 'ColorOS'), (4, 'COOL'),
                 (5, 'EMUI'), (6, 'Flyme'), (7, 'Funtouch'), (8, 'Google'), (9, 'H2OS'), (10, 'HALO'),
                 (11, 'HydrogenOS'),(12, 'iOS'),(13, 'iQOO'),(14, 'JOYUI'),(15, 'KaiOS'),(16, 'Legion'),
                 (17, 'LG'),(18, 'Magic'),(19, 'MiFavor'),(20, 'MIUI'),(21, 'moto'),(22, 'MY'),
                 (23, 'nubia'),(24, 'One'),(25, 'OriginOS'),(26, 'OS'),(27, 'Oxygen'),(28, 'realme')],
        default=3,
        coerce=int
    )
    phone_resolution = SelectField(
        label='Phone Resolution',
        choices=[(0,''),(1,'720P'),(2,'1080P'),(3,'2K'),(4,'4K')],
        default=1,
        coerce=int
    )
    phone_frequency = SelectField(
        label='Phone Frequency',
        choices=[(0,''),(1,'1.0~1.5 GHz'),(2,'1.5~2.0 GHz'),(3,'2.0~2.2 GHz'),(4,'2.2~2.4 GHz'),(5,'2.4~2.6 GHz'),
                 (6,'2.6~2.8 GHz'),(7,'2.8~3.0GHz')],
        default = 2,
        coerce = int
    )
    phone_kernel_num = SelectField(
        label='Phone Kernel Num',
        choices=[(0,''),(1,'1 kernel'),(2,'2 kernel'),(3,'4 kernel'),(4,'6 kernel'),(5,'8 kernel')],
        default=5,
        coerce=int
    )
    phone_RAM_capacity = SelectField(
        label='Phone Random Access Memory',
        choices=[(0,''),(1,'2GB'),(2,'3GB'),(3,'4GB'),(4,'6GB'),(5,'8GB'),(6,'12GB')],
        default=5,
        coerce=int
    )
    phone_ROM_capacity = SelectField(
        label='Phone Read Only Memory',
        choices=[(0,''),(1,'32GB'),(2,'64GB'),(3,'128GB'),(4,'256GB'),(5,'512GB')],
        default=3,
        coerce=int
    )
    phone_battery_capacity = SelectField(
        label='Phone Battery Capacity',
        choices=[(0,''),(1,'1000~2000mAh'),(2,'2000~3000mAh'),(3,'3000~4000mAh'),(4,'4000~5000mAh'),(5,'5000~6000mAh')],
        default=4,
        coerce=int
    )
    phone_rear_camera = SelectField(
        label='Phone Rear Camera',
        choices=[(0,''),(1,'2 million pixels'),(2,'4 million pixels'),(3,'6 million pixels'),(4,'8 million pixels'),
                 (5,'12 million pixels'),(6,'13 million pixels'),(7,'14 million pixels'),(8,'16 million pixels'),
                 (9,'19 million pixels'),(10,'20 million pixels'),(11,'21 million pixels'),(12,'24 million pixels'),
                 (13,'32 million pixels'),(14,'40 million pixels'),(15,'48 million pixels'),(16,'50 million pixels'),
                 (17,'64 million pixels'),(18,'80 million pixels'),(19,'100 million pixels')],
        default=6,
        coerce=int
    )
    phone_front_camera = SelectField(
        label='Phone Front Camera',
        choices=[(0,''),(1,'5 million pixels'),(2,'7 million pixels'),(3,'8 million pixels'),(4,'10 million pixels'),
                 (5,'12 million pixels'),(6,'13 million pixels'),(7,'16 million pixels'),(8,'20 million pixels'),
                 (9,'24 million pixels'),(10,'25 million pixels'),(11,'32 million pixels')],
        default=3,
        coerce=int
    )
    submit = SubmitField('Search')

