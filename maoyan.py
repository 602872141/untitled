import csv
import time

import requests,re,json

def get_one_page(url):
    headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
    }
    request=requests.get(url,headers=headers)
    if request.status_code == 200:

        return request.text
    return None
def parse_one_page(html):
    patten=re.compile(
        '<dd>.*?board-index.*?>(.*?)</i>.*?data-src="(.*?)".*?title="(.*?)".*?class="star">(.*?)</p>.*?releasetime">(.*?)</p>.*?"integer">(.*?)</i>.*?"fraction">(.*?)</i>.*?</dd>',re.S
    )
    items = re.findall(patten,html)
    print(items)
    for item in items:
        yield {
            'index':item[0],
            'image':item[1],
            'title':item[2],
            'actor':item[3].strip(),
            'time':item[4].strip(),
            'score':item[5].strip()+item[6].strip()
        }
def writ_to_file(content):
    with open('maoyanTOP100','a',encoding='utf-8') as f:
        f.write(json.dumps(content,ensure_ascii=False)+ '\n')
    with open('maoyanTOP001.csv', 'a', encoding='utf-8') as f:
        fieldname=['index','image','title','actor','time','score']
        writer = csv.DictWriter(f, fieldnames=fieldname)
        writer.writeheader()
        writer.writerow(content)

def main(offset):
    url="https://maoyan.com/board/4?offset="+str(offset)
    print(url)
    text=get_one_page(url)
    for item in parse_one_page(text):
        writ_to_file(item)
if __name__=='__main__':
    for i in range(10):
        main(offset=i*10)
        time.sleep(1)