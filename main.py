import pygame
import random

#Initialize PyGame
pygame.init()

#Game Constants
WIDTH,HEIGHT=800,600

#Creating window
screen=pygame.display.set_mode((WIDTH,HEIGHT))

#Title of window
pygame.display.set_caption("Fruit Ninja")

#Load Image
bg=pygame.image.load('assets/background.png')

fruit_images={
    'fruit1':pygame.image.load('assets/fruit1.png'),#Apple
    'fruit2':pygame.image.load('assets/fruit2.png'),#Pineapple
    'fruit3':pygame.image.load('assets/fruit3.png')#Watermelon
}

bomb_image=pygame.image.load('assets/bomb.png')

#Transform 
fruit_sizes={'fruit1':50,'fruit2':100,'fruit3':90}

for fruit in fruit_images:
    fruit_images[fruit]=pygame.transform.scale(fruit_images[fruit],(fruit_sizes[fruit],fruit_sizes[fruit]))

bomb_image=pygame.transform.scale(bomb_image,(60,60))

class GameObject:
    def __init__(self,fruit_type,is_bomb):
        self.x=400
        self.y=300
        self.fruit_type=fruit_type
        self.is_bomb=is_bomb

    #Drawing the object on screen
    def draw(self):    
        if self.is_bomb:
            screen.blit(bomb_image,(self.x,self.y))
        else:
            screen.blit(fruit_images[self.fruit_type],(self.x,self.y))


running=True

while running:

    screen.blit(bg,(0,0))
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False

    fruit_type = random.choice(["fruit1", "fruit2", "fruit3"])  
    is_bomb=random.randint(0,1)==1

    obj=GameObject(fruit_type,is_bomb)

    obj.draw()

    pygame.display.update()

pygame.quit()




