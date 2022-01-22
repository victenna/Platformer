import pygame
pygame.init()
screen = pygame.display.set_mode((800,800))
pygame.display.set_caption("Doodle Jump")
clock = pygame.time.Clock()
class Player():
    def __init__(self):
        self.image=pygame.image.load('player.png')
        self.image=pygame.transform.scale(self.image,(50,100))
        self.rect=self.image.get_rect()
        self.rect.centerx=400
        self.rect.centery=650
        self.dx,self.dy=2,0
    def draw(self):
        screen.blit(self.image,self.rect)
    def left_right(self):
        key=pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            self.rect.x -=self.dx
        if key[pygame.K_RIGHT]:
            self.rect.x +=self.dx

    def update(self):
        self.left_right() 
        self.rect.y += self.dy 
        self.dy += 0.55 
        for block in plates:
            if self.rect.colliderect(block.rect):
                if self.dy > 0:
                    self.rect.bottom = block.rect.top
                elif self.dy < 0: 
                    self.rect.top = block.rect.bottom
                self.dy = 0 
class Platform():
    def __init__(self,posx,posy,clr, w):
        self.posx=posx
        self.posy=posy
        self.clr=clr
        self.surf = pygame.surface.Surface((w,10))
        self.surf.fill((self.clr))
        self.rect = self.surf.get_rect(center = (self.posx,self.posy))
    def draw_plate(self):
        screen.blit(self.surf,self.rect)
mario=Player()
Q=8
plates=[0]*Q
color=['red','blue','brown','green','gold','black','violet','purple','orange']
pos_x,pos_y=[400,100,200,300,400,500,600,700],[700,200,300,400,600,400,300,200]
width=[900,100,100,100,100,100,100,100]
for i in range(Q):
    plates[i]=Platform(pos_x[i],pos_y[i],color[i],width[i])
while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:  
            if event.key == pygame.K_SPACE and 2>mario.dy>0:
                mario.dy = -15
    screen.fill((255, 0, 255))
    mario.draw()
    for p in plates:
        p.draw_plate()
    mario.update()
    pygame.display.update()

