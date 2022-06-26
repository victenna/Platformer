import pygame
pygame.init()
clock=pygame.time.Clock()
X,Y,acc=900,900,2
screen= pygame.display.set_mode((X,Y))
pygame.display.set_caption("First Game")
mario= pygame.image.load('player0.png')
mario=pygame.transform.scale(mario,(50,90))
mario_rect = mario.get_rect(midbottom=(X//2,Y-100))

jump,left,right,down = False,False,False,False
y_speed=0
Q=11
platform,p_rects=[0]*Q,[0]*Q
x,y=[X],[100]
for i in range(Q-1):
    x.append(50); y.append(20)
                
posx=[X//2,100,180,350,700,80,720,550,550,830,320]
posy=[Y,680,480,200,450,270,250,650,350,750,400]
color=['dark green','blue','red','purple','dark grey',\
       'black','brown','cyan','orange','navy','pink']

for i in range(Q):
    platform[i]=pygame.surface.Surface((x[i],y[i]))
    platform[i].fill(color[i])
    p_rects[i]=platform[i].get_rect(midbottom=(posx[i],posy[i]))

def move():
    global X,Y,y_speed,jump
    if jump: y_speed = -30
    mario_rect.bottom += y_speed

    if left and mario_rect.left > 0:
        mario_rect.centerx -= 5
    if right and mario_rect.right < X:
        mario_rect.centerx += 5

    if on_ground():
        global k,collision
        if y_speed >= 0:
            mario_rect.bottom = p_rects[mario_rect.collidelist(p_rects)].top + 1
            y_speed = 0
        else:
            mario_rect.top = p_rects[mario_rect.collidelist(p_rects)].bottom
            y_speed = 2
    else:
        y_speed += acc
    
def on_ground():
    collision=mario_rect.collidelist(p_rects)
    if collision>-1:
        for i in range(Q):
            if collision!=0 and abs(mario_rect.bottom-p_rects[i].top)<2:
                k[collision]=1
                platform[i].fill('white')
        return True
    else:
        return False
k=[0]*Q
Sum=0
count=True
T=40

time_delay = 1000
timer_event = pygame.USEREVENT+1
pygame.time.set_timer(timer_event, time_delay)
delta=1
counter,counter1 = 0,0
font = pygame.font.SysFont(None, 50)
text0 = font.render('Time=', True, (0, 128, 0))
text = font.render(str(counter), True, (0, 128, 0))
text1 = font.render('Score=', True, (0, 128, 0))

while True:
    jump,left,right = False,False,False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                jump=True
        if event.type==timer_event:
            counter= counter+delta
            text = font.render(str(counter), True, (0, 128, 0))
            if counter==T and count==True:
                count=False
                delta=0
                for i in range (Q):
                    Sum=Sum+k[i]
                print('Sum=',Sum)
                text2 = font.render(str(Sum), True, (0, 128, 0))
      
    keys=pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        left=True
    if keys[pygame.K_RIGHT]:
        right=True
    move()     
    screen.fill('gold')

    for i in range(Q):
        screen.blit(platform[i],p_rects[i])
    screen.blit(mario,mario_rect)

    screen.blit(text0, (600,50))
    screen.blit(text, (700,50))
    if counter==T:
        screen.blit(text1,(100,50))
        screen.blit(text2,(220,50))
        
    if counter==T:
        counter1=counter1+1
        if counter1==2*T:
            #quit()
            break
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            
    clock.tick(50)   
    pygame.display.update() 