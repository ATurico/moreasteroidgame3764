import pygame

class Ship(pygame.sprite.Sprite):
  def __init__(self):
    super().__init__()
    self.image = pygame.image.load('Spaceship2.png')
    self.image = pygame.transform.smoothscale(self.image, (60, 60))
    self.rect = self.image.get_rect()
    self.rect.center = (35, 300)
    rotation = (270)
    self.image = pygame.transform.rotate(self.image, 270)
    self.speed = pygame.math.Vector2(0, 0)

  def update(self):
    self.rect.move_ip(self.speed)
    