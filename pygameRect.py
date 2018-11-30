import pygame
from pygame.locals import *
import random
# import shelve

"""
Isaac Sutor
Rocket Evasion Game!
"""


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        # create surface
        self.image = pygame.image.load('jet.png').convert()
        # color surface
        self.image.set_colorkey((255, 255, 255), pygame.RLEACCEL)
        self.rect = self.image.get_rect()

    def update(self, pressed_keys):
        if pressed_keys[pygame.K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[pygame.K_DOWN]:
            self.rect.move_ip(0, 5)
        if pressed_keys[pygame.K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[pygame.K_RIGHT]:
            self.rect.move_ip(5, 0)

        # keep player on screen
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > 800:
            self.rect.left = 800
        if self.rect.top <= 0:
            self.rect.top = 0
        elif self.rect.bottom >= 600:
            self.rect.bottom = 600


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.image = pygame.image.load('missile.png').convert()
        self.image.set_colorkey((255, 255, 255), pygame.RLEACCEL)
        self.rect = self.image.get_rect(center=(random.randint(820, 900), random.randint(0, 600)))
        self.speed = random.randint(5, 20)

    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()


class Cloud(pygame.sprite.Sprite):
    def __init__(self):
        super(Cloud, self).__init__()
        self.image = pygame.image.load('cloud.png').convert()
        self.image.set_colorkey((0, 0, 0), pygame.RLEACCEL)
        self.rect = self.image.get_rect(center=(random.randint(820, 900), random.randint(0, 600)))

    def update(self):
        self.rect.move_ip(-5, 0)
        if self.rect.right < 0:
            self.kill()


# initialize
pygame.init()

# create screen
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Missile Dodge")

ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 250)

ADDCLOUD = pygame.USEREVENT + 2
pygame.time.set_timer(ADDCLOUD, 1000)

player = Player()

myfont = pygame.font.SysFont("monospace", 16)
background = pygame.Surface((screen.get_size()))
background.fill((135, 206, 250))
endfont = pygame.font.Font(None, 36)

enemies = pygame.sprite.Group()
clouds = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

score = 0
stopscore = False

# d = shelve.open('hscore.txt')

# Variable to keep main loop running
running = True

# Main Loop
while running:
    # for loop through the event queue
    for event in pygame.event.get():
        # check KEYDOWN event;
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
        # check for QUIT
        elif event.type == pygame.QUIT:
            running = False
        elif event.type == ADDENEMY:
            new_enemy = Enemy()
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)
        elif event.type == ADDCLOUD:
            new_cloud = Cloud()
            all_sprites.add(new_cloud)
            clouds.add(new_cloud)

    screen.blit(background, (0, 0))
    scoretext = myfont.render("Score {0}".format(score), 1, (0, 0, 0))
    screen.blit(scoretext, (5, 10))
    if not stopscore:
        score += 1
    pressed_keys = pygame.key.get_pressed()
    player.update(pressed_keys)
    enemies.update()
    clouds.update()
    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)

    if pygame.sprite.spritecollideany(player, enemies):
        player.kill()
        stopscore = True
        # If game over is true, draw game over
        text = endfont.render("Game Over", True, [0, 0, 0], None)
        text_rect = text.get_rect()
        text_x = screen.get_width() / 2 - text_rect.width / 2
        text_y = screen.get_height() / 2 - text_rect.height / 2

    if stopscore:
        screen.blit(text, [text_x, text_y])
        # highscore = d['key']
        # if score > highscore:
            # d['key'] = score  # thats all, now it is saved on disk.
            # d.close()
            # print(score)
    pygame.display.flip()




