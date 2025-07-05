import pygame
# allows to use code from open-source pygame library
import sys
from constants import *
# allows to use constants from the file
from player import Player
# allows to use Player class
from asteroid import Asteroid
# allows to use Asteroids class
from asteroidfield import AsteroidField
#
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS)
    asteroidfield = AsteroidField()

    fpsclock = pygame.time.Clock()
    dt = 0

    while True:
        for event in pygame.event.get(): # allows to quit the game
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen, (0, 0, 0)) # fill screen black

        for draws in drawable:
            draws.draw(screen) # draw player and asteroids
        updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.collision(player):
                print("Game over!")
                sys.exit()

        pygame.display.flip()
        fpsclock.tick(60)
        dt = fpsclock.get_time() / 1000

if __name__ == "__main__":
    main()
