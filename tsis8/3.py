import pygame

# инициализация Pygame
pygame.init()

# установка размеров экрана
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))

# установка заголовка окна
pygame.display.set_caption("Рисование")

# установка цветовой палитры
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# установка размера кисти
brush_size = 10

# установка начального цвета
brush_color = BLACK
drawing_type = "pen"
# создание поверхности для рисования
drawing = False
last_pos = None
canvas = pygame.Surface((screen_width, screen_height))

# основной цикл программы
running = True
while running:
    # обработка событий клавиатуры
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                # выход из режима рисования
                drawing = False
            elif event.key == pygame.K_p:
                # выбор ручки
                drawing_type = "pen"
            elif event.key == pygame.K_r:
                # выбор рисования прямоугольника
                drawing_type = "rect"
            elif event.key == pygame.K_c:
                # выбор рисования круга
                drawing_type = "circle"
            elif event.key == pygame.K_e:
                # стирание холста
                canvas.fill(BLACK)
            elif event.key == pygame.K_s:
                # сохранение изображения
                pygame.image.save(canvas, "drawing.png")
            elif event.key == pygame.K_MINUS:
                # уменьшение размера кисти
                brush_size = max(1, brush_size - 1)
            elif event.key == pygame.K_PLUS or event.key == pygame.K_EQUALS:
                # увеличение размера кисти
                brush_size += 1
            elif event.key == pygame.K_1:
                # выбор цвета черный
                brush_color = BLACK
            elif event.key == pygame.K_2:
                # выбор цвета красный
                brush_color = RED
            elif event.key == pygame.K_3:
                # выбор цвета зеленый
                brush_color = GREEN
            elif event.key == pygame.K_4:
                # выбор цвета синий
                brush_color = BLUE
            elif event.key == pygame.K_5:
                # выбор цвета желтый
                brush_color = YELLOW


        elif event.type == pygame.MOUSEBUTTONDOWN:
            # начало рисования
            drawing = True
            last_pos = pygame.mouse.get_pos()
        elif event.type == pygame.MOUSEBUTTONUP:
            # конец рисования
            drawing = False
        elif event.type == pygame.MOUSEMOTION:
            # рисование
            # рисование фигуры
            if drawing_type == "pen":
                # рисование кистью
                if drawing:
                    current_pos = pygame.mouse.get_pos()
                    pygame.draw.line(canvas, brush_color, last_pos, current_pos, brush_size)
                    last_pos = current_pos

        elif drawing_type == "rect":
                # рисование прямоугольника
            if drawing:
                current_pos = pygame.mouse.get_pos()
                pygame.draw.rect(canvas,brush_color, (last_pos[0], last_pos[1], current_pos[0] - last_pos[0], current_pos[1] - last_pos[1]))
        elif drawing_type == "circle":
                    # рисование круга
            if drawing:
                current_pos = pygame.mouse.get_pos()
                radius = max(abs(current_pos[0] - last_pos[0]), abs(current_pos[1] - last_pos[1]))
                pygame.draw.circle(canvas, brush_color, last_pos, radius, brush_size)
                                     # отрисовка экрана
    screen.blit(canvas, (0, 0))
    pygame.display.flip()

# завершение Pygame
pygame.quit()
