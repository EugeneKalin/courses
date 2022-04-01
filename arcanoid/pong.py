# Инициализация PyGame
import pygame
pygame.init()

# Назначаем чёрный цвет
BLACK = (0, 0, 0)
# Назначаем зелёный цвет
GREEN = (0, 200, 64)
# Назначаем жёлтый цвет
YELLOW = (225, 225, 0)

# Позиция по Y для блока
posY_block = 150

# Позиция по Y для шарика
posX_circle = 80
# Позиция по X для шарика
posY_circle = 150

# Направление шарика на право
circle_right = True
# Направление шарика вверх
circle_top = True

# Скорость
speed = 3
# Ширина окна игры
screenWidth = 800
# Высота окна игры
screenHeight = 400

# Создаём окно
screen = pygame.display.set_mode((screenWidth, screenHeight))
# Берём компонент часов
clock = pygame.time.Clock()

while True:
    # Назначаем FPS
    clock.tick(60)
    # Красим экран в чёрный цвет
    screen.fill(BLACK)

    # Отслеживаем зажатие клавиш
    pressed_keys = pygame.key.get_pressed()
    # Если зажата стрелка верх
    if pressed_keys[pygame.K_UP]:
        # Проверяем позицию блока по Y больше нуля
        if posY_block > 0:  # То
            # Вычитаем из позиции скорость
            posY_block -= speed
    # Если нажата стрелка вниз то
    if pressed_keys[pygame.K_DOWN]:
        # Проверяем позиция по Y плюс 100 больше высоты окна
        if posY_block + 100 < screenHeight:  # То
            # Увеличиваем позицию Y на скорость
            posY_block += speed
    # Проверяем что наш шарик достиг левого края окна
    if posX_circle - 50 <= 0:
        # Меняем направление на право
        circle_right = True

    # Проверяем что шарик достиг верхнего края
    if posY_circle - 50 <= 0:
        # Меняем направление вниз
        circle_top = False
    # Если шарик достиг нижнего края
    elif posY_circle + 50 >= screenHeight:
        # Меняем направление вверх
        circle_top = True

    # Проверяем направление на право
    if circle_right:
        # Увеличиваем позицию X на скорость
        posX_circle += speed
    else:  # Иначе
        # Уменьшаем позицию X на скорость
        posX_circle -= speed

    # Проверяем направление на верх
    if circle_top:
        # Уменьшаем позицию Y на скорость
        posY_circle -= speed
    else:  # Иначе
        # Увеличиваем позицию Y на скорость
        posY_circle += speed
    # Проверка того, что шарик столкнулся с блоком
    if posY_block <= posY_circle <= posY_block + 100 and screenWidth - 20 <= posX_circle + 50 <= screenWidth:
        # Меняем направление
        circle_right = False
    # Если шарик прошёл за правый край, то
    elif posX_circle + 50 > screenWidth:
        # Выходим из программу
        pygame.quit()
        sys.exit()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Рисуем блок
    pygame.draw.rect(screen, GREEN, (780, posY_block, 20, 100))
    # Рисуем шарик
    pygame.draw.circle(screen, YELLOW, (posX_circle, posY_circle), 20)
    # Обновляем экран
    pygame.display.update()