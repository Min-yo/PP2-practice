import pygame

pygame.init()
screen = pygame.display.set_mode((600, 450))
done = False
x = 50
y = 50
step = 20
clock = pygame.time.Clock()
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN and y+25+step <= 450: y += step
        if event.type == pygame.KEYDOWN and event.key == pygame.K_UP and y-25-step > 0: y -= step
        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT and x-25-step > 0: x -= step
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT and x+25+step <= 600: x += step

    screen.fill((255, 255, 255))             
    pygame.draw.circle(screen, (200, 0, 0), (x, y), 25)
    pygame.display.flip()
    clock.tick(60)
