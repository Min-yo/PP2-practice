import pygame

pygame.init()
screen = pygame.display.set_mode((225, 225))
done = False
clock = pygame.time.Clock()

image = pygame.image.load(r'pics\music_player.jpg')
screen.blit(image, (0, 0))
m = [r'music\1.ogg', r'music\2.ogg', r'music\3.ogg']

pygame.mixer.music.load(m[0])
pygame.mixer.music.play()
pygame.mixer.music.set_volume(0.1)
current = 0
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_UP and not pygame.mixer.music.get_busy(): pygame.mixer.music.unpause()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN and pygame.mixer.music.get_busy(): pygame.mixer.music.pause()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT and current-1 > -1:
            current -= 1
            pygame.mixer.music.load(m[current])
            pygame.mixer.music.play()
            pygame.mixer.music.queue(m[current+1])
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT and current+1 < len(m):
            current += 1
            pygame.mixer.music.load(m[current])
            pygame.mixer.music.play()
            if current != len(m)-1:
                pygame.mixer.music.queue(m[current+1])

    pygame.display.flip()
    clock.tick(60)