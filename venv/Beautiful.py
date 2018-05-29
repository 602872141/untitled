from bs4 import BeautifulSoup

import requests
def open_url(url):
    headers={
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36' }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        # print(response.text)
        return response.text
    return None
def parse_one_page(html):
    spup = BeautifulSoup(html, 'lxml')
    chapters = spup.find_all(name='div', class_="listmain")
    # print(str(chapters))
    download_soup = BeautifulSoup(str(chapters), 'lxml')
    begin_flag = False
    for child in download_soup.dl.children:
        # 滤除回车
        if child != '\n':
            # 找到《一念永恒》正文卷,使能标志位
            if child.string == "《一念永恒》正文卷":
                begin_flag = True
            # 爬取链接
            if begin_flag == True and child.a != None:
                download_url = "http://www.biqukan.com" + child.a['href']
                download_name = child.string
                print(download_name + " : " + download_url)

if __name__=='__main__':
    text=open_url('http://www.biqukan.com/1_1094/')
    parse_one_page(text)