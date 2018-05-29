# import time
# import threading
#
#
# def run(n):
#     print("task___%s___"%n)
#     time.sleep(2)
#     print("task done",n)
#
#
# start_time = time.time()
# threa_list =[]
# for i in range(50):
#     t = threading.Thread(target=run, args=("%s"%i,))
#     t.start()
#     threa_list.append(t)
# for o in threa_list:
#     o.join()
#
# end_time = time.time()
#
# print("--all threads has finisde..--")
# print("cost ",end_time-start_time)
# print("\033[41;1mred light is on....\033[0m")、

# from threading import Lock ,Thread
#
# def f(lock):
#     # Lock.acquire()
#     global mun
#     mun+=1
#     # Lock.release()
# if __name__=="__main__":
#     mun=0
#     lock = Lock()
#     for i in range(100):
#         q=Thread(target=f,args=(lock,))
#         q.start()
#     print(mun)
# import re
#
# re.compile("\d{5}","45464456")
# import threading,time
# event = threading.Event()
# def lighter():
#     count = 0
#     event.set() #先设置绿灯
#     while True:
#         if count >5 and count < 10: #改成红灯
#             event.clear() #把标志位清了
#             print("\033[41;1mred light is on....\033[0m")
#         elif count >10:
#             event.set() #变绿灯
#             count = 0
#         else:
#             print("\033[42;1mgreen light is on....\033[0m")
#         time.sleep(1)
#         count +=1
#
#
# def car(name):
#     while True:
#         if event.is_set(): #代表绿灯
#             print("[%s] running..."% name )
#             time.sleep(1)
#         else:
#             print("[%s] sees red light , waiting...." %name)
#             event.wait()
#             print("\033[34;1m[%s] green light is on, start going...\033[0m" %name)
#
#
#
# Ligther = threading.Thread(target=lighter,)
# Ligther.start()
# Car=threading.Thread(target=car,args=("Tesla",))
# Car.start()
#
#

# from  multiprocessing import Queue,Process
# import threading
# def f(qq):
#     print("子进程")
#     qq.put("子线程发出的信息")
#
# if __name__ == "__main__":
#    q = Queue()
#    q.put("主进程发出的信息")
#    ff=Process(target=f,args=(q,))
#
#    ff.start()
#    ff.join()
#
#    print(q.get())
#    print(q.get())


# from selenium import webdriver
# browser = webdriver.Chrome()
#
# from bs4 import BeautifulSoup
# soup = BeautifulSoup("<p>hello</p>","lxml")
# print(soup.p.string)
import csv

import  pyquery
import aiohttp

# from flask import Flask
#
# app = Flask(__name__)
#
#
# @app.route("/")
# def hello():
#     return "Hello World!"
#
#
# if __name__ == "__main__":
#     app.run()
# 1
# from flask import Flask
#
# app = Flask(__name__)
#
#
# @app.route("/")
# def hello():
#     return "Hello World!"
#
#
# if __name__ == "__main__":
#     app.run()
#
import tornado.ioloop
import tornado.web
#
#
# class MainHandler(tornado.web.RequestHandler):
#     def get(self):
#         self.write("Hello, world")
#
#
# def make_app():
#     return tornado.web.Application([
#         (r"/", MainHandler),
#     ])
#
#
# if __name__ == "__main__":
#     app = make_app()
#     app.listen(8888)
#     tornado.ioloop.IOLoop.current().start()
#
#
#
#

with open('maoyanTOP001.csv','r') as r:
    Reader=csv.reader(r)
    for rpw in Reader:
        print(rpw)


