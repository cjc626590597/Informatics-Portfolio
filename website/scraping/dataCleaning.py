import re
import xlrd
import xlwt

def main():
# Open the excel to data cleaning
    data=xlrd.open_workbook("data/Chinese/asd10.xls")
    table=data.sheets()[0]
    nrows=table.nrows
    ncols=table.ncols
    dataList=[]
    brand = []
    for i in range(1,nrows):
        rowValues=table.row_values(i)
        data = []
        for j in range(len(rowValues)):
            if j==0: #Phone_name
                rawValue = rowValues[j]
                rowValues[j] = rowValues[j].replace('一加','OnePlus ').replace('三星','Samsung ').replace('苹果','Apple ').replace('荣耀','Glory ').replace('华为','Huawei ').replace('诺基亚','Nokia ')
                rowValues[j] = rowValues[j].replace('魅族','Meizu ').replace('小米','Xiaomi ').replace('黑鲨','Blackshark ').replace('努比亚','Nubia ').replace('海信','Hisense ').replace('索尼','Sony ').replace('朵唯','DOOV ')
                rowValues[j] = rowValues[j].replace('金立', 'Gionee ').replace('美图', 'Meitu ').replace('黑莓', 'BlackBerry ').replace('金立', 'Gionee ').replace('中兴', 'ZTH ').replace('金立', 'Gionee ').replace('锤子科技坚果','Smartisan ').replace('钛金手机','Titanium mobile phone ')
                rowValues[j] = rowValues[j].replace('联想', 'Lenovo ').replace('华硕', 'ASUS ').replace('夏普', 'Sharp ').replace('华硕', 'ASUS ').replace('小辣椒', 'Xiaolajiao ').replace('格力', 'Gree ').replace('酷派', 'Coolpad ').replace('兰博基尼', 'Lamborghini ')
                rowValues[j] = rowValues[j].replace('畅享', 'Enjoy ').replace('青春', 'Youth ').replace('游戏手机', 'Gaming Phone ').replace('红魔', 'Red Devils ').replace('魅蓝', 'Meizu Blue ').replace('精英', 'Elite ').replace('中国电信', 'China Telecom ')
                rowValues[j] = rowValues[j].replace('全网通',' All Netcom ').replace('版',' version').replace('参数',' parameters').replace('国际',' international').replace('高配',' High dividend').replace('手机','mobile phone')
                pattern = re.compile(r' .*parameters$')
                rawValue = re.sub(pattern, '', rowValues[j])
                brand.append(rawValue)
            elif j==1: #Phone_price
                rowValues[j] = rowValues[j].replace('（预售）','')
            elif j==3: #Phone_screen_size
                pattern = re.compile(r'英寸.*$')
                rowValues[j] = re.sub(pattern, '英寸', rowValues[j])
                rowValues[j] = rowValues[j].replace('英寸',' inches')
            elif j==5: #Phone_resolution
                pattern = re.compile(r'^.*像素')
                rowValues[j] = re.sub(pattern, '', rowValues[j])
                pattern = re.compile(r'清.*$')
                rowValues[j] = re.sub(pattern, '清', rowValues[j])
                rowValues[j] = rowValues[j].replace('高清', '').replace('超清', '').replace('普清', '')
            elif j==6: #Phone_frequency
                rowValues[j] = rowValues[j].replace('（大四核）','*4').replace('（小四核）','*4').replace('（大两核）','*2').replace('（大双核）','*2').replace('（小六核）','*6').replace('+微智核i7','').replace('+微智核i6','').replace('，','+')
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
            elif j==14: #Phone_brand
                pass
            data.append(rowValues[j])
        # print(data)
        dataList.append(data)

# Put the data to new excel
    book = xlwt.Workbook(encoding="utf-8", style_compression=0)
    sheet = book.add_sheet("实验", cell_overwrite_ok=True)
    col = ("Phone_name", "Phone_price", "Phone_factory_system_kernel", "Phone_screen_size", "Phone_OS", "Phone_resolution",
           "Phone_frequency", "Phone_kernel_num", "Phone_RAM_capacity", "Phone_ROM_capacity", "Phone_battery_capacity",
           "Phone_rear_camera", "Phone_front_camera", "Phone_pic_URL", "Phone_brand", "Phone_target_group")
    for i in range(0, 16):
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
        sheet.write(i + 1, 14, brand[i])
    book.save("./data/English/English10.xls")

if __name__ == '__main__':
    main()