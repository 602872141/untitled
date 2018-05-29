import requests
from urllib.parse import urlencode
from pyquery import PyQuery as pq
from pymongo import MongoClient

base_url = 'https://m.weibo.cn/api/container/getIndex?'
Headers={
'Host':'m.weibo.cn',
'Referer':'https://m.weibo.cn/u/2830678474?display=0&retcode=6102',
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
'X-Requested-With':'XMLHttpRequest'
}
Client=MongoClient()
db=Client['weibo']
collection=db['weibo']
def get_page(page):
    params = {
        'type': 'uid',
        'value': '2830678474',
        'containerid': '1076032830678474',
        'page': page
    }
    url=base_url+urlencode(params)
    request=requests.get(url,headers=Headers)
    if request.status_code == 200:
       return request.json()
def  get_fenxi(json):
    if json:
        items=json.get('data').get('cards')
        for innnte,item in enumerate(items):
            print(innnte)
            item=item.get('mblog')
            if innnte==1:
                continue
            weibo = {}
            weibo['id'] = item.get('id')
            weibo['text'] = pq(item.get('text')).text()
            weibo['attitudes'] = item.get('attitudes_count')
            weibo['comments'] = item.get('comments_count')
            weibo['reposts'] = item.get('reposts_count')
            yield weibo
def save_to_monodb(result):
    if collection.insert_one(result):
        print(result)
if __name__=='__main__':
    for page in range(1,11):
        json=get_page(page)
        results=get_fenxi(json)
        for result in results:
            save_to_monodb(result)


D:\python\Scripts\;D:\python\;
%SystemRoot%\system32;%SystemRoot%;%SystemRoot%\System32\Wbem;%SYSTEMROOT%\System32\WindowsPowerShell\v1.0\;%MYSQL_HOME%\bin;D:\python\Scripts;C:\Git\cmd