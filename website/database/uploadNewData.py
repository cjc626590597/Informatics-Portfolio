import xlrd
from __init__ import db
from website.database.models import allData

data = xlrd.open_workbook('newData.xls')
table = data.sheets()[0]
nrows = table.nrows
ncols = table.ncols
dataList = []
for i in range(1, nrows):
    rowValues = table.row_values(i)
    data = []
    for item in rowValues:
        data.append(item)
    dataList.append(data)

for i in range(0, len(dataList)):
    post = allData(Phone_name=dataList[i][0], Phone_price=dataList[i][1], Phone_factory_system_kernel=dataList[i][2],
                   Phone_screen_size=dataList[i][3], Phone_OS=dataList[i][4], Phone_resolution=dataList[i][5]
                   , Phone_frequency=dataList[i][6], Phone_kernel_num=dataList[i][7], Phone_RAM_capacity=dataList[i][8],
                   Phone_ROM_capacity=dataList[i][9], Phone_battery_capacity=dataList[i][10],
                   Phone_rear_camera=dataList[i][11],
                   Phone_front_camera=dataList[i][12], Phone_pic_URL=dataList[i][13], Phone_brand=dataList[i][14],
                   Phone_target_group=dataList[i][15])
    db.session.add(post)
    db.session.commit()
