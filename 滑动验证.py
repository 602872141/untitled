import time

from io import BytesIO
from PIL import Image
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
Email='602872141@qq.com'
POSSWORD='qq602872141'


class GrackGeetrst():
    def __init__(self):
        self.url = 'https://account.geetest.com/login'
        self.browser=webdriver.Chrome()
        self.wait=WebDriverWait(self.browser,20)
        self.email=Email
        self.possword=POSSWORD
    def get_geetest_button(self):
        """
               获取初始验证按钮
               :return:
               """
        self.browser.get(self.url)
        button=self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'geetest_radar_tip')))
        return button
    def get_position(self):
        """
              获取验证码位置
              :return: 验证码位置元组
              """
        image = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'geetest_canvas_img')))
        time.sleep(2)
        location = image.location
        size = image.size()
        top,botton,left,right=location['y'],location['y']+size['height'],location['x'],location['x']+size['width']
        return(top,botton,left,right)
    def get_screenshost(self):
        """
              获取网页截图
              :return: 截图对象
              """
        screenshot = self.browser.get_screenshot_as_png()
        screenshot = Image.open(BytesIO(screenshot))
        return screenshot


    def get_geetest_image(self,name='captcha.png'):
        """
           获取验证码图片
           :return: 图片对象
           """
        top, botton, left, right=self.get_position()
        screenshost = self.get_screenshost()
        crop = screenshost.crop((left, top, right, botton))
        return crop
    def get_slider(self):
        """
            获取滑块
            :return: 滑块对象
            """
        button = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'geetest_slider_button')))
        return button
    def is_pixel_equal(self,image1,image2,x,y):
        """
          判断两个像素是否相同
          :param image1: 图片1
          :param image2: 图片2
          :param x: 位置x
          :param y: 位置y
          :return: 像素是否相同
          """
        pixel1 = image1.load()[x, y]
        pixel2 = image2.load()[x, y]
        threashold=60
        if abs(pixel1[0]-pixel2[0])<threashold and abs(pixel1[1]-pixel2[1])<threashold and abs(pixel1[2]-pixel2[2])<threashold :
            return True
        else:
            return  False
    def get_gap(self,image1,image2):
        """
             获取缺口偏移量
             :param image1: 不带缺口图片
             :param image2: 带缺口图片
             :return:
             """
        left=60
        for i in range(left,image1.size[0]):
            for j in range(image1.size[1]):
                if not self.is_pixel_equal(image1,image2,i,j):
                    left=i
                    return left
        return left
    def get_track(self,distance):
        """
           根据偏移量获取移动轨迹
           :param distance: 偏移量
           :return: 移动轨迹
           """
        # 移动轨迹
        track = []
        # 当前位移
        current = 0
        # 减速条件
        mind=distance* 4/5
        # 时间
        t=0.2
        # 初速度
        v=0

        while current<distance:
            if current<mind :
                # 加速度
                a =2
            else:
    #             开始减速
                a=-3
            # 初速度
            v0=v
            # 当前速度 v= v0+a*t
            v=v0=a*t
            # 移动距离 X=vo*t =1/2*a*t*t
            move=v0*t+1/2*a*t*t
            # 保存当前位移
            current += move
            # 加入轨迹中
            track.append(round(current))
        return track



    def move_to_gap(self,slider,tracks):
        """
            拖动滑块到缺口处
            :param slider: 滑块
            :param track: 轨迹
            :return:
            """
        ActionChains(self.browser).click_and_hold(slider).perform()
        for x in tracks:
            ActionChains(self.browser).move_by_offset(xoffset=x,yoffset=0).perform()
        time.sleep(0.5)
        ActionChains(self.browser).release().perform()


    def get_Login_button(self):
        """
             打开网页输入用户名密码
             :return: None
             """
        self.browser.get('https://account.geetest.com/login')
        email_input = self.wait.until(EC.presence_of_element_located((By.ID,'email')))
        possword_input =  self.wait.until(EC.presence_of_element_located((By.ID,'password')))
        email_input.send_keys(self.email)
        possword_input.send_keys(self.possword)
    def get_enter_button(self):
        enter_button=self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME,'login-btn')))
        return enter_button

    def main(self):
        # 填入账号密码
        self.get_Login_button()
#         开始验证
#         先获取验证码按钮
        geetest_button = self.get_geetest_button()
#         点击按钮
        geetest_button.click()
        time.sleep(1)
#         获取完整的验证图片
        image1=self.get_position()
#         获取验证的按钮
        slider=self.get_slider()
        slider.click()
#         获取残缺的图片
        image2 = self.get_geetest_image()
#          比对图片
        distance = self.get_gap(image1, image2)
#           开始拖动
        track = self.get_track(distance)
        self.move_to_gap(slider,track)

if __name__ == '__main__':
    Grack=GrackGeetrst()
    Grack.main()


