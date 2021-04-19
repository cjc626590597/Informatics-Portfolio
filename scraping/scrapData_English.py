import bs4
import xlrd
from bs4 import BeautifulSoup     #网页解析，获取数据
import re      #正则表达式
import xlwt
from website.scraping.utils.askHtml import askURL
from website.scraping.utils.translate import getTranslate


def main():
    # 1 从表格中获取所有手机URL
    urlList = getURL()
    # 2 爬取网页
    phoneList = getData(urlList)
    # # 3 保存所有手机信息到表格中
    saveData(phoneList)

#获取所有手机网页链接
def getURL():
    data = xlrd.open_workbook("data/URLs.xls")
    table = data.sheets()[0]
    startRows = 1 #一行数据代表一部手机
    endRows = 10
    urlList = []
    for i in range(startRows, endRows): # 9部手机
        rowValues = table.row_values(i)
        urlList.append(rowValues[0])
    return urlList

#爬取网页
def getData(urlList):
    datalist = []
    for url in urlList: #一次性检索不同的url，不同的url代表不同的手机
        html = askURL(url)    #保存获取到的网页源码
        #     # print(html)

        #2.逐一解析数据
        bs = BeautifulSoup(html,"html.parser")
        datas = {}  # 存放各种参数
        phoneName = bs.findAll(class_="product-model__name")[0].text
        phoneName = getTranslate(str(phoneName))  # 翻译为英文
        datas["Phone_name"] = phoneName
        phone_div = str(bs.findAll(class_='big-pic-fl'))
        findURL = re.compile(r'<img alt="" heigth="300" src="(.*?)" width="300"/>')
        phoneUrl = str(re.findall(findURL, phone_div)[0])
        datas['Phone_pic_URL'] = phoneUrl

        # 获取表格的所有参数
        for table in bs.findAll('table'):
            for tr in table.children: #GG是table,children是tr,然后分为th和td
                if type(tr) == bs4.element.Tag:
                    result = str.split(tr.text, '\n')  #tr.text直接获取文本，然后根据换行分隔
                    result = [j for j in result if j != ''] #去除空值
                    for j in range(len(result)):
                        result[j] = getTranslate(result[j]) #翻译为英文
                        result[j] = result[j].replace(' error correction','').replace('>','') #多余信息替换
                    # print(result)  #result即列表['电商报价','￥6989']
                    properties = ['Electricity price','The factory system kernel','The home screen size','The operating system','The home screen resolution','CPU frequency','The core number','RAM capacity','ROM capacity','Battery capacity','The rear camera','Front-facing camera']
                    if result[0] in properties:
                        th = result[0]
                        td = result[1]
                        if th == "Electricity price":
                            datas["Phone_price"] = td
                        elif th == "The factory system kernel":
                            datas["Phone_factory_system_kernel"] = td
                        elif th == "The home screen size":
                            datas["Phone_screen_size"] = td
                        elif th == "The operating system":
                            datas["Phone_OS"] = td
                        elif th == "The home screen resolution":
                            datas["Phone_resolution"] = td
                        elif th == "CPU frequency":
                            datas["Phone_frequency"] = td
                        elif th == "The core number":
                            datas["Phone_kernel_num"] = td
                        elif th == "RAM capacity":
                            datas["Phone_RAM_capacity"] = td
                        elif th == "ROM capacity":
                            datas["Phone_ROM_capacity"] = td
                        elif th == "Battery capacity":
                            datas["Phone_battery_capacity"] = td
                        elif th == "The rear camera":
                            datas["Phone_rear_camera"] = td
                        elif th == "Front-facing camera":
                            datas["Phone_front_camera"] = td

        print(datas)
        # 将一部手机的属性字典加进列表里
        datalist.append(datas)

        # print(datalist)

    return datalist

#保存数据
def saveData(datalist):
     #将字典列表转换为DataFrame
     print("save")
     book=xlwt.Workbook(encoding="utf-8",style_compression=0)
     sheet=book.add_sheet("实验",cell_overwrite_ok=True)
     col=("Phone_name","Phone_price","Phone_factory_system_kernel","Phone_screen_size","Phone_OS","Phone_resolution","Phone_frequency","Phone_kernel_num","Phone_RAM_capacity","Phone_ROM_capacity","Phone_battery_capacity","Phone_rear_camera","Phone_front_camera","Phone_pic_URL")
     for i in range(0,14):
         sheet.write(0,i,col[i])
     for i in range(0,len(datalist)):
         data=datalist[i]
         # print(data)
         for j in range(0,14):
             try:
                temp=data[col[j]]
             except:
                print(col[j]+"message access failed")
             else:
                 sheet.write(i+1,j,temp)
     book.save("./data/English1.xls")

main()


