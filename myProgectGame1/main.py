import pygame

clock = pygame.time.Clock()
pygame.init()

#задаем размер экрана
screen = pygame.display.set_mode((600,400))
pygame.display.set_caption("My game")
icon = pygame.image.load('images/icon.jpg')
pygame.display.set_icon(icon)

fon = pygame.image.load('images/fon.jpg')

walk_right = [
    pygame.image.load('images/r/r1.png'),
    pygame.image.load('images/r/r2.png'),
    pygame.image.load('images/r/r3.png'),
    pygame.image.load('images/r/r4.png'),
    pygame.image.load('images/r/r5.png'),
    pygame.image.load('images/r/r6.png'),
    pygame.image.load('images/r/r7.png'),
   # pygame.image.load('images/r/r8.png'),
    pygame.image.load('images/r/r9.png'),
]

walk_left = [
    pygame.image.load('images/l/l1.png'),
    pygame.image.load('images/l/l2.png'),
    pygame.image.load('images/l/l3.png'),
    pygame.image.load('images/l/l4.png'),
    pygame.image.load('images/l/l5.png'),
    pygame.image.load('images/l/l6.png'),
    pygame.image.load('images/l/l7.png'),
  #  pygame.image.load('images/l/l8.png'),
    pygame.image.load('images/l/l9.png'),
]

player_anim_count = 0
fon_x = 0

dog_sound = pygame.mixer.Sound('sounds/dog running.mp3')
dog_sound.play()

running = True
#для работы вечный цикл
while running:

    screen.blit(fon,(fon_x,0))
    screen.blit(fon, (fon_x + 600, 0))
    screen.blit(walk_right[player_anim_count], (100, 300))

    if player_anim_count == 7:
        player_anim_count =0
    else:
        player_anim_count += 1

    fon_x -= 2
    if fon_x == - 600:
        fon_x = 0



    # обновление консоли
    pygame.display.update()

    #перебор всех событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

    clock.tick(10)





