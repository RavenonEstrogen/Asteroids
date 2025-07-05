import pygame
import random
from circleshape import *
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20, 50)
        first_split = pygame.Vector2.rotate(self.velocity, random_angle)
        second_split = pygame.Vector2.rotate(self.velocity, -random_angle)
        smaller_asteroids_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid_one = Asteroid(self.position.x, self.position.y, smaller_asteroids_radius)
        asteroid_one.velocity = first_split * 1.2
        asteroid_two = Asteroid(self.position.x, self.position.y, smaller_asteroids_radius)
        asteroid_two.velocity = second_split * 1.2