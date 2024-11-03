"""
  Author: zvarros

  Date: June 12, 2024

  Description: Black and White (2 player platformer); both players work together in order to reach the door and access new levels. 
  Players can only land on platforms of their colour but can work together by standing on one anothers' heads.
"""

import pygame
import gameSprites
import gameLevels

def resetLevel(screen, white, black, platformGroup, door, allSprites, levelTracker):
  ''' this function triggers whenever a player goes out of bounds (bottom or sides of screen) or when the level has been won. 
  It takes the screen, both player sprites, the platform group (containing all platform sprites), the allSprites group, and the 
  level tracker object as parameters. It clears old sprites and replaces them in the correct starting position using the gameLevels 
  module. '''
  platformGroup.empty()  # clear old platforms
  platforms = gameLevels.startLevel(False, levelTracker.getLevel())  # get new platforms
  for platform in platforms:
    platformGroup.add(platform)  # add each platform individually

  door.rect.topleft = gameLevels.startLevel(True, levelTracker.getLevel())  # update door position

  whiteStartPos = gameLevels.resetCharacters(True, levelTracker.getLevel())
  blackStartPos = gameLevels.resetCharacters(False, levelTracker.getLevel())
  white.reset(whiteStartPos)
  black.reset(blackStartPos)

  allSprites.empty() # clears. GROUP not list
  if levelTracker.getLevel() == 6:
    allSprites.add(platformGroup, black, white, door)
  else:
    allSprites.add(platformGroup, black, white, door, levelTracker)

  if levelTracker.getLevel() == 1:
    subtitle = gameSprites.Subtitle("Players can only stand on platforms of their own colour", (10, 10), 17)
    allSprites.add(subtitle)
  elif levelTracker.getLevel() == 3:
    subtitle = gameSprites.Subtitle("Press 'Z' to change platform colour", (10, 10), 17)
    allSprites.add(subtitle)
  elif levelTracker.getLevel() == 6:
    subtitle = gameSprites.Subtitle("YOU WON! Enter the door to end game", (15, 50), 25)
    allSprites.add(subtitle)


def main():
  '''This function defines the 'mainline logic' for Black and White. It includes the setup (following the "IDEA" format) 
  and the main game loop (following the "ALTER" format). It also calls the end screen when the game has been won.'''
  # I - Initialize pygame
  pygame.init()
  pygame.mixer.init()


  # D - DISPLAY
  screen = pygame.display.set_mode((640, 480))
  pygame.display.set_caption("Black and White")

  # E - ENTITIES
  background = pygame.Surface(screen.get_size())
  background = background.convert()
  background.fill((11, 92, 222))
  screen.blit(background, (0, 0))

  # background music
  pygame.mixer.music.load("bgMusic.wav")
  pygame.mixer.music.set_volume(0.3)
  pygame.mixer.music.play(-1)

  # sound effects
  jumpSound = pygame.mixer.Sound("jump.ogg")
  jumpSound.set_volume(0.5)

  levelCompleteSound = pygame.mixer.Sound("levelComplete.wav")
  levelCompleteSound.set_volume(0.5)

  deathSound = pygame.mixer.Sound("death.wav")
  deathSound.set_volume(0.7)

  # scorekeeper sprite
  levelTracker = gameSprites.Scorekeeper()

  # sprites for platforms
  platformGroup= pygame.sprite.Group(gameLevels.startLevel(False, levelTracker.getLevel()))

  # sprite for door
  door = gameSprites.Door(gameLevels.startLevel(True, levelTracker.getLevel()))  

  # sprite for instructions
  subtitle = gameSprites.Subtitle("Players can only stand on platforms of their own colour", (10, 10), 17)
  
  # sprites for black and white players
  white = gameSprites.Player(gameLevels.resetCharacters(True, levelTracker.getLevel()), True, \
  {"left": pygame.K_LEFT, "right": pygame.K_RIGHT, "jump": pygame.K_UP}, 480)
  
  black = gameSprites.Player(gameLevels.resetCharacters(False, levelTracker.getLevel()), False, \
  {"left": pygame.K_a, "right": pygame.K_d, "jump": pygame.K_w}, 480) 

  
  
  allSprites = pygame.sprite.OrderedUpdates(platformGroup, black, white, door, subtitle, levelTracker) 

  # A - ACTION

  # A - ASSIGN 
  clock = pygame.time.Clock()
  keepGoing = True
  throughDoor = 0

  # L - LOOP
  while keepGoing:

    # TIME
    clock.tick(60) # supposed to be 30 but runs to slow; 60 for smooth animation

    # E - EVENT HANDLING
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        keepGoing = False
      elif event.type == pygame.KEYDOWN:                
        if event.key == pygame.K_UP:
          white.jump()
          jumpSound.play()
        if event.key == pygame.K_w:
          black.jump()
          jumpSound.play()
        if event.key == pygame.K_z:
          for sprite in platformGroup:
            if isinstance(sprite, gameSprites.Switch):
              sprite.switchColour()

    # Check for collisions between player sprites and the door
    if pygame.sprite.collide_rect(white, door) and white.toggleReactions:
      white.toggleReactions= False
      throughDoor += 1
      white.kill()
    if pygame.sprite.collide_rect(black, door) and black.toggleReactions:
      black.toggleReactions= False
      throughDoor += 1
      black.kill()

    # player collisions with walls/floor
    if (white.rect.bottom > 480 or white.rect.left < 0 or white.rect.right > 640) and throughDoor < 2:
      resetLevel(screen, white, black, platformGroup, door, allSprites, levelTracker)
      throughDoor = 0
      deathSound.play()
    if (black.rect.bottom > 480 or black.rect.left < 0 or black.rect.right > 640) and throughDoor < 2:
      resetLevel(screen, white, black, platformGroup, door, allSprites, levelTracker)
      throughDoor = 0
      deathSound.play()


    # check if level won
    if throughDoor == 2:
      levelTracker.addLevel()
      levelCompleteSound.play()
      if levelTracker.levelsCompleted != 7:
        resetLevel(screen, white, black, platformGroup, door, allSprites, levelTracker)
      else:
        keepGoing = False
      throughDoor = 0

    # R - REFRESH SCREEN
    allSprites.clear(screen, background)
    platformGroup.update()
    playersAlive = []
    for player in [white, black]:
      if player.alive():
        playersAlive.append(player)
    for player in playersAlive:
      player.update(platformGroup, playersAlive)
    levelTracker.update()
    allSprites.draw(screen)
    pygame.display.flip()

  # Close the game window
  pygame.time.delay(1000)
  pygame.quit()    

# Call the main function
main()    

