import re
import xlrd
import xlwt

# 打开表格进行数据清洗
data=xlrd.open_workbook("data/Chinese/asd10.xls")
table=data.sheets()[0]
nrows=table.nrows
ncols=table.ncols
dataList=[]
for i in range(1,nrows):
    rowValues=table.row_values(i)
    data = []
    for j in range(len(rowValues)):
        if j==0: #Phone_name
            rowValues[j] = rowValues[j].replace('一加','One Plus ').replace('三星','One Plus ').replace('苹果','Apple ').replace('荣耀','Glory ').replace('华为','Huawei ')
            rowValues[j] = rowValues[j].replace('魅族','Meizu ').replace('小米','Xiaomi ')
            rowValues[j] = rowValues[j].replace('全网通',' All Netcom ').replace('版',' version').replace('参数',' parameters')
        elif j==3: #Phone_screen_size
            pattern = re.compile(r'英寸.*$')
            rowValues[j] = re.sub(pattern, '英寸', rowValues[j])
            rowValues[j] = rowValues[j].replace('英寸',' inches')
        elif j==5: #Phone_resolution
            pattern = re.compile(r'像素.*$')
            rowValues[j] = re.sub(pattern, '像素', rowValues[j])
            pattern = re.compile(r'1080P高清.*$')
            rowValues[j] = re.sub(pattern, '', rowValues[j])
            rowValues[j] = rowValues[j].replace('像素', ' Pixel')
        elif j==7: #Phone_kernel_num
            rowValues[j] = rowValues[j].replace('八核','eight-core').replace('六核','six-core').replace('四核','four-core')
        elif j==8: #Phone_RAM_capacity
            pattern = re.compile(r'游戏运行.*$')
            rowValues[j] = re.sub(pattern, '', rowValues[j])
        elif j==9: #Phone_ROM_capacity
            pattern = re.compile(r'GB.*$')
            rowValues[j] = re.sub(pattern, 'GB', rowValues[j])
        elif j==10: #Phone_battery_capacity
            pattern = re.compile(r'mAh.*$')
            rowValues[j] = re.sub(pattern, 'mAh', rowValues[j])
        elif j==11: #Phone_rear_camera
            pattern = re.compile(r'00万.*高清像素手机$')
            rowValues[j] = re.sub(pattern, ' million pixels', rowValues[j])
            rowValues[j] = rowValues[j].replace('双','')
        elif j==12: #Phone_front_camera
            pattern = re.compile(r'00万像素.*$')
            rowValues[j] = re.sub(pattern, ' million pixels', rowValues[j])
        data.append(rowValues[j])
    print(data)
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
book.save("./data/English/English10.xls")


