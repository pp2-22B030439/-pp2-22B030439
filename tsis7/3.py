import pygame

# Initialize Pygame
pygame.init()

# Set the dimensions of the screen
screen_width, screen_height = 640, 480
screen = pygame.display.set_mode((screen_width, screen_height))

# Set the initial position of the ball
ball_x, ball_y = screen_width // 2, screen_height // 2

# Set the radius of the ball
ball_radius = 25

# Set the color of the ball and the background
ball_color = (255, 0, 0)
background_color = (255, 255, 255)

# Define a function to draw the ball on the screen
def draw_ball(x, y):
    pygame.draw.circle(screen, ball_color, (x, y), ball_radius)

# Game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            # Move the ball when arrow keys are pressed
            if event.key == pygame.K_UP:
                ball_y -= 20
            elif event.key == pygame.K_DOWN:
                ball_y += 20
            elif event.key == pygame.K_LEFT:
                ball_x -= 20
            elif event.key == pygame.K_RIGHT:
                ball_x += 20
    
    # Keep the ball within the screen
    ball_x = max(ball_radius, min(ball_x, screen_width - ball_radius))
    ball_y = max(ball_radius, min(ball_y, screen_height - ball_radius))
    
    # Draw the background and the ball on the screen
    screen.fill(background_color)
    draw_ball(ball_x, ball_y)
    pygame.display.flip()
