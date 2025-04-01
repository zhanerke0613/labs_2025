import pygame
import sys


pygame.init()


screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Движение красного мяча")


x = screen_width // 2
y = screen_height // 2
radius = 25      
speed = 20        

clock = pygame.time.Clock()

while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                
                if y - radius - speed >= 0:
                    y -= speed
            elif event.key == pygame.K_DOWN:
                #нижняя граница
                if y + radius + speed <= screen_height:
                    y += speed
            elif event.key == pygame.K_LEFT:
                #левая граница
                if x - radius - speed >= 0:
                    x -= speed
            elif event.key == pygame.K_RIGHT:
                #правая граница
                if x + radius + speed <= screen_width:
                    x += speed

   
    screen.fill((255, 255, 255))
    
    
    pygame.draw.circle(screen, (255, 0, 0), (x, y), radius)
    
    
    pygame.display.flip()
    
    
    clock.tick(60)