import sys
import pygame
from pygame.time import Clock
from constants import *
from player import *
from asteroidfield import *
from asteroids import *


def main():
    pygame.init()
    clk = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shots.containers = (shots, drawable, updatable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(color="#000000")
        updatable.update(dt)
        for asteroid in asteroids:
            if CircleShape.collision(player, asteroid):
                return sys.exit("Game over!")
            for shot in shots:
                if CircleShape.collision(shot, asteroid):
                    shot.kill()
                    asteroid.split()
        for item in drawable:
            item.draw(screen)
        pygame.display.flip()
        dt = clk.tick(60) / 1000
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()
