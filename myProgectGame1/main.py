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
    pygame.image.load('images/r/r1.png').convert_alpha(),
    pygame.image.load('images/r/r2.png').convert_alpha(),
    pygame.image.load('images/r/r3.png').convert_alpha(),
    pygame.image.load('images/r/r4.png').convert_alpha(),
    pygame.image.load('images/r/r5.png').convert_alpha(),
    pygame.image.load('images/r/r6.png').convert_alpha(),
    pygame.image.load('images/r/r7.png').convert_alpha(),
    pygame.image.load('images/r/r9.png').convert_alpha(),
]

walk_left = [
    pygame.image.load('images/l/l1.png').convert_alpha(),
    pygame.image.load('images/l/l2.png').convert_alpha(),
    pygame.image.load('images/l/l3.png').convert_alpha(),
    pygame.image.load('images/l/l4.png').convert_alpha(),
    pygame.image.load('images/l/l5.png').convert_alpha(),
    pygame.image.load('images/l/l6.png').convert_alpha(),
    pygame.image.load('images/l/l7.png').convert_alpha(),
    pygame.image.load('images/l/l9.png').convert_alpha(),
]

ghost = pygame.image.load('images/ghost.png').convert_alpha()

ghost_list_in_game = []

player_anim_count = 0
fon_x = 0

player_speed = 5
player_x = 150
player_y = 250

is_jump = False
jump_count = 10


dog_sound = pygame.mixer.Sound('sounds/dog running.mp3')
dog_sound.play()

ghost_timer = pygame.USEREVENT +1
pygame.time.set_timer(ghost_timer, 2500)

label = pygame.font.Font('font/Rubik-Italic.ttf', 40)
lose_label = label.render('Вы проиграли!!!', False, (193, 196, 199))
restart_label = label.render('Играть заново', False, (115, 132, 148))
restar_label_rect = restart_label.get_rect(topleft=(180,280))

gameplay = True


running = True
#для работы вечный цикл
while running:

    screen.blit(fon,(fon_x,0))
    screen.blit(fon, (fon_x + 600, 0))

    if gameplay:
        player_rect = walk_left[0].get_rect(topleft=(player_x, player_y))

        if ghost_list_in_game:
            for (i, el) in enumerate(ghost_list_in_game):
                screen.blit(ghost, el)
                el.x -= 10

                if el.x < -10:
                    ghost_list_in_game.pop(i)

                if player_rect.colliderect(el):
                    gameplay =False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            screen.blit(walk_left[player_anim_count], (player_x, player_y))
        else:
            screen.blit(walk_right[player_anim_count], (player_x, player_y))

        if keys[pygame.K_LEFT] and player_x > 50:
            player_x -= player_speed
        elif keys[pygame.K_RIGHT] and player_x < 200:
            player_x += player_speed

        if not is_jump:
            if keys[pygame.K_SPACE]:
                is_jump =True
        else:
            if jump_count >= -10:
                if jump_count > 0:
                    player_y -= (jump_count ** 2) / 2
                else:
                    player_y += (jump_count ** 2) / 2
                jump_count -= 1
            else:
                is_jump = False
                jump_count = 10

        if player_anim_count == 7:
            player_anim_count =0
        else:
            player_anim_count += 1

        fon_x -= 2
        if fon_x == - 600:
            fon_x = 0
    else:
        dog_sound.stop()
        screen.fill((87, 88, 89))
        screen.blit(lose_label, (180, 100))
        screen.blit(restart_label, restar_label_rect)


        mouse = pygame.mouse.get_pos()
        if restar_label_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            dog_sound.play()
            gameplay =True
            player_x = 150
            ghost_list_in_game.clear()


    # обновление консоли
    pygame.display.update()

    #перебор всех событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        if event.type == ghost_timer:
            ghost_list_in_game.append(ghost.get_rect(topleft=(620,250)))


    clock.tick(10)





