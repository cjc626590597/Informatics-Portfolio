import re
import xlrd
import xlwt

def main():
# Open the excel to data cleaning
    data=xlrd.open_workbook("data/English/English10.xls")
    table=data.sheets()[0]
    nrows=table.nrows
    ncols=table.ncols
    dataList=[]
    for i in range(1,nrows):
        rowValues=table.row_values(i)
        data = []
        for j in range(len(rowValues)):
            if j==1: # Phone_price
                if rowValues[j]!='':
                    try:
                        rowValues[j] = float(rowValues[j].split('￥')[1])
                    except:
                        print('hahha')
                        print(i)
            elif j==2: #Phone_factory_system_kernel
                if rowValues[j] != '':
                    rowValues[j] = rowValues[j].split(' ')[0]
            elif j==3: #Phone_screen_size
                if rowValues[j] != '':
                    rowValues[j] = float(rowValues[j].split(' ')[0])
            elif j==4: #Phone_OS
                if rowValues[j] != '':
                    rowValues[j] = rowValues[j].split(' ')[0]
            elif j==6: #Phone_frequency
                rowValues[j] = rowValues[j].replace('A55 ', '').replace('A77 ', '').replace('Based ', '').replace('×', 'x').replace(
                    'Cortex-', '').replace('Cortex ','')
                if 'x' in rowValues[j]:
                    isX = True
                else:
                    isX = False
                rowValues[j] = rowValues[j].split("+")
                cpus = []
                nums = []
                sumGhz = 0.0
                sum = 0
                try:
                    if len(rowValues[j]) > 1:
                        if not isX:
                            for str in rowValues[j]:
                                str = str.split("*")
                                cpus.append(float(str[0].split("G")[0]))
                                nums.append(int(str[1]))
                            for i in range(len(cpus)):
                                sumGhz = sumGhz + cpus[i] * nums[i]
                                sum = sum + nums[i]
                            averageCpu = round(sumGhz / sum, 2)
                        elif isX:
                            for str in rowValues[j]:
                                pattern = re.compile(r'A.* ')
                                str = re.sub(pattern, '', str)
                                str = str.split("x")
                                cpus.append(float(str[1].split("G")[0]))
                                nums.append(int(str[0]))
                            for i in range(len(cpus)):
                                sumGhz = sumGhz + cpus[i] * nums[i]
                                sum = sum + nums[i]
                            averageCpu = round(sumGhz / sum, 2)
                        rowValues[j] = averageCpu
                    else:
                        rowValues[j] = float(rowValues[j][0].split("G")[0])
                    print(averageCpu)
                except:
                    print(i)
                    print(rowValues[j])
            elif j==7: #Phone_kernel_num
                if "four" in rowValues[j]:
                    rowValues[j] = 4
                elif "six" in rowValues[j]:
                    rowValues[j] = 6
                elif "eight" in rowValues[j]:
                    rowValues[j] = 8
            elif j==8: #Phone_RAM_capacity
                if rowValues[j] != '':
                    rowValues[j] = rowValues[j].split('/')[0]
                    rowValues[j] = float(rowValues[j].replace('GB',''))
            elif j==9: #Phone_ROM_capacity
                if rowValues[j] != '':
                    rowValues[j] = rowValues[j].split('/')[0]
                    rowValues[j] = float(rowValues[j].replace('GB',''))
            elif j==10: #Phone_battery_capacity
                if rowValues[j] != '':
                    rowValues[j] = float(rowValues[j].replace('mAh',''))
            elif j==11: #Phone_rear_camera
                if rowValues[j] != '':
                    rowValues[j] = float(rowValues[j].split(' ')[0])
            elif j==12: #Phone_front_camera
                if rowValues[j] != '':
                    rowValues[j] = float(rowValues[j].split(' ')[0])
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
        for j in range(0, 15):
            try:
                temp = data[j]
            except:
                print(col[j] + "message access failed")
            else:
                sheet.write(i + 1, j, temp)
    book.save("./data/FinalData/Data10.xls")

if __name__ == '__main__':
    main()