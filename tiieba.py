import urllib.request
import requests

def loadPage(fullurl,filename):
    print("正在下载"+filename)
    Request = urllib.request.Request(fullurl)
    Request.add_header()
    urllib.request.urlopen(fullurl,)

def TiebaSqlie(url,beginpage,endpage):
    """"
        作用 ：贴吧爬虫调度器，负责组合处理每个页面的Url
        url:贴吧yrl的前部分
        beginpage；启示页
        endpage；结束页
    """
    for page in range(beginpage,endpage+1):
        pn = (page-1)*50
        filename="第"+page+"页.html"
        fullurl = url + "%pn=" + pn
        loadPage(fullurl,filename)
        print(fullurl)

if __name__ =="__main__":
    kw = input("输入你要爬去的贴吧")
    beginpage=int(input("请输入启示页"))
    endpage=int(input("请输入结束页"))

    url="http://tieba.baidu.com/f?"
    key=urllib.request.urlencode({"kw":kw})
    fullurl=url +key
    TiebaSqlie(fullurl,beginpage,endpage)

