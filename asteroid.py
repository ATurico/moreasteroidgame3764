import pygame
import random

class Asteroid(pygame.sprite.Sprite):
  def __init__(self):
    super().__init__()
    self.image = pygame.image.load('asteroid2.png')
    self.image = pygame.transform.smoothscale(self.image, (random.randint(30, 70), random.randint(30, 70)))
    self.speed = pygame.math.Vector2(0,3)
    self.speed.rotate_ip(random.randint(0,360))
    self.rect = self.image.get_rect()
    self.rect.center = (random.randint(30, 870), random.randint(30, 570))
    
  def update(self):
      screen_info = pygame.display.Info()
      self.rect.move_ip(self.speed)
      if self.rect.bottom > screen_info.current_h or self.rect.top < 0:
        self.speed[1] *= -1
        self.image = pygame.transform.flip(self.image, False, True)
        self.rect.move_ip(0, self.speed[1])

      if self.rect.right > screen_info.current_w or self.rect.left < 0:
        self.speed[1] *= -1
        self.image = pygame.transform.flip(self.image, False, True)
        self.rect.move_ip(0, self.speed[1])
        self.speed[0] *= -1
        self.image = pygame.transform.flip(self.image, True, False)
        self.rect.move_ip(self.speed[0], 0)