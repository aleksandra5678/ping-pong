from pygame import *
from random import randint

#создай окно игры
window = display.set_mode((700,600))
display.set_caption('стрелялки')
fon = transform.scale(image.load('pole.jpg'),(700,600))
font.init()
font = font.Font(None,37)


class Games(sprite.Sprite):
    def __init__(self, im, sp_x, sp_y, size_x, size_y, speeed):
        super(). __init__()
        self.image = transform.scale(image.load(im),(size_x, size_y))
        self.speed = speeed
        self.rect = self.image.get_rect()
        self.rect.x = sp_x
        self.rect.y = sp_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player1(Games):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5 :
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.x < 590:
            self.rect.y += self.speed 

class Player2(Games):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5 :
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.x < 590:
            self.rect.y += self.speed 

        
finish = False
speed_x = 3
speed_y = 3

sp1 = Player1('roketka.jpg', 30, 250, 80, 100, 3)
sp2 = Player2('roketka.jpg', 587, 250, 80, 100, 3)
sp3 = Games('tennis_ball.png', 300, 300, 50, 40, 3)

text1 = font.render('PLAYER1 LOSE', True,(255,255,255))
text2 = font.render('PLAYER2 LOSE', True,(255,255,255))




game = True
while game:
    k = key.get_pressed()
    for e in event.get():
        if e.type == QUIT:
            game = False


    if finish != True:
        
        window.blit(fon,(0,0))

        sp1.update_r()
        sp2.update_l()
        

        sp1.reset()
        sp2.reset()
        sp3.reset()

        sp3.rect.x += speed_x 
        sp3.rect.y += speed_y

        

        if sprite.collide_rect(sp1, sp3) or sprite.collide_rect(sp2, sp3):
            speed_x *= -1 
        
        if sp3.rect.y > 600 or sp3.rect.y < 0:
            speed_y *= -1
        
        if sp3.rect.x > 650:
            window.blit(text1,(300,300)) 
            finish = True
          
        if sp3.rect.x < 0:            
            window.blit(text2,(300,300))
            finish = True
            







    display.update()