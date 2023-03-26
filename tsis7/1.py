import pygame
import math
import time

# Initialize Pygame
pygame.init()

# Set the size of the window
window_size = (829, 840)
screen = pygame.display.set_mode(window_size)

# Load the images
mickey_image = pygame.image.load("mickeyclock.jpeg")
minute_hand_image = pygame.image.load("right.png")
minute_hand_image = pygame.transform.scale(minute_hand_image, (200, 183))
second_hand_image = pygame.image.load("left.png")
second_hand_image = pygame.transform.scale(second_hand_image, (200, 183))

# Define the center of the clock
clock_center = (418, 421)

# Define the length of the hands
minute_hand_length = 320
second_hand_length = 300

# Run the clock
while True:
    # Get the current time
    current_time = time.localtime()
    current_minute = current_time.tm_min
    current_second = current_time.tm_sec

    # Draw the clock face
    screen.blit(mickey_image, (0, 0))

    minute_angle = math.radians(current_minute * 6 - 90)
    minute_hand_x = clock_center[0] + (minute_hand_length / 2) * math.cos(minute_angle)
    minute_hand_y = clock_center[1] + (minute_hand_length / 2) * math.sin(minute_angle)
    minute_hand_end_x = clock_center[0] + (minute_hand_length - 50) * math.cos(minute_angle)
    minute_hand_end_y = clock_center[1] + (minute_hand_length - 50) * math.sin(minute_angle)
    pygame.draw.line(screen, (0, 0, 0), (clock_center[0], clock_center[1]), (minute_hand_end_x, minute_hand_end_y), 8)

    # Draw the second hand
    second_angle = math.radians(current_second * 6 - 90)
    second_hand_x = clock_center[0] + (second_hand_length / 2) * math.cos(second_angle)
    second_hand_y = clock_center[1] + (second_hand_length / 2) * math.sin(second_angle)
    second_hand_end_x = clock_center[0] + (second_hand_length - 50) * math.cos(second_angle)
    second_hand_end_y = clock_center[1] + (second_hand_length - 50) * math.sin(second_angle)
    pygame.draw.line(screen, (0, 0, 0), (clock_center[0], clock_center[1]), (second_hand_end_x, second_hand_end_y), 4)

    # Update the display
    pygame.display.flip()

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
