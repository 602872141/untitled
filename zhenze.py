#coding=utf-8
# 导⼊re模块
import re
# 使⽤match⽅法进⾏匹配操作
mm = "c:\\a\\b\\c"
# result = re.match("\d*","45464456")
# 如果上⼀步匹配到数据的话，可以使⽤g


# rou
# p⽅法来提取数据
# print(result)
s=r"\nasd"
s

ret = re.match(r"\\nasd",s)
s
# print(ret)
# print(r"c:\\a")
# print("c:\\a\\b\\c")0-100
# sum=re.match(r"[1-9]?\d$|100","200")
# pp=re.match("[1-9]?\d$","0")

# pp=re.match(r"<h1>(\w{1,20})</h1>","<h1>fsdlfkjlskdjflksjdfl</h1>")
# sss="http://www.interoem.com/messageinfo.asp?id=35"
# # qq=re.match(r"http://.+?/",sss)
# qq=re.sub(r"(http://.+?/).*",lambda x:x.group(1),sss)
# print(qq)
content='http://weibo.com/ comment/ KeraCn'
result1 = re.match('http.*?comment/(.*?)', content)
result2 = re.match('http.*?comment/(.*)', content)
print(result1.group(1)+'\n')
print(result2.group(1))