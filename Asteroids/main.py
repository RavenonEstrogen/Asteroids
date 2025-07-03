import pygame
# allows to use code from open-source pygame library
from constants import *
# allows to use constants from the file

def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    


if __name__ == "__main__":
    main()
