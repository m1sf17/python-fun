import os, sys
import pygame

WHITE=(255,255,255)
ORANGE=(214,137,16)
# We need more comments!
print("Starting pygame...")
pygame.display.init()
screen = pygame.display.set_mode((640, 340))

gameActive = True
while gameActive: 

  pygame.draw.rect(screen, WHITE, [150, 150, 200, 100], 2)
  pygame.draw.rect(screen, ORANGE, [150, 30, 200, 100], 2)
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      print("Got quit! Returning...")
      gameActive = False
  pygame.display.flip ()     

print("Quitting pygame...")
pygame.display.quit()

