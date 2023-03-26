import pygame

# initialize pygame
pygame.init()

# set up the display
size = (640, 480)
screen = pygame.display.set_mode(size)

# set up the font
font = pygame.font.Font(None, 36)

# set up the music playlist
playlist = ["1.mp3", "2.mp3", "3.mp3", "4.mp3", "5.mp3", "6.mp3"]
current_song = 0

# set up the music player
pygame.mixer.init()
pygame.mixer.music.set_volume(1)
pygame.mixer.music.load(playlist[current_song])

# set up the initial display text
text = font.render("Press Space to Play/Pause", True, (255, 255, 255))
text_rect = text.get_rect(center=(size[0] // 2, size[1] // 2))

# start the game loop
running = True
paused = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if paused:
                    pygame.mixer.music.unpause()
                    paused = False
                    text = font.render("Press Space to Play/Pause", True, (255, 255, 255))
                else:
                    pygame.mixer.music.pause()
                    paused = True
                    text = font.render("Press Space to Play/Pause", True, (255, 255, 255))
            elif event.key == pygame.K_RIGHT:
                current_song = (current_song + 1) % len(playlist)
                pygame.mixer.music.load(playlist[current_song])
                pygame.mixer.music.play()
                paused = False
                text = font.render("Press Space to Play/Pause", True, (255, 255, 255))
                print("Now playing:", playlist[current_song])
            elif event.key == pygame.K_LEFT:
                current_song = (current_song - 1) % len(playlist)
                pygame.mixer.music.load(playlist[current_song])
                pygame.mixer.music.play()
                paused = False
                text = font.render("Press Space to Play/Pause", True, (255, 255, 255))
                print("Now playing:", playlist[current_song])

    # update the display
    screen.fill((0, 0, 0))
    screen.blit(text, text_rect)
    pygame.display.flip()

# quit pygame
pygame.quit()
