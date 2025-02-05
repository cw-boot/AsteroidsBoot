import pygame
from constants import *
from player import *

def main():
    #print("Starting asteroids!")
    #print("Screen width: "+ str(SCREEN_WIDTH))
    #print("Screen height: "+ str(SCREEN_HEIGHT))
    updateable = pygame.sprite.Group()
    drawables = pygame.sprite.Group()

    Player.containers = (updateable,drawables)
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    _clock = pygame.time.Clock()
    dt = 0.0
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, PLAYER_RADIUS)

    

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
    
        #pygame.Surface.fill(screen,color=(0,0,0))
        updateable.update(dt)
        screen.fill((0,0,0))
        for obj in drawables:
            obj.draw(screen)
        
        pygame.display.flip()
        dt = _clock.tick(60)/1000


if __name__ == "__main__":
    main()
