import bs4
from bs4 import BeautifulSoup     #网页解析，获取数据
import re      #正则表达式
import urllib.request,urllib.error        #制定URL,获取网页数据
import xlwt
from website.scraping.utils.askHtml import askURL

def main():
    # 1 1 Get all the urls from website
    urlList = getURL()
    # 2 Save all the urls to excel
    saveData(urlList)

#Get all the urls from website
def getURL():
    baseurl = "https://detail.zol.com.cn/cell_phone_index/subcate57_0_list_1_0_1_2_0_"
    urls = []
    for i in range(1,20,1):
        url = baseurl + str(i) + ".html"
        html = askURL(url)    #Save the source code
        # print(html)

        bs = BeautifulSoup(html,"html.parser")

        for item in bs.select('h3'):
            item = str(item)
            findURL = re.compile(r'<h3><a href="(.*?)" target="_blank".*</span></a></h3>')
            if re.findall(findURL,item):
                urls.append("https://detail.zol.com.cn/"+str(re.findall(findURL,item)[0]))
    # print(urls)

    finalURL = []
    for url in urls:
        html = askURL(url)  #Save the source code
        bs = BeautifulSoup(html, "html.parser")
        for item in bs.findAll(class_='section-more'):
            item = str(item)
            findURL = re.compile(r'<a class="section-more" href="(.*?)">查看完整参数')
            if re.findall(findURL, item):
                finalURL.append("https://detail.zol.com.cn/"+re.findall(findURL, item)[0])
    # print(finalURL)
    return finalURL

#Save the data
def saveData(urlList):
     #Change the lisst to DataFrame
     print("save")
     book=xlwt.Workbook(encoding="utf-8",style_compression=0)
     sheet=book.add_sheet("URLs",cell_overwrite_ok=True)
     sheet.write(0,0,"URLs")
     for i in range(0, len(urlList)):
         print(urlList[i])
         try:
            temp=urlList[i]
         except:
            print(temp+"access error")
         else:
             sheet.write(i+1,0,temp)
     book.save("./data/URLs.xls")

main()

