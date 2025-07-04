import pygame
# allows to use code from open-source pygame library
from constants import *
# allows to use constants from the file
from player import Player
# allows to use Player class

def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS)

    fpsclock = pygame.time.Clock()
    dt = 0

    while True:
        for event in pygame.event.get(): # allows to quit the game
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen, (0, 0, 0)) # fill screen black

        player.draw(screen) # draw player
        player.update(dt)

        pygame.display.flip()
        fpsclock.tick(60)
        dt = fpsclock.get_time() / 1000

if __name__ == "__main__":
    main()
