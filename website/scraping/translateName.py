import re
import xlrd
import xlwt
from website.scraping.utils.translate import getTranslate

# 打开表格进行数据清洗
data=xlrd.open_workbook("data/English/English0.xls")
table=data.sheets()[0]
nrows=table.nrows
ncols=table.ncols
dataList=[]
for i in range(1,nrows):
    rowValues=table.row_values(i)
    data = []
    for j in range(len(rowValues)):
        if j==0: #Phone_name
            rowValues[j] = getTranslate(rowValues[j])
        data.append(rowValues[j])
    # print(data)
    dataList.append(data)

# 数据清洗完存进新的表格中
book = xlwt.Workbook(encoding="utf-8", style_compression=0)
sheet = book.add_sheet("实验", cell_overwrite_ok=True)
col = ("Phone_name", "Phone_price", "Phone_factory_system_kernel", "Phone_screen_size", "Phone_OS", "Phone_resolution",
       "Phone_frequency", "Phone_kernel_num", "Phone_RAM_capacity", "Phone_ROM_capacity", "Phone_battery_capacity",
       "Phone_rear_camera", "Phone_front_camera", "Phone_pic_URL")
for i in range(0, 14):
    sheet.write(0, i, col[i])
for i in range(0, len(dataList)):
    data = dataList[i]
    # print(data)
    for j in range(0, 14):
        try:
            temp = data[j]
        except:
            print(col[j] + "message access failed")
        else:
            sheet.write(i + 1, j, temp)
book.save("./data/FinalData/English0.xls")


