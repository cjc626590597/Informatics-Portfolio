import re
import xlrd
import xlwt

def main():
# 打开表格进行数据清洗
    data=xlrd.open_workbook("data/English/English0.xls")
    table=data.sheets()[0]
    nrows=table.nrows
    ncols=table.ncols
    dataList=[]
    brand = []
    for i in range(1,nrows):
        rowValues=table.row_values(i)
        data = []
        for j in range(len(rowValues)):
            if j==1: # Phone_price
                print(rowValues[j])
                if rowValues[j]!='':
                    # rowValues[j] = int(rowValues[j].split('￥')[1])
                    rowValues[j] = int(rowValues[j].split('￥')[1])

                    # if 0 <= rowValues[j] < 2000:
                    #     rowValues[j] = "0~2000￥"
                    # elif 2000 <= str < 4000:
                    #     rowValues[j] = "2000~4000￥"
                    # elif 4000 <= str < 6000:
                    #     rowValues[j] = "4000~6000￥"
                    # elif 6000 <= str < 8000:
                    #     rowValues[j] = "6000~8000￥"
                    # elif 8000 <= str < 10000:
                    #     rowValues[j] = "8000~10000￥"
                    # elif 10000 <= str:
                    #     rowValues[j] = "more than 10000￥"
                    # print(rowValues[j])
            elif j==3: #Phone_screen_size
                pass
            elif j==5: #Phone_resolution
                pass
            elif j==7: #Phone_kernel_num
                pass
            elif j==8: #Phone_RAM_capacity
                pass
            elif j==9: #Phone_ROM_capacity
                pass
            elif j==10: #Phone_battery_capacity
                pass
            elif j==11: #Phone_rear_camera
                pass
            elif j==12: #Phone_front_camera
                pass
            elif j==14: #Phone_brand
                pass
            data.append(rowValues[j])
        # print(data)
        dataList.append(data)

# 数据清洗完存进新的表格中
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
    book.save("./data/FinalData/Data0.xls")

if __name__ == '__main__':
    main()