import sys
import pygame as pg
import time
pg.init()
font_d=pg.font.SysFont("None", 24)
# developing the screen
main = pg.display.set_mode((720, 480))
#coloring it to gray
main.fill((200, 200, 200))
# defining the class
class Ball:
 # X coordinate
    x=0
 # Y coordinate 
    y=0
 # Colour
    colr=(255,0,0)
 # we will consider 1 when Ball coming down,
    direction=1
 # we will consider -1 when Ball going up
 # Time in this direction
    ftime=0
  # local gravity
    droprate=0
    # Initialise the Ball with x coordinate, y coordinate and droprate.
    def __init__(self,x,y,droprate):
        self.x=x
        self.y=y
        self.droprate=droprate
        self.ftime=0
    def setcolour(self,newcolr):
        self.colr=newcolr
    # drawing a circle to represent the ball
    def draw(self):
        pg.draw.circle(main,self.colr,(self.x,self.y),10,0)
    # defining a function for fall
    def fall(self):
        pg.draw.circle(main,(200,200,200),(self.x,self.y),10,0)
        if self.direction==1:
            if (self.y<=460): #checking the falling criterion
                self.y=int(self.y+(self.droprate*(self.ftime*self.ftime)))
                self.ftime+=1
            else: 
                self.direction=-1
                self.ftime-=1
        else:
            if(self.y>=30):
                self.y=int(self.y-(self.droprate*(self.ftime*self.ftime)))
                self.ftime-=1
            else:
                self.direction=-1
            if (self.ftime==0):
                self.ftime=1
                self.direction=1
def drawBalls(alist):
    for ball in alist:
        ball.draw()

def fallBalls(alist):
    for ball in alist:
        ball.fall()

class Display:
    slowspeed = 0 #Animation delay
    def __init__(self):
        self.slowspeed=0 # Initially set to zero.
    def setslow(self,setspeed):
        self.slowspeed=setspeed
    def display(self):
        pg.draw.rect(main, (0,0,0), ((0,0),(720,20)),0)
        text=font_d.render("Current delay "+str(self.slowspeed), True,(127,0,255))
        main.blit(text,(300,5))
def Main():
    slowdown=0
    display = Display()
    display.setslow(slowdown)
    display.display()

    balllist=[]

    balllist.append(Ball(150,100,1))
    balllist.append(Ball(250,100,2))
    balllist.append(Ball(350,100,4))
    balllist.append(Ball(450,100,2))
    balllist.append(Ball(550,100,1))

    balllist[1].setcolour((0,0,254))
    balllist[2].setcolour((0,255,255))
    balllist[3].setcolour((102,0,204))
    balllist[4].setcolour((255,51,225))

    drawBalls(balllist)
    pg.display.update()

    while (True):
        # Get all of the balls to fall
        fallBalls(balllist)
        drawBalls(balllist)
        pg.draw.rect(main, (0,0,0), ((0,20),(720,460)),16)
        display.display()
        pg.display.update()
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_UP:
                    slowdown+=10
                    display.setslow(slowdown)
                elif event.key == pg.K_DOWN:
                    if (slowdown>0):
                        slowdown-=10
                        display.setslow(slowdown)
                if event.key == pg.K_ESCAPE:
                    print("EXITING")
                    time.sleep(0.05)
                    pg.quit(); sys.exit()
                    pg.time.delay(slowdown)
            if event.type == pg.QUIT:
                pg.quit(); sys.exit()
                pg.time.delay(slowdown)
if __name__ == '__main__':
    pg.display.set_caption("Bouncing Balls")
    pg.draw.rect(main, (0,0,0), ((0,0),(720,20)),0)
    pg.draw.rect(main, (0,0,0), ((0,20),(720,460)), 16)
    Main()
            