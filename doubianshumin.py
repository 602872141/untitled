import requests
import re
header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
content = requests.get("https://book.douban.com/",headers=header).text
# print(content)
ww='<li.*?href="(.*?)".*?title="(.*?)">.*?more-meta.*?author">(.*?).*?</span>.*?class="year">(.*?)'
ss="""
<li class="">
            <div class="cover">
              <a href="https://book.douban.com/subject/30177173/?icn=index-editionrecommend" title="假如真有时光机">
                <img src="https://img3.doubanio.com/view/subject/m/public/s29756103.jpg" class="" width="115px" height="172px" alt="假如真有时光机">
              </a>
            </div>
                <div class="intervenor-info">
                    <img src="https://img3.doubanio.com/f/book/ef040178fab1770d60e3f2f12ba4c7aa70714396/pics/book/partner/jd_recommend.png" class="jd-icon" width="16" height="16"> 
                    <span>推荐</span>
                </div>
            <div class="info">
              <div class="title">
                <a class="" href="https://book.douban.com/subject/30177173/?icn=index-editionrecommend" title="假如真有时光机">假如真有时光机</a>
              </div>
              <div class="author">
                [日] 村上春树
              </div>
              <div class="more-meta">
                <h4 class="title">
                  假如真有时光机
                </h4>
                <p>
             
                  <span class="author">
                    [日] 村上春树
                  </span>
                  /
                  <span class="year">
                    2018-5-1
                  </span>
                  /
                  <span class="publisher">
                    南海出版公司
                  </span>
                </p>
                <p class="abstract">
                  
                  ❤人生是一条单行线，假如真有时光机，你想实现什么愿望？
❤我至今仍然能历历在目地回忆起沿途的景致，就像想起与恋人约会时走过的路线。
❤村上春树全新旅行随笔隆重登场，与《当我谈跑步时我谈些什么》《我的职业是小说家》并列为村上三大经典之作
❤在焦虑的时代，像村上春树一样享受人生，发现一个温暖有趣的世界
————————————————————————...
                </p>
              </div>
            </div>
          </li>
"""
# pattern = re.compile('.*',re.S)
# result = re.findall('<li.*?cover.*?href="(.*?)".*?title="(.*?)".*?more-meta.*?author">(.*?)</span>.*?year">(.*?)</span>.*?</li>',ss,re.S)
result = re.findall('<li.*?href="(.*?)".*?title="(.*?)">.*?more-meta.*?author">(.*?)</span>.*?class="year"(.*?)</span>.*?</li>',content,re.S)
print(result[0])
