#-*-codeing = utf-8 -*-
#@Time : 2020/8/8 22:48
import bs4
from bs4 import BeautifulSoup     #网页解析，获取数据
import re      #正则表达式
import urllib.request,urllib.error        #制定URL,获取网页数据
import xlwt
from init import db
from models import Phone

from models import Phone
import pandas as pd

def main():
    # 1 获取URL
    urlList = getURL()
    # print(urlList)
    # 2 爬取网页
    datalist = getData(urlList)


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
        datas["手机名"] = phoneName

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
                            datas["电商报价"] = td
                        elif th == "出厂系统内核":
                            datas["出厂系统内核"] = td
                        elif th == "主屏尺寸":
                            datas["主屏尺寸"] = td
                        elif th == "操作系统":
                            datas["操作系统"] = td
                        elif th == "主屏分辨率":
                            datas["主屏分辨率"] = td
                        elif th == "CPU频率":
                            datas["CPU频率"] = td
                        elif th == "核心数":
                            datas["核心数"] = td
                        elif th == "RAM容量":
                            datas["RAM容量"] = td
                        elif th == "ROM容量":
                            datas["ROM容量"] = td
                        elif th == "电池容量":
                            datas["电池容量"] = td
                        elif th == "后置摄像头":
                            datas["后置摄像头"] = td
                        elif th == "前置摄像头":
                            datas["前置摄像头"] = td
        phone_div = str(bs.findAll(class_='big-pic-fl'))
        findURL = re.compile(r'<img alt="" heigth="300" src="(.*?)" width="300"/>')
        a = str(re.findall(findURL, phone_div))
        a = a.replace("['", "")
        a = a.replace("']", "")
        datas['手机URL']=a
        # 将一部手机的属性字典加进列表里
        datalist.append(datas)
        saveData(datalist)

        print(url)


#获取手机网页链接
def getURL():
    baseurl = "https://detail.zol.com.cn/cell_phone_index/subcate57_0_list_1_0_1_2_0_"
    urls = []
    for i in range(21,23,1):   ###############################################将(1,2,1)改为(1,100,1)
        url = baseurl + str(i) + ".html"
        html = askURL(url)    #保存获取到的网页源码
        # print(html)

        #2.逐一解析数据
        bs = BeautifulSoup(html,"html.parser")

        for item in bs.select('h3'):
            item = str(item)
            findURL = re.compile(r'<h3><a href="(.*?)" target="_blank".*</span></a></h3>')
            if re.findall(findURL,item):
                urls.append("https://detail.zol.com.cn/"+str(re.findall(findURL,item)[0]))
    # print(urls)

    finalURL = []
    for url in urls:
        html = askURL(url)  # 保存获取到的网页源码
        bs = BeautifulSoup(html, "html.parser")
        for item in bs.findAll(class_='section-more'):
            item = str(item)
            findURL = re.compile(r'<a class="section-more" href="(.*?)">查看完整参数')
            if re.findall(findURL, item):
                finalURL.append("https://detail.zol.com.cn/"+re.findall(findURL, item)[0])
    # print(finalURL)
    return finalURL

#得到指定一个URL的网页内容
def askURL(url):
    head = {             #模拟浏览器头部信息，向豆瓣服务器发送消息
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"
    }
                         #用户代理，表示告诉豆瓣服务器，我们是什么类型的机器、浏览器（本质上是告诉浏览器，我们可以接受什么水平的文件内容）
    request = urllib.request.Request(url,headers=head)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        # html = response.read().decode("utf-8")
        html = response.read().decode("gb18030")
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)
    return html

def saveData(datalist):
     #将字典列表转换为DataFrame
     print("save")
     book=xlwt.Workbook(encoding="utf-8",style_compression=0)
     sheet=book.add_sheet("实验",cell_overwrite_ok=True)
     col=("手机名","电商报价","出厂系统内核","主屏尺寸","操作系统","主屏分辨率","CPU频率","核心数","RAM容量","ROM容量","电池容量","后置摄像头","前置摄像头","手机URL")
     for i in range(0,14):
         sheet.write(0,i,col[i])
     for i in range(0,len(datalist)):
         data=datalist[i]
         print(data)
         for j in range(0,14):
             try:
                temp=data[col[j]]
             except:
                print(col[j]+"获取失败")
             else:
                 sheet.write(i+1,j,temp)
     book.save("asd10.xls")

def upload(datalist):
    col=("手机名","电商报价","出厂系统内核","主屏尺寸","操作系统","主屏分辨率","CPU频率","核心数","RAM容量","ROM容量","电池容量","后置摄像头","前置摄像头","手机URL")
    for i in range(0,len(datalist)):
         data=datalist[i]
main()

