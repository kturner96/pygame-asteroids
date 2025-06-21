import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *



def main() :
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()


    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots, updatable, drawable)





    player = Player(x=SCREEN_WIDTH/2, y=SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()

    while True :
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updatable.update(dt)
        screen.fill((0, 0, 0))

        for asteroid in asteroids:
            if player.collision_detect(asteroid):
                print("Game over!")
                pygame.quit()
                exit()

        for asteroid in asteroids:
            for shot in shots:

                if shot.collision_detect(asteroid):
                    asteroid.split()
                    shot.kill()
        

        # Loop over all drawables
        for drawables in drawable :
            drawables.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000

        




if __name__ == "__main__":
    main()