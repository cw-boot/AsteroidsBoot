import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    _clock = pygame.time.Clock()
    
    updateable = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updateable,drawables)
    Shot.containers = (shots, updateable, drawables)
    AsteroidField.containers = updateable
    asteroid_field = AsteroidField()

    Player.containers = (updateable,drawables)
    

   
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, PLAYER_RADIUS)
    
    dt = 0.0
    

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        updateable.update(dt)

        
        for a in asteroids:
            for s in shots:
                if a.collisionCheck(s):
                    a.split()
                    s.kill()

            if a.collisionCheck(player):
                print("GameOver!")
                return

        screen.fill((0,0,0))
        for obj in drawables:
            obj.draw(screen)
        
        
        pygame.display.flip()

        dt = _clock.tick(60)/1000


if __name__ == "__main__":
    main()
