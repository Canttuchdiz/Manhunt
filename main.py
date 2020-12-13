import pygame, sys, random, time

# Functions

pygame.init()
width, height = 1000,1000
screen = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()

# Icon
pygame.display.set_caption("Manhunt")
icon = pygame.image.load('assets/costume1.png')
pygame.display.set_icon(icon)

# Variables
BLACK = (0, 0, 0)
x = 0
y = 0
#frames_index = []
#frames = frames_index
#frames_index.append()
guyAn_1 = pygame.image.load('assets/sord2.png').convert()
guyAn_1_rect = guyAn_1.get_rect()
copAn_3 = pygame.image.load('assets/npc.png').convert()
copAn_1_rect = copAn_3.get_rect()
guyAn_2 = pygame.image.load('assets/run2.png').convert()
guyAn_2_rect = guyAn_2.get_rect()
copAn_2 = pygame.image.load('assets/sp2.png').convert()
copAn_2_rect = copAn_2.get_rect()
guyAn_1f1 = pygame.image.load('assets/sord2.png').convert()
guyAn_1f2 = pygame.image.load('assets/run2.png').convert()
guy_frames = [guyAn_1_rect,guyAn_2_rect]
guy_index = 0
guy_index = guy_frames

# Map
map = pygame.image.load('assets/Mapdoop.png',).convert()
map = pygame.transform.scale(map, (1000, 1000))


x_then, y_then = x, y

frame = guyAn_1

time_then = time.time()
OK = True

animation_FPS = 0.2

frames = [guyAn_1, guyAn_2]
frames_index = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((0, 0, 0))
    screen.blit(map,(0,0))
    # Movement

    key = pygame.key.get_pressed()
    # moving the sprite left
    if key[pygame.K_LEFT]:
        x -= 5
    # moving the sprite right
    if key[pygame.K_RIGHT]:
        x += 5
    # moving the sprite down
    if key[pygame.K_DOWN]:
        y += 5
    # moving the sprite up
    if key[pygame.K_UP]:
        y -= 5

    time_now = time.time()

    if x_then != x or y_then != y:
        if OK:
            OK = False
            time_then = time_now
            frames_index += 1
            if frames_index > 1:
                frames_index = 0
        if time_now - time_then > animation_FPS:
            time_then = time_now
            frames_index += 1
            if frames_index > 1:
                frames_index = 0
    else:
        OK = True

    if x > 930:
        x = 930
    if x < 0:
        x = 0
    if y > 900:
        y = 900
    if y < 0:
        y = 0

    screen.blit(frames[frames_index], (x, y))

    guyAn_1.set_colorkey(BLACK)
    copAn_3.set_colorkey(BLACK)
    guyAn_2.set_colorkey(BLACK)
    copAn_2.set_colorkey(BLACK)

    x_then, y_then = x, y


    pygame.display.flip()
    clock.tick(60)