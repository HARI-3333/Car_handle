import pygame
import random
import time
pygame.init()
t=pygame.time.Clock()
#Game display 
bg=pygame.display.set_mode((1400,800))
red=(255,0,0)
green=(0,150,0)
blue=(0,0,255)
black=(0,0,0)
white=(255,255,255)
bb=(120,120,120)
photo=pygame.image.load("image/403132.jpg")
car_image=pygame.image.load("image/white car.2.png")
car_image=pygame.transform.scale(car_image,(50,100))
come=pygame.image.load("image/000.2.jpg")
come=pygame.transform.scale(come,(180,800))
ston=pygame.image.load("image/000.5.png")
ston=pygame.transform.scale(ston,(250,800))
enmy_cars=pygame.image.load("image/red car.2.png")
enmy_cars=pygame.transform.scale(enmy_cars,(50,100))

def message(size,mess,xpos,ypos):
  font=pygame.font.SysFont(None,size)
  render=font.render(mess,True,black)
  bg.blit(render,(xpos,ypos))
  
message(100,"Let's Go HERO",150,100)
t.tick(1)



def car(x,y):
  bg.blit(car_image,(x,y))
  bg.blit(come,(0,0))
  bg.blit(ston,(1170,0))
  if 0<x<160 or 1170<x+10:
    message(100,"Game Over",400,400)
    pygame.display.update()
    t.tick(0.17)
    play()

def enmy_car(xpos,ypos):
  bg.blit(enmy_cars,(xpos,ypos))
  pygame.display.update()

def button(x_button,y_button,messb):
  pygame.draw.rect(bg,white,[x_button,y_button,490,70])
  message(100,messb,x_button,y_button)
  mouse=pygame.mouse.get_pos()
  click=pygame.mouse.get_pressed()
  print(mouse)
  print(click)
  if x_button<mouse[False]<x_button+490 and y_button<mouse[True]<y_button+70:
    pygame.draw.rect(bg,bb,[x_button,y_button,490,70])
    message(100,messb,x_button,y_button)
    if click==(1,0,0) and messb=="Let's Go HERO":
      cr()
    elif click==(1,0,0) and messb=="QUIT":
      
      pygame.quit()
      quit()
      
def car_crash(x,xpos,y,ypos):
   if xpos<x+50<xpos+50 and ypos<y<ypos+50 or xpos<x+50<xpos+100 and ypos<y<ypos+50:
      message(100,"BOOM",200,200)
      pygame.display.update()
      time.sleep(1)
      play()
      for a in pygame.event.get():
         if a.type==pygame.QUIT:
            pygame.quit()





def play():
 play=False
 while play==False:
  bg.blit(photo,(0,0))
  button(100,30,"Let's Go HERO")
  button(100,110,"QUIT") 
  for i in pygame.event.get():
      if i.type==pygame.QUIT:
        pygame.quit()
        quit()
  pygame.display.update()
    

def cr():
  x=700
  xpos=random.randrange(180,1150)
  ypos=0
  y=650
  x1=0 

  loop=False
  while loop==False:
   for i in pygame.event.get():
    if i.type==pygame.QUIT:
       loop=True
    if i.type==pygame.KEYDOWN:
      if i.key==pygame.K_LEFT:
        x1=-10
      elif i.key==pygame.K_RIGHT:
        x1=+10  
    if i.type==pygame.KEYUP:
      if i.key==pygame.K_LEFT or i.key==pygame.K_RIGHT:
        x1=0 

 
   bg.fill(bb)
   car(x,y)
   enmy_car(xpos,ypos)
   ypos+=8
   if ypos==800:
     xpos=random.randrange(180,1150)
     ypos=0
   car_crash(x,xpos,y,ypos)  
   x=x+x1
   t.tick(50)
   pygame.display.update()



play()
pygame.quit()
quit()