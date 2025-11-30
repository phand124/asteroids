import pygame
import random
from logger import log_event
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from circleshape import CircleShape


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            child_angle = random.uniform(20, 50)
            child1_velocity = self.velocity.rotate(child_angle)
            child2_velocity = self.velocity.rotate(-child_angle)
            child_radius = self.radius - ASTEROID_MIN_RADIUS
            child1 = Asteroid(self.position.x, self.position.y, child_radius)
            child2 = Asteroid(self.position.x, self.position.y, child_radius)
            child1.velocity = child1_velocity * 1.2
            child2.velocity = child2_velocity * 1.2
