import os, sys
import pygame
import icmpcomm

WHITE=(255,255,255)
ORANGE=(214,137,16)
# We need more comments!
print("Starting pygame...")
pygame.display.init()
screen = pygame.display.set_mode((640, 340))

comm = icmpcomm.MonitorThread()
comm.start()

gameActive = True
while gameActive: 
init() -> None

  pygame.draw.rect(screen, ORANGE, [150, 150, 200, 100])
  pygame.draw.rect(screen, ORANGE, [150, 30, 200, 100])
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      print("Got quit! Returning...")
      gameActive = False
  pygame.display.flip()

comm.abort = True
print("Quitting pygame...")
pygame.display.quit()



#more comments
