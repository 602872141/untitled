import requests
from pyquery import PyQuery as pq


'''
CSS 选择器
id #
class .
节点 不用
遍历 itmes()
获取文本 text()
----------------------
查找父节点
一个parent
多个parents
查找兄弟节点
sibings

'''




# url='http://yunvs.com/list/mai_1.html'
url='https://maoyan.com/board/4?offset=0'
headers = {

    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
    }
request = requests.get(url, headers=headers)
html=request.text
doc=pq(html)

for items in doc('div .main').find('dd').items():
    print(items('i.board-index').text())
    print(items('img.board-img').attr('data-src'))
    # print(items('img:last-child').attr('data-src'))麻烦死了
    print(items('img.board-img').attr('alt'))
    print(items('p.star').text())
    print(items('p.releasetime').text())
    print(items('p.score i.integer').text()+items('p.score i.fraction').text())
#coding=utf-8
from pyquery import PyQuery as pq
from lxml import etree
# from pyquery import PyQuery as pq
# from lxml import etree
#
#
# v_source=pq(url='http://yunvs.com/list/mai_1.html')
#
#
# for data in v_source('tr'):
#     print(pq(data).text())
