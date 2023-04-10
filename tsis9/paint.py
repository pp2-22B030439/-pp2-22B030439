import pygame
import math
pygame.init()

screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Paint")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

brush_size = 10

brush_color = BLACK
drawing_type = "pen"
drawing = False
last_pos = None
canvas = pygame.Surface((screen_width, screen_height))

def calculate_triangle_vertices(center, size, orientation):
    x, y = center
    angle = math.radians(orientation)
    height = size * math.sqrt(3) / 2
    x1 = x + size / 2 * math.cos(angle)
    y1 = y - size / 2 * math.sin(angle)
    x2 = x + size * math.cos(angle + math.pi * 2 / 3)
    y2 = y - size * math.sin(angle + math.pi * 2 / 3)
    x3 = x + size / 2 * math.cos(angle + math.pi * 4 / 3)
    y3 = y - size / 2 * math.sin(angle + math.pi * 4 / 3)
    return ((int(x1), int(y1)), (int(x2), int(y2)), (int(x3), int(y3)))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                drawing = False
            elif event.key == pygame.K_p:
                drawing_type = "pen"
            elif event.key == pygame.K_r:
                drawing_type = "rect"
            elif event.key == pygame.K_c:
                drawing_type = "circle"
            elif event.key == pygame.K_e:
                canvas.fill(BLACK)
            elif event.key == pygame.K_s:
                drawing_type = "square"
            elif event.key == pygame.K_t:
                drawing_type = "triangle"
            elif event.key == pygame.K_g:
                drawing_type = "e-triangle"
            elif event.key == pygame.K_d:
                drawing_type = "rhombus"
            elif event.key == pygame.K_MINUS:
                brush_size = max(1, brush_size - 1)
            elif event.key == pygame.K_PLUS or event.key == pygame.K_EQUALS:
                brush_size += 1
            elif event.key == pygame.K_1:
                brush_color = BLACK
            elif event.key == pygame.K_2:
                brush_color = RED
            elif event.key == pygame.K_3:
                brush_color = GREEN
            elif event.key == pygame.K_4:
                brush_color = BLUE
            elif event.key == pygame.K_5:
                brush_color = YELLOW


        elif event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
            last_pos = pygame.mouse.get_pos()
            if drawing_type == "triangle":
                triangle_top = last_pos
        elif event.type == pygame.MOUSEBUTTONUP:
            if drawing_type == "square":
                current_pos = pygame.mouse.get_pos()
                size = max(abs(current_pos[0] - last_pos[0]), abs(current_pos[1] - last_pos[1]))
                rect = pygame.Rect(last_pos, (size, size))
                pygame.draw.rect(canvas, brush_color, rect, brush_size)
            elif drawing_type == "rhombus":
                if drawing:
                    current_pos = pygame.mouse.get_pos()
                    dx = abs(current_pos[0] - last_pos[0])
                    dy = abs(current_pos[1] - last_pos[1])
                    if dx > dy:
                        diamond_rect = pygame.Rect(last_pos[0], last_pos[1] - dx // 2, dx, dx)
                    else:
                        diamond_rect = pygame.Rect(last_pos[0] - dy // 2, last_pos[1], dy, dy)
                    pygame.draw.polygon(canvas, brush_color, (
                    (diamond_rect.centerx, diamond_rect.top), (diamond_rect.right, diamond_rect.centery),
                    (diamond_rect.centerx, diamond_rect.bottom), (diamond_rect.left, diamond_rect.centery)), brush_size)
            elif drawing_type == "triangle":
                triangle_bottom = pygame.mouse.get_pos()
                pygame.draw.polygon(canvas, brush_color,
                                    [triangle_top, (triangle_bottom[0], triangle_top[1]), triangle_bottom], brush_size)
            elif drawing_type == "e-triangle":
                current_pos = pygame.mouse.get_pos()
                side_length = abs(current_pos[0] - last_pos[0])
                height = int(side_length * (3 ** 0.5) / 2)
                if current_pos[1] < last_pos[1]:
                    height = -height
                pygame.draw.polygon(canvas, brush_color,
                                    [(last_pos[0], last_pos[1]), (last_pos[0] + side_length // 2, last_pos[1] + height),
                                     (last_pos[0] - side_length // 2, last_pos[1] + height)], brush_size)
            elif drawing_type == "rect":
                    current_pos = pygame.mouse.get_pos()
                    pygame.draw.rect(canvas, brush_color, (
                    last_pos[0], last_pos[1], current_pos[0] - last_pos[0], current_pos[1] - last_pos[1]), brush_size)
            elif drawing_type == "circle":
                    current_pos = pygame.mouse.get_pos()
                    radius = max(abs(current_pos[0] - last_pos[0]), abs(current_pos[1] - last_pos[1]))
                    pygame.draw.circle(canvas, brush_color, last_pos, radius, brush_size)
            drawing = False
        elif event.type == pygame.MOUSEMOTION:
            if drawing_type == "pen":
                if drawing:
                    current_pos = pygame.mouse.get_pos()
                    pygame.draw.line(canvas, brush_color, last_pos, current_pos, brush_size)
                    last_pos = current_pos



    screen.blit(canvas, (0, 0))
    pygame.display.flip()
pygame.quit()
