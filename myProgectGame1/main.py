import pygame


pygame.init()

#задаем размер экрана
screen = pygame.display.set_mode((600,300))
pygame.display.set_caption("My game")
icon = pygame.image.load('images/icon.jpg')
pygame.display.set_icon(icon)

#задаем плоскость с размерами
squere = pygame.Surface((50,50))
#заливаем ее голубым цветом
squere.fill('blue')

myfont = pygame.font.Font('font/Rubik-Italic.ttf', 40)
text_surface = myfont.render('Лева хороший', True,'Red')


running = True
#для работы вечный цикл
while running:

    #выводит прямоугольник в координатах 0,0
    screen.blit(squere,(275,125))

    pygame.draw.circle(screen, 'red', (300,150), 25)
    screen.blit(text_surface, (10, 80))

    # обновление консоли
    pygame.display.update()

    #перебор всех событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()





