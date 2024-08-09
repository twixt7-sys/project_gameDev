import pygame
pygame.init()

#window
screen_size = [500, 500]
win = pygame.display.set_mode(screen_size) #a touple
pygame.display.set_caption("Hello GameWorld")

#Main Sprite
sprite_pos = [50, 50]
sprite_size = [10, 10]

frame_rate = 5
vel = 2

run = True

while run:
    pygame.time.delay(frame_rate)

    #Quit Function
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    #Key Functions
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and sprite_pos[0] > 0:
        sprite_pos[0] -= vel
    if keys[pygame.K_RIGHT] and sprite_pos[0] < screen_size[0] - sprite_size[0]:
        sprite_pos[0] += vel
    if keys[pygame.K_UP] and sprite_pos[1] > 0:
        sprite_pos[1] -= vel
    if keys[pygame.K_DOWN] and sprite_pos[1] < screen_size[1] - sprite_size[1]:
        sprite_pos[1] += vel

    win.fill((0, 0, 0))             #refresh background

#                   surface   color
    pygame.draw.rect(win, (255, 0, 0), (sprite_pos[0], sprite_pos[1], sprite_size[0], sprite_size[1]))
    pygame.display.update()
pygame.quit()