import bs4
import xlrd
from bs4 import BeautifulSoup     #网页解析，获取数据
import re      #正则表达式
import urllib.request,urllib.error        #制定URL,获取网页数据
import xlwt
from website.scraping.utils.askHtml import askURL


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
        print(url)
        html = askURL(url)    #保存获取到的网页源码
        #     # print(html)

        #2.逐一解析数据
        bs = BeautifulSoup(html,"html.parser")
        datas = {}  # 存放各种参数
        phoneName = bs.findAll(class_="product-model__name")[0].text
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
                        result[j] = result[j].replace('纠错','').replace('>','') #多余信息替换
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
        # 将一部手机的属性字典加进列表里
        datalist.append(datas)

    return datalist

#保存数据
def saveData(datalist):
     #将字典列表转换为DataFrame
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

