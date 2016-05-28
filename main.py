import os, sys
import pygame

# We need more comments!
print("Starting pygame...")
pygame.display.init()
screen = pygame.display.set_mode((640, 480))

gameActive = True
while gameActive:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      print("Got quit! Returning...")
      gameActive = False

print("Quitting pygame...")
pygame.display.quit()

