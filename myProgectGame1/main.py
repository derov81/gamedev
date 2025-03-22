import pygame


pygame.init()

#задаем размер экрана
screen = pygame.display.set_mode((600,300))
pygame.display.set_caption("My game")
icon = pygame.image.load('images/icon.jpg')
pygame.display.set_icon(icon)

running = True
#для работы вечный цикл
while running:

    #screen.fill((72, 87, 189))

    # обновление консоли
    pygame.display.update()

    #перебор всех событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                screen.fill((235, 232, 56))





