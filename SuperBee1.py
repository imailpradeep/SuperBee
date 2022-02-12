import pygame,sys, random, time

pygame.init()


x = 800
y = 350
clock = pygame.time.Clock()

#colors
GREEN=(0,250,0)
RED=(250,0,0)
LIGHT_BLUE=(100,100,250)
WHITE = (255,255,255)
BLACK = (0,0,0)
SCREEN_LENGTH = 700
SCREEN_HEIGHT = 500
i = 0
SPEED = 0

screen=pygame.display.set_mode((SCREEN_LENGTH,SCREEN_HEIGHT))
pygame.display.set_caption('SUPER BEE')


bee = pygame.image.load("bee.png")
bee = pygame.transform.scale(bee, (70, 70))
pygame.display.set_icon(bee)

# load background images -----------------------------------------------#
background0 = pygame.image.load('background1-min.png')
#flower1 = pygame.image.load('flower1.jpg')
#flower2 = pygame.image.load('flower2.jpg')

bg_x1 = 0
bg_x2 = 800#background0.get_width()
#bg_x3 = 1600#2*background0.get_width()

#creating class(Blueprint of objects)----------------------------------------------#
class MovingBall():
        
        def __init__(self,ballsize,ballcolor,x,y,x_vel,y_vel):
                self.ballsize= ballsize
                self.ballcolor= ballcolor
                self.x=x
                self.y=y
                self.x_vel=x_vel#velocity(X-axis)
                self.y_vel=y_vel#velocity(Y-axis)

        def draw(self,x,y):
                self.ballsize -= 1
                pygame.draw.circle(screen,self.ballcolor,(self.x,self.y),self.ballsize)

        def velocity(self,x_vel,y_vel):
                self.x+=self.x_vel
                self.y+=self.y_vel
                
                if(self.x>SCREEN_LENGTH):
                        self.x_vel *= -1
                if(self.y>SCREEN_HEIGHT):
                        self.y_vel *= -1
                if(self.x<0):
                        self.x_vel *= -1
                if(self.y<0):
                        self.y_vel *= -1


class Obstacle_Rects():
        def __init__(self,x,y,rect_length, rect_height, x_vel,y_vel):
                #self.rectcolor= rectcolor
                self.x=x
                self.y=y
                self.rect_length = rect_length
                self.rect_height = rect_height
                self.x_vel=x_vel#velocity(X-axis)
                self.y_vel=y_vel#velocity(Y-axis)

        def draw_rect(self,x,y,rect_length, rect_height, x_vel,y_vel):
            self.x -= 1
            pygame.draw.rect(screen,RED,(self.x,self.y,self.rect_length,self.rect_height))
                 
        def move_rect(self,x_vel,y_vel):
            #pygame.draw.rect(screen,RED,(self.x,self.y,self.rect_length,self.rect_height))
            self.x -= self.x_vel
            self.y -= self.y_vel
               
                

def Obstacle_Movement():
    global SCREEN_LENGTH,SCREEN_HEIGHT

    x_vel = 1
    y_vel = 0

    rect_length = random.randint(30,45)
    rect_height = random.randint(30,70)
    x = random.randint(SCREEN_LENGTH+100,SCREEN_LENGTH+200)
    y = random.randint(0,SCREEN_HEIGHT-rect_height)
    
    rect_1 = Obstacle_Rects(x,y,rect_length, rect_height, x_vel,y_vel)
    obstacles.append(rect_1)


    for obstacle in obstacles:
        obstacle.draw_rect(x,y,rect_length,rect_height,x_vel,y_vel)
        obstacle.move_rect(x_vel,y_vel)
        
     
def Bee_Movement():
    # mouse position for balls
    mx, my = pygame.mouse.get_pos()
    #time.sleep(0.1) # If your computer is fast you can enable this and change 0.1 to any value
    ball_1 = MovingBall(10,(random.randint(200,250),random.randint(100,150),random.randint(150,250)), mx,my, -10,random.randint(-7,7))
    balls.append(ball_1)

    for ball in balls:
        ball.draw(mx,my)
        ball.velocity(0,2)
        
    screen.blit(bee, (mx,my-40))


def quit():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

def Redraw_Window():
    global bg_x1, bg_x2
    bg_x1 -= 1
    bg_x2 -= 1
    
    
    screen.blit(background0, (bg_x1, 0))  # draws our first bg image
    screen.blit(background0, (bg_x2, 0))
    if bg_x1 <= -800: #background0.get_width() * -1:  # If our bg is at the -width then reset its position
        bg_x1 = 800#2*background0.get_width()
    if bg_x2 <= -800: #background0.get_width() * -1:  # If our bg is at the -width then reset its position
        bg_x2 = 800 #2*background0.get_width()
        #time.sleep(0.25) # if your computer is fast you can enable this and change 0.25 to any value

    

def Level_1():
    global x,y
    
    x -= 1
    if x>-50: 
        pygame.draw.rect(screen,RED,(x,y,50,50))
    else:
        x = 805
        y = random.randint(0,400)

      
    


#instantiate objects----------------------------------------------------------------#         

balls = []
obstacles = []

#game loop--------------------------------------------------------------------------#
while True:

    quit()
    
    #background color---------------------------------------------------------------#    
    #screen.fill(WHITE)

    
    
    Redraw_Window() # draw moving background
   
    
    Bee_Movement() # make bee move with mouse

    
    Level_1()
    
    i +=1
    print(i%100)
    if i%100 < 0.5:
        #pygame.draw.rect(screen,RED,(805,random.randint(0,400),50,50))
        Obstacle_Movement()
        
    
    #Obstacle_Movement()
               
    clock.tick(300 + SPEED)
    # Update -----------------------------------------------------------------------#
    pygame.display.update()
                        
                        
                
   
            
    
        
