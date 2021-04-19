import urllib.request, urllib.error

from website.decisionTree.decisionTree import retrieveTrainingData, createDecisionTree, predict
from website.models import all_data
from flask_sqlalchemy import SQLAlchemy


# 根据条件检索数据库
def Search(value):
    for i in range(len(value)):
        if value[i] != 0:
            if i == 0:
                min = (int(value[0]) - 1) * 1000
                max = int(value[0]) * 1000
            if i == 1:
                if value[i] == '1':
                    FS = 'IOS'
                else:
                    FS = 'Android'
            if i == 2:
                if value[i] == '1':
                    PSmin = 2.0
                    PSmax = 3.0
                elif value[i] == '2':
                    PSmin = 4.0
                    PSmax = 5.0
                elif value[i] == '3':
                    PSmin = 5.0
                    PSmax = 6.0
                elif value[i] == '4':
                    PSmin = 6.0
                    PSmax = 7.0
                else:
                    PSmin = 7.0
                    PSmax = 8.0
            if i == 3:
                if value[i] == '1':
                    POS = '360'
                if value[i] == '2':
                    POS = 'Android'
                if value[i] == '3':
                    POS = 'ColorOS'
                if value[i] == '4':
                    POS = 'COOL'
                if value[i] == '5':
                    POS = 'EMUI'
                if value[i] == '6':
                    POS = 'Flyme'
                if value[i] == '7':
                    POS = 'Funtouch'
                if value[i] == '8':
                    POS = 'Google'
                if value[i] == '9':
                    POS = 'H2OS'
                if value[i] == '10':
                    POS = 'HALO'
                if value[i] == '11':
                    POS = 'HydrogenOS'
                if value[i] == '12':
                    POS = 'iOS'
                if value[i] == '13':
                    POS = 'iQOO'
                if value[i] == '14':
                    POS = 'JOYUI'
                if value[i] == '15':
                    POS = 'KaiOS'
                if value[i] == '16':
                    POS = 'Legion'
                if value[i] == '17':
                    POS = 'LG'
                if value[i] == '18':
                    POS = 'Magic'
                if value[i] == '19':
                    POS = 'MiFavor'
                if value[i] == '20':
                    POS = 'MIUI'
                if value[i] == '21':
                    POS = 'moto'
                if value[i] == '22':
                    POS = 'MY'
                if value[i] == '23':
                    POS = 'nubia'
                if value[i] == '24':
                    POS = 'One'
                if value[i] == '25':
                    POS = 'OriginOS'
                if value[i] == '26':
                    POS = 'OS'
                if value[i] == '27':
                    POS = 'Oxygen'
                if value[i] == '28':
                    POS = 'realme'
            if i == 4:
                if value[i] == '1':
                    PR = '720P'
                if value[i] == '2':
                    PR = '1080P'
                if value[i] == '3':
                    PR = '2k'
                if value[i] == '4':
                    PR = '4K'
            if i == 5:
                if value[i] == '1':
                    PFmin = 1.0
                    PFmax = 1.5
                if value[i] == '2':
                    PFmin = 1.5
                    PFmax = 2.0
                if value[i] == '3':
                    PFmin = 2.0
                    PFmax = 2.2
                if value[i] == '4':
                    PFmin = 2.2
                    PFmax = 2.4
                if value[i] == '5':
                    PFmin = 2.4
                    PFmax = 2.6
                if value[i] == '6':
                    PFmin = 2.6
                    PFmax = 2.8
                if value[i] == '7':
                    PFmin = 2.8
                    PFmax = 3.0
            if i == 6:
                if value[i] == '1':
                    PKN = 1
                if value[i] == '2':
                    PKN = 2
                if value[i] == '3':
                    PKN = 4
                if value[i] == '4':
                    PKN = 6
                if value[i] == '5':
                    PKN = 8
            if i == 7:
                if value[i] == '1':
                    PRAM = 2
                if value[i] == '2':
                    PRAM = 3
                if value[i] == '3':
                    PRAM = 4
                if value[i] == '4':
                    PRAM = 6
                if value[i] == '5':
                    PRAM = 8
                if value[i] == '6':
                    PRAM = 12
            if i == 8:
                if value[i] == '1':
                    PROM = 32
                if value[i] == '2':
                    PROM = 64
                if value[i] == '3':
                    PROM = 128
                if value[i] == '4':
                    PROM = 256
                if value[i] == '5':
                    PROM = 512
            if i == 9:
                PBCmin = int(value[i]) * 1000
                PBCmax = (int(value[i]) + 1) * 1000
            if i == 10:
                if value[i] == '1':
                    PRC = 2
                if value[i] == '2':
                    PRC = 4
                if value[i] == '3':
                    PRC = 6
                if value[i] == '4':
                    PRC = 8
                if value[i] == '5':
                    PRC = 12
                if value[i] == '6':
                    PRC = 13
                if value[i] == '7':
                    PRC = 14
                if value[i] == '8':
                    PRC = 16
                if value[i] == '9':
                    PRC = 19
                if value[i] == '10':
                    PRC = 20
                if value[i] == '11':
                    PRC = 21
                if value[i] == '12':
                    PRC = 24
                if value[i] == '13':
                    PRC = 32
                if value[i] == '14':
                    PRC = 40
                if value[i] == '15':
                    PRC = 48
                if value[i] == '16':
                    PRC = 50
                if value[i] == '17':
                    PRC = 64
                if value[i] == '18':
                    PRC = 80
                if value[i] == '19':
                    PRC = 100
            if i == 11:
                if value[i] == '1':
                    PFC = 5
                if value[i] == '2':
                    PFC = 7
                if value[i] == '3':
                    PFC = 8
                if value[i] == '4':
                    PFC = 10
                if value[i] == '5':
                    PFC = 12
                if value[i] == '6':
                    PFC = 13
                if value[i] == '7':
                    PFC = 16
                if value[i] == '8':
                    PFC = 20
                if value[i] == '9':
                    PFC = 24
                if value[i] == '10':
                    PFC = 25
                if value[i] == '11':
                    PFC = 32

    data = all_data.query.filter(all_data.Phone_price > min, all_data.Phone_price <= max,
                                 all_data.Phone_factory_system_kernel == FS, all_data.Phone_screen_size >= PSmin,
                                 all_data.Phone_screen_size <= PSmax, all_data.Phone_OS == POS,
                                 all_data.Phone_resolution == PR, all_data.Phone_frequency >= PFmin,
                                 all_data.Phone_frequency <= PFmax, all_data.Phone_kernel_num == PKN,
                                 all_data.Phone_RAM_capacity == PRAM, all_data.Phone_ROM_capacity == PROM,
                                 all_data.Phone_battery_capacity >= PBCmin, all_data.Phone_battery_capacity <= PBCmax,
                                 all_data.Phone_rear_camera == PRC, all_data.Phone_front_camera == PFC).all()
    length = len(data)
    if length == 0:
        data = all_data.query.filter(all_data.Phone_price > min, all_data.Phone_price <= max,
                                     all_data.Phone_factory_system_kernel == FS, all_data.Phone_screen_size >= PSmin,
                                     all_data.Phone_screen_size <= PSmax, all_data.Phone_OS == POS,
                                     all_data.Phone_resolution == PR, all_data.Phone_frequency >= PFmin,
                                     all_data.Phone_frequency <= PFmax, all_data.Phone_kernel_num == PKN,
                                     all_data.Phone_RAM_capacity == PRAM, all_data.Phone_ROM_capacity == PROM,
                                     all_data.Phone_rear_camera == PRC, all_data.Phone_front_camera == PFC).all()
        length = len(data)
        if length == 0:
            data = all_data.query.filter(all_data.Phone_price > min, all_data.Phone_price <= max,
                                         all_data.Phone_factory_system_kernel == FS,
                                         all_data.Phone_screen_size >= PSmin,
                                         all_data.Phone_screen_size <= PSmax, all_data.Phone_OS == POS,
                                         all_data.Phone_resolution == PR, all_data.Phone_frequency >= PFmin,
                                         all_data.Phone_frequency <= PFmax, all_data.Phone_kernel_num == PKN,
                                         all_data.Phone_RAM_capacity == PRAM, all_data.Phone_ROM_capacity == PROM).all()
            length = len(data)
            if length == 0:
                data = all_data.query.filter(all_data.Phone_price > min, all_data.Phone_price <= max,
                                             all_data.Phone_factory_system_kernel == FS,
                                             all_data.Phone_screen_size >= PSmin,
                                             all_data.Phone_screen_size <= PSmax, all_data.Phone_OS == POS,
                                             all_data.Phone_resolution == PR, all_data.Phone_frequency >= PFmin,
                                             all_data.Phone_frequency <= PFmax, all_data.Phone_kernel_num == PKN,
                                             all_data.Phone_RAM_capacity == PRAM).all()
                length = len(data)
                if length == 0:
                    data = all_data.query.filter(all_data.Phone_price > min, all_data.Phone_price <= max,
                                                 all_data.Phone_factory_system_kernel == FS,
                                                 all_data.Phone_screen_size >= PSmin,
                                                 all_data.Phone_screen_size <= PSmax, all_data.Phone_OS == POS,
                                                 all_data.Phone_resolution == PR, all_data.Phone_frequency >= PFmin,
                                                 all_data.Phone_frequency <= PFmax,
                                                 all_data.Phone_kernel_num == PKN).all()
                    length = len(data)
                    if length == 0:
                        data = all_data.query.filter(all_data.Phone_price > min, all_data.Phone_price <= max,
                                                     all_data.Phone_factory_system_kernel == FS,
                                                     all_data.Phone_screen_size >= PSmin,
                                                     all_data.Phone_screen_size <= PSmax, all_data.Phone_OS == POS,
                                                     all_data.Phone_resolution == PR, all_data.Phone_frequency >= PFmin,
                                                     all_data.Phone_frequency <= PFmax).all()
                        length = len(data)
                        if length == 0:
                            data = all_data.query.filter(all_data.Phone_price > min, all_data.Phone_price <= max,
                                                         all_data.Phone_factory_system_kernel == FS,
                                                         all_data.Phone_screen_size >= PSmin,
                                                         all_data.Phone_screen_size <= PSmax, all_data.Phone_OS == POS,
                                                         all_data.Phone_resolution == PR).all()
                            length = len(data)
                            if length == 0:
                                data = all_data.query.filter(all_data.Phone_price > min, all_data.Phone_price <= max,
                                                             all_data.Phone_factory_system_kernel == FS,
                                                             all_data.Phone_screen_size >= PSmin,
                                                             all_data.Phone_screen_size <= PSmax,
                                                             all_data.Phone_OS == POS).all()
                                length = len(data)
                                if length == 0:
                                    data = all_data.query.filter(all_data.Phone_price > min,
                                                                 all_data.Phone_price <= max,
                                                                 all_data.Phone_factory_system_kernel == FS,
                                                                 all_data.Phone_screen_size >= PSmin,
                                                                 all_data.Phone_screen_size <= PSmax).all()
                                    length = len(data)
                                    if length == 0:
                                        data = all_data.query.filter(all_data.Phone_price > min,
                                                                     all_data.Phone_price <= max,
                                                                     all_data.Phone_factory_system_kernel == FS).all()
                                        length = len(data)
                                        if length == 0:
                                            data = all_data.query.filter(all_data.Phone_price > min,
                                                                         all_data.Phone_price <= max).all()
    # #TODO: data for test
    data = all_data.query.filter(all_data.Phone_price > min,
                                 all_data.Phone_price <= max).all()
    _dataSet, _features = retrieveTrainingData()
    _root = createDecisionTree(_dataSet, _features)
    for item in data:
        phone = [item.Phone_price,
                 item.Phone_factory_system_kernel,
                 item.Phone_screen_size,
                 item.Phone_OS,
                 item.Phone_resolution,
                 item.Phone_frequency,
                 item.Phone_kernel_num,
                 item.Phone_RAM_capacity,
                 item.Phone_ROM_capacity,
                 item.Phone_battery_capacity,
                 item.Phone_rear_camera,
                 item.Phone_front_camera,
                 item.Phone_brand]
        item.Phone_target_group = predict(_root, phone, _features)
    print(data)
    return data
