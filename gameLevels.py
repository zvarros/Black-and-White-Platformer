"""
    Author: Alex Lindqvist

    Date: June 12, 2024

    Description: Levels for Blak and White game (positioning of platforms, players, and doors)
"""

import pygame
import gameSprites


def startLevel(door, level):
  ''' this function takes itself, the boolean value door, and level as parameters and returns either the platforms or door depending on the door parameter'''
  WHITE = (255, 255, 255)
  BLACK = (0, 0, 0)

  if level == 1:
    black1 = gameSprites.Platform((50, 150), 200, 12, False, BLACK)
    white1 = gameSprites.Platform((50, 250), 200, 12, True, WHITE)
    black2 = gameSprites.Platform((300, 250), 200, 12, False, BLACK)
    white2 = gameSprites.Platform((300, 150), 200, 12, True, WHITE)

    if door:
      return (550, 175)
    else:
      return black1, black2, white1, white2

  elif level == 2:
    black1 = gameSprites.Platform((40, 100), 50, 12, False, BLACK)
    white1 = gameSprites.Platform((100, 100), 50, 12, True, WHITE)
    black2 = gameSprites.Platform((250, 350), 50, 12, False, BLACK)
    white2 = gameSprites.Platform((310, 350), 50, 12, True, WHITE)
    black3 = gameSprites.Platform((400, 225), 50, 12, False, BLACK)
    white3 = gameSprites.Platform((460, 225), 50, 12, True, WHITE)

    if door:
      return (575, 200)
    else:
      return black1, black2, white1, white2, black3, white3

  elif level == 3:
    white1 = gameSprites.Platform((40, 100), 75, 12, False, BLACK)
    black1 = gameSprites.Platform((150, 100), 75, 12, True, WHITE)
    switch1 = gameSprites.Switch((250, 250), False)

    if door:
      return(575, 200)
    else:
      return black1, white1, switch1

  elif level == 4:
    black1 = gameSprites.Platform((30, 350), 150, 12, False, BLACK)
    white1 = gameSprites.Platform((125, 300), 150, 12, True, WHITE)
    white2 = gameSprites.Platform((400, 400), 100, 12, True, WHITE)
    black2 = gameSprites.Platform((325, 100), 40, 250, False, BLACK)
  
    if door:
      return (500, 150)
    else:
      return black1, white1, white2, black2

  elif level == 5:
    white = gameSprites.Platform((30, 350), 550, 12, True, WHITE)
    black1 = gameSprites.Platform((100, 200), 25, 135, False, BLACK)
    black2 = gameSprites.Platform((400, 200), 25, 135, False, BLACK)

    if door:
      return (500, 250)
    else:
      return white, black1, black2

  else:
    white = gameSprites.Platform((30, 300), 225, 12, True, WHITE)
    black = gameSprites.Platform((400, 300), 225, 12, False, BLACK)

    if door:
      return (305, 200)
    else:
      return white, black



def resetCharacters(white, level):
  ''' this function takes itself, the white boolean value, and the current level as arguments and returns either the black or white 
  player start positions depending on level and the white boolean argument'''
  if level == 1:
    if white:
      return (125, 100)
    else:
      return (75, 100)
      
  elif level == 2:
    if white:
      return (125, 30)
    else:
      return (65, 30)
      
  elif level == 3:
    if white:
      return (175, 30)
    else:
      return (65, 30)
      
  elif level == 4:
    if white:
      return (150, 250)
    else:
      return (50, 300)
      
  elif level == 5:
    if white:
      return (50, 300)
    else:
      return (50, 250)
      
  else:
    if white:
      return (50, 250)
    else:
      return (550, 250)

