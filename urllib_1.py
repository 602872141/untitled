import urllib.request
from bs4 import BeautifulSoup
import  re,requests
# request = urllib.request.urlopen("Https://baidu.com/")
# request.status ./?integer">(.*?)</i>.*?fraction">(.*?)</p>.*?</dd>
# html=request.read()<dd>.*?board-index.*?>(.*?)</i>.*?title="(.*?)".*?data-src="(.*?)"
# print(request.getheaders)<dd>.*?board-index-1">(.*?)</i>.*?title="(.*?)".*?board-img" src="(.*?)".*?class="name".*?star+>(.*?)</p>.*?relesetime">(.*?)</p>.*?integer">(.*?)</i>.*?fraction(.*?)</i>.*?</dd>
url = "https://maoyan.com/board/4?offset=0"
pattern=re.compile(
    '<dd>.*?board-index.*?>(.*?)</i>.*?data-src="(.*?)".*?title="(.*?)".*?class="star">(.*?)</p>.*?releasetime">(.*?)</p>.*?"integer">(.*?)</i>.*?"fraction">(.*?)</i>.*?</dd>',re.S)

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
    }
html = requests.get(url, headers=headers).text
text=BeautifulSoup(html,'lxml')
# print(text.findAll(name='dl',class_="board-wrapper"))
text1=BeautifulSoup(str(text.findAll(name='dl',class_="board-wrapper")),'lxml')
# print(text1.findAll(name='dd'))

for item in text1.findAll(name='dd'):
    if item.a.img['alt'] != '':
        print(item.a.img['alt'])
        print(item.a.img['alt'])


# print(items)