import bs4
import xlrd
from bs4 import BeautifulSoup     #网页解析，获取数据
import re      #正则表达式
import urllib.request,urllib.error        #制定URL,获取网页数据
import xlwt
from website.scraping.utils.askHtml import askURL


def main():
    # 1 Get all the urls in URLs.xls
    urlList = getURL()
    # 2 Scraping the data
    phoneList = getData(urlList)
    # 3 Save the data to excel
    saveData(phoneList)

#Get all the urls in URLs.xls
def getURL():
    data = xlrd.open_workbook("data/URLs.xls")
    table = data.sheets()[0]
    startRows = 1 # A row data means a phone
    endRows = 10
    urlList = []
    for i in range(startRows, endRows):
        rowValues = table.row_values(i)
        urlList.append(rowValues[0])
    return urlList

#Scrap the website
def getData(urlList):
    datalist = []
    for url in urlList: #Retrieval different urls at a time, different urls mean different phoens
        print(url)
        html = askURL(url)    #Protect website source codes
        #     # print(html)

        bs = BeautifulSoup(html,"html.parser")
        datas = {}  # Save all data
        phoneName = bs.findAll(class_="product-model__name")[0].text
        datas["Phone_name"] = phoneName
        phone_div = str(bs.findAll(class_='big-pic-fl'))
        findURL = re.compile(r'<img alt="" heigth="300" src="(.*?)" width="300"/>')
        phoneUrl = str(re.findall(findURL, phone_div)[0])
        datas['Phone_pic_URL'] = phoneUrl

        # Save all data of excel
        for table in bs.findAll('table'):
            for tr in table.children: #GG is table,children is tr
                if type(tr) == bs4.element.Tag:
                    result = str.split(tr.text, '\n')  #tr.text
                    result = [j for j in result if j != ''] #Remove null value
                    for j in range(len(result)):
                        result[j] = result[j].replace('纠错','').replace('>','')
                    # print(result)  #result即列表['电商报价','￥6989']
                    properties = ['电商报价','出厂系统内核','主屏尺寸','操作系统','主屏分辨率','CPU频率','核心数','RAM容量','ROM容量','电池容量','后置摄像头','前置摄像头']
                    if result[0] in properties:
                        th = result[0]
                        td = result[1]
                        if th == "电商报价":
                            datas["Phone_price"] = td
                        elif th == "出厂系统内核":
                            datas["Phone_factory_system_kernel"] = td
                        elif th == "主屏尺寸":
                            datas["Phone_screen_size"] = td
                        elif th == "操作系统":
                            datas["Phone_OS"] = td
                        elif th == "主屏分辨率":
                            datas["Phone_resolution"] = td
                        elif th == "CPU频率":
                            datas["Phone_frequency"] = td
                        elif th == "核心数":
                            datas["Phone_kernel_num"] = td
                        elif th == "RAM容量":
                            datas["Phone_RAM_capacity"] = td
                        elif th == "ROM容量":
                            datas["Phone_ROM_capacity"] = td
                        elif th == "电池容量":
                            datas["Phone_battery_capacity"] = td
                        elif th == "后置摄像头":
                            datas["Phone_rear_camera"] = td
                        elif th == "前置摄像头":
                            datas["Phone_front_camera"] = td
        print(datas)
        # 将一部手机的属性字典加进列表里Put dictionary in list
        datalist.append(datas)

    return datalist

#Save the data
def saveData(datalist):
     #Change the list to DataFrame
     print("save")
     book=xlwt.Workbook(encoding="utf-8",style_compression=0)
     sheet=book.add_sheet("experiment",cell_overwrite_ok=True)
     col=("Phone_name","Phone_price","Phone_factory_system_kernel","Phone_screen_size","Phone_OS","Phone_resolution","Phone_frequency","Phone_kernel_num","Phone_RAM_capacity","Phone_ROM_capacity","Phone_battery_capacity","Phone_rear_camera","Phone_front_camera","Phone_pic_URL")
     for i in range(0,14):
         sheet.write(0,i,col[i])
     for i in range(0,len(datalist)):
         data=datalist[i]
         print(data)
         for j in range(0,14):
             try:
                temp=data[col[j]]
                # temp=getTranslate(temp)
             except:
                print(col[j]+"access error")
             else:
                 sheet.write(i+1,j,temp)
     book.save("./data/Chinese1.xls")

main()

