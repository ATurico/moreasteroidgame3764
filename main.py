()import pygame
from ship import *
from asteroid import *

pygame.init()
screen_info = pygame.display.Info()
print(screen_info)
size = (width, height) = (screen_info.current_w, screen_info.current_h)
screen = pygame.display.set_mode(size)
clock =  pygame.time.Clock()
color = (0, 10, 30)

Numlevels = 4
Level = 1
AsteroidCount = 4
player = Ship()
Asteroids = pygame.sprite.Group()

def init():
  for i in range(AsteroidCount):
    Asteroids.add(Asteroid())

def main():
   while Level <= Numlevels:
      clock.tick(60)
      for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_RIGHT:
            player.speed[0] = 10
        elif event.type == pygame.KEYUP:
          if event.key == pygame.K_RIGHT:
            player.speed[0] = 0

        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_LEFT:
            player.speed[0] = -10
        elif event.type == pygame.KEYUP:
          if event.key == pygame.K_LEFT:
            player.speed[0] = 0

        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_UP:
            player.speed[1] = -10
        elif event.type == pygame.KEYUP:
          if event.key == pygame.K_UP:
            player.speed[1] = 0
            
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_DOWN:
            player.speed[1] = 10
        elif event.type == pygame.KEYUP:
          if event.key == pygame.K_DOWN:
            player.speed[1] = 0
      danger.update()
      player.update()
      screen.fill(color)
      screen.blit(danger.image, danger.rect)
      screen.blit(player.image, player.rect)
      pygame.display.flip()

if __name__=='__main__':
  main()
