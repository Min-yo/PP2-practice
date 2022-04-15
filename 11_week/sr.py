import random
import sys
import pygame

pygame.init()

FPS = 60
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
STEP = 5

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
SCORE  = 0
numb_coins = 0
collision_1 = False
clock = pygame.time.Clock()
score_font = pygame.font.SysFont("Verdana", 20)
SURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Street Racer")
bg = pygame.image.load(r"pics\AnimatedStreet.png")

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r"pics\Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
        self.step = 10

    def update(self):
        global SCORE
        self.rect.move_ip(0, self.step)
        if(self.rect.bottom > SCREEN_HEIGHT):
            SCORE += 1
            self.top = 0
            self.rect.center = (random.randint(30, 350), 0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r"pics\Coin.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(30, 350), 540)
    
    def draw(self, surface):
        surface.blit(self.image, self.rect)

class Extra_Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.cnt = 0
        self.image = pygame.image.load(r"pics\Coin_1.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(30, 350), 540)
    
    def draw(self, surface):
        global collision_1
        if self.cnt == 5:
            surface.blit(self.image, self.rect)
            if collision_1:
                self.cnt = 0
                self.rect.center = (random.randint(30, 350), 540)
                collision_1 = not collision_1
                


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r"pics\Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def update(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:
            if pressed_keys[pygame.K_LEFT]:
                self.rect.move_ip(-STEP, 0)

        if self.rect.right < SCREEN_WIDTH:
            if pressed_keys[pygame.K_RIGHT]:
                self.rect.move_ip(STEP, 0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def does_collide(self, coin, coin_1):
        global numb_coins
        if self.rect.x < coin.rect.x + coin.rect.width and self.rect.x + self.rect.width > coin.rect.x and self.rect.y < coin.rect.y + coin.rect.height and self.rect.height + self.rect.y > coin.rect.y:
           coin.rect.center = (random.randint(30, 350), 540) 
           numb_coins += 1
           coin_1.cnt += 1
               
    def does_collide_1(self, coin_1):
        global collision_1
        if self.rect.x < coin_1.rect.x + coin_1.rect.width and self.rect.x + self.rect.width > coin_1.rect.x and self.rect.y < coin_1.rect.y + coin_1.rect.height and self.rect.height + self.rect.y > coin_1.rect.y:
            collision_1 = True



P1 = Player()
E1 = Enemy()
coin = Coin()
coin_1 = Extra_Coin()
enemies = pygame.sprite.Group()
enemies.add(E1)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    P1.update()
    E1.update()
    P1.does_collide(coin, coin_1)
    P1.does_collide_1(coin_1)
    if numb_coins == 15:
        E1.step = 12
    elif numb_coins == 30:
        E1.step = 13

    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.quit()
        sys.exit()


    SURF.blit(bg, (0, 0))
    coin.draw(SURF)
    coin_1.draw(SURF)
    E1.draw(SURF)
    P1.draw(SURF)

    #score_img = score_font.render(str(SCORE), True, BLACK)
    numb_coins_img = score_font.render(str(numb_coins), True, BLACK)
    #SURF.blit(score_img, (10, 10))
    SURF.blit(numb_coins_img, (360, 10))


    pygame.display.update()
    clock.tick(FPS)