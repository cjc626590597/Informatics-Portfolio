import re
import xlrd

data=xlrd.open_workbook("./data/Chinese1.xls")
table=data.sheets()[0]
nrows=table.nrows
ncols=table.ncols
dataList=[]
for i in range(1,nrows):
    rowValues=table.row_values(i)
    data = []
    for j in range(len(rowValues)):
        if j==0:
            rowValues[j] = rowValues[j].replace('一加','One Plus ').replace('三星','One Plus ').replace('苹果','Apple ').replace('荣耀','Glory ').replace('华为 ','Huawei ')
            rowValues[j] = rowValues[j].replace('全网通',' All Netcom ').replace('版',' version').replace('参数',' parameters')
        elif j==1:
            pass
        elif j==3:
            pattern = re.compile(r'需双手打字.*$')
            rowValues[j] = re.sub(pattern, '', rowValues[j])
            rowValues[j] = rowValues[j].replace('英寸',' inches')
        elif j==4:
            pass
        elif j==5:
            pass
        elif j==6:
            pass
        elif j==7:
            pass
        elif j==8:
            pass
        elif j==9:
            pass
        elif j==10:
            pass
        elif j==11:
            pass
        elif j==12:
            pass
        elif j==13:
            pass
        data.append(rowValues[j])
    print(data)
    dataList.append(data)





