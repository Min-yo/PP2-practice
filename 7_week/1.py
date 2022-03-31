import pygame
from datetime import datetime

time_sec = (datetime.now()).strftime('%S')
time_sec = int(time_sec)
angle_sec = (-6)*time_sec+1

time_min = (datetime.now()).strftime('%M')
time_min = int(time_min)
angle_min = (-6)*time_min+1

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((480, 480))

image = pygame.image.load(r'pics\mickeyclock2.jpg')
image_sec = pygame.image.load(r'pics\hand_sec.png')
image_min = pygame.image.load(r'pics\hand_min.png')
done = False
dx = dy = 240
screen.fill((255, 255, 255))             
screen.blit(image, (0, 0))

sec_copy = pygame.transform.rotate(image_sec, angle_sec)
screen.blit(sec_copy, (dx - int(sec_copy.get_width() / 2), dy - int(sec_copy.get_height() / 2)))

min_copy = pygame.transform.rotate(image_min, angle_min)
screen.blit(min_copy, (dx - int(min_copy.get_width() / 2), dy - int(min_copy.get_height() / 2)))



while True:
    angle_sec -= 6
    angle_min -= 0.1
    
    screen.fill((255, 255, 255))             
    screen.blit(image, (0, 0))  
 
    sec_copy = pygame.transform.rotate(image_sec, angle_sec)
    screen.blit(sec_copy, (dx - int(sec_copy.get_width() / 2), dy - int(sec_copy.get_height() / 2)))

    min_copy = pygame.transform.rotate(image_min, angle_min)
    screen.blit(min_copy, (dx - int(min_copy.get_width() / 2), dy - int(min_copy.get_height() / 2)))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
                
    pygame.display.flip()
    clock.tick(1)