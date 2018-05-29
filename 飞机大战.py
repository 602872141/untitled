import pygame
from pygame.locals import *
import random

class BaseBuller(object):
    def __init__(self,screen,x,y,name):
        self.screen = screen
        self.x = x
        self.y = y
        self.image = pygame.image.load(name)

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))
class Bullet(BaseBuller):
    def __init__(self,screen,x,y):
        BaseBuller.__init__(self,screen,x,y,"./bullet2.png")
    def move(self):
        self.y -= 5
    def judge(self):
        if self.y < 0 :
            return True
        else:
            return False
class EnemyBullet(BaseBuller):
    def __init__(self,screen,x,y):
        BaseBuller.__init__(self, screen, x+30, y+30, "./bullet1.png")

    def move(self):
        self.y += 2

    def judge(self):
        if self.y > 890 :
            return True
        else:
            return False

class BasePlane(object):
    def __init__(self,screen_temp,x,y,image_name):
        self.x = x
        self.y = y
        self.screen = screen_temp
        self.image = pygame.image.load(image_name)
        self.bullet_list = []

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))
        for bullet in self.bullet_list:
            bullet.display()
            bullet.move()
            if bullet.judge():
                self.bullet_list.remove(bullet)
class MyPlane(BasePlane):
    def __init__(self,screen_temp):
        BasePlane.__init__(self,screen_temp,230,600,"./hero1.png")
    def moveLeft(self):
        self.x -= 20
    def moveRight(self):
        self.x += 20
    def sheBullet(self):
        self.bullet_list.append(Bullet(self.screen,self.x+46,self.y-25))
class EnemyPlane(BasePlane):
    def __init__(self,screen):
        BasePlane.__init__(self,screen,0,0,"./enemy1.png")

        self.direction = "right"


    def move(self):
       if self.direction == "right":
           self.x += 3
       if self.direction == "left":
           self.x -= 3
       if self.x>480-50:
           self.direction="left"
       if self.x<0:
           self.direction ="right"
    def sheBullet(self):
        x = random.randint(0, 100)
        if x==8 or x== 50:
         self.bullet_list.append(EnemyBullet(self.screen, self.x, self.y))

def eventType(heroplane):
    for event in pygame.event.get():
        if event.type == QUIT:
            print("exit")
            exit()
        elif event.type == KEYDOWN :
            if event.key ==K_a or event.key == K_LEFT:
                heroplane.moveLeft()
                print("想右移")
            if event.key == K_d or event.key == K_RIGHT:
                heroplane.moveRight()
                print("想左移")
            if event.key == K_SPACE:
                heroplane.sheBullet()
                print("发射子弹")
def main():
    screen = pygame.display.set_mode((480, 852), 0, 32)
    background = pygame.image.load("./background.png")
    heroPlane = MyPlane(screen)
    enemyplane=EnemyPlane(screen)
    while True:
        screen.blit(background, (0, 0))
        heroPlane.display()
        enemyplane.display()
        enemyplane.move()
        enemyplane.sheBullet()
        eventType(heroPlane)
        pygame.display.update()

if __name__=="__main__":
       main()