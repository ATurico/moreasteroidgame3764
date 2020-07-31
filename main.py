import pygame, pandas as pd
from ship import *
from asteroid import *

pygame.init()
screen_info = pygame.display.Info()
print(screen_info)
size = (width, height) = (screen_info.current_w, screen_info.current_h)
screen = pygame.display.set_mode(size)
clock =  pygame.time.Clock()
color = (0, 10, 30)

df = pd.read_csv('game_info.csv')

Numlevels = df['LevelNum'].max()
Level = df['LevelNum'].min()
LevelData = df.iloc[Level]
AsteroidCount = LevelData['AsteroidCount']
player = Ship((LevelData['PlayerX'], LevelData['PlayerY']))
Asteroids = pygame.sprite.Group()

def init():
  player.reset((35,300))
  for i in range(AsteroidCount):
    Asteroids.add(Asteroid())

def main():
   init()
   global Level
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
      #danger.update()
      player.update()
      get_hit = pygame.sprite.spritecollide(player, Asteroids, False)
      screen.fill(color)
      #screen.blit(danger.image, danger.rect)
      Asteroids.draw(screen)
      Asteroids.update()
      screen.blit(player.image, player.rect)
      pygame.display.flip()

      if player.checkReset(800):
        if Level == Numlevels:
          break
        else:
          Level += 1
          init()
      elif get_hit:
        player.reset((35, 300))

if __name__=='__main__':
  main()