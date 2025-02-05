import random
import pygame
from circleshape import *
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self,x,y,radius):
        super().__init__(x,y,radius)
        
    

    def draw(self, screen):
        pygame.draw.circle(
            screen,(225,225,225),(int(self.position.x),int(self.position.y)),self.radius,2
            )
    
    def update(self, dt):
        self.position += (self.velocity * dt)
        
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        random_angle = random.uniform(20,50)
        vel1 = self.velocity.rotate(random_angle)
        vel2 = self.velocity.rotate(-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        
        Asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        Asteroid1.velocity = vel1 * 1.2
        Asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        Asteroid2.velocity = vel2 * 1.2
        
        #self.spawn(new_radius, random_angle, self.velocity * 1.2)
        
        
        