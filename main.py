import os, sys
import pygame
import icmpcomm

# Global variables
MOUSE_LEFT_BUTTON = 1
MOUSE_MIDDLE_BUTTON = 2
MOUSE_RIGHT_BUTTON = 3

# Global color values
WHITE=(255,255,255)
ORANGE=(214,137,16)
RED=(255, 0, 0)

# Initialize pygame subsystems and the screen
print("Starting pygame...")
pygame.display.init()
pygame.font.init()
screensize = (500, 340)
screen = pygame.display.set_mode(screensize)

#Display text on the screen
font = pygame.font.SysFont(None, 40)
text = font.render("Quit", True, RED)
textrect = [220, 190]

#extra text for the screen
font = pygame.font.SysFont(None, 40)
text1 = font.render("Start", True, RED)
textrect1 = [215, 65]

# Start ICMP monitor thread
comm = icmpcomm.MonitorThread()
comm.start()

#Start game loop
#A=connect to somebody
#B=Host the game
  

# Start main loop
gameActive = True
currentscreen = 0
while gameActive:
  if currentscreen == 0:
    #display boxes for foxes
    pygame.draw.rect(screen, ORANGE, [150, 150, 200, 100])
    pygame.draw.rect(screen, ORANGE, [150, 30, 200, 100])
    screen.blit(text, textrect)
    screen.blit(text1, textrect1)
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      print("Got quit! Returning...")
      gameActive = False
    if event.type == pygame.MOUSEBUTTONDOWN:
      print("Got mouse button!", event)
      if currentscreen == 0:
        if pygame.Rect([150,150,200,100]).collidepoint(event.pos):
          if event.button == MOUSE_LEFT_BUTTON:
            print("Clicked left button inside quit!")
            gameActive = False 
        if pygame.Rect([150,30,200,100]).collidepoint(event.pos):
          if event.button == MOUSE_LEFT_BUTTON:
            print("I'm suposed to start the game") 
  pygame.display.flip()

# Main loop has finished, so stop the pygame subsystems and tell the comm thread to abort
comm.abort = True
print("Quitting pygame...")
pygame.display.quit()
pygame.font.quit()
