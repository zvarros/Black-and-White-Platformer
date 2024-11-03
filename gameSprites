"""
    Author: zvarros

    Date: June 12, 2024
    
    Description: Sprites for Blak and White game
"""

import pygame

class Player(pygame.sprite.Sprite):
  ''' Sprite subclass for the players of the Black and White game. It contains all the code for their functionality including 
  movement, collision detection, and animation.'''
  def __init__(self, xy, colour, controls, screenHeight):
    ''' this is the initialization for the Player class. It takes the xy coordinates (tuple), colour (boolean), controls (dictionary), 
    and the height of the screen (integer) as parameters. It initializes all instance variables and loads all images for player animation. '''
    pygame.sprite.Sprite.__init__(self)
    if colour:
      self.leftImage = pygame.image.load("wLeft.png")
      self.rightImage = pygame.image.load("wRight.png")
      self.leftShrug = pygame.image.load("wShrugLeft.png")
      self.rightShrug = pygame.image.load("wShrugRight.png")
      self.rightRUp = pygame.image.load("wRightRUp.png")
      self.leftRUp = pygame.image.load("wLeftRUp.png")
      self.rightLUp = pygame.image.load("wRightLUp.png")
      self.leftLUp = pygame.image.load("wLeftLUp.png")
    else:
      self.leftImage = pygame.image.load("bLeft.png")
      self.rightImage = pygame.image.load("bRight.png")
      self.leftShrug = pygame.image.load("bShrugLeft.png")
      self.rightShrug = pygame.image.load("bShrugRight.png")
      self.rightRUp = pygame.image.load("bRightRUp.png")
      self.leftRUp = pygame.image.load("bLeftRUp .png")
      self.rightLUp = pygame.image.load("bRightLUp.png")
      self.leftLUp = pygame.image.load("bLeftLUp.png")

    self.carouselPos = 0
    self.leftCarousel = [self.leftRUp, self.leftImage, self.leftLUp, self.leftImage]
    self.rightCarousel = [self.rightRUp, self.rightImage, self.rightLUp, self.rightImage]
    
    self.image = self.rightImage  
    self.rect = self.image.get_rect()
    self.rect.topleft = xy  # placement of player 
    self.colour = colour #which platforms plater can land on (bool) 
    self.controls = controls  # dict
    self.screenHeight = screenHeight
    self.velocityY = 0
    self.velocityX = 0
    self.jumpsLeft = 2   
    self.jumpCooldown = 0  #long press doublejump preventation
    self.mvmtCooldown = 0
    self.standingCooldown = 0
    self.isMoving = False
    self.toggleReactions= True
    
  def update(self, platforms, players):
    ''' this is the update method of the player class. It takes the object, the platform group, and the players alive as parameters. 
    It calls the handleKeys, applyGravity, horizontalCollisions, and verticalCollisions methods (passing the platform group and players 
    alive to the collision detection methods) in order to determine the x and y positions of the sprite. It then handles player 
    animation by either reducing the cooldown or calling the switchStandingImage method.'''
    self.handleKeys()
    self.applyGravity()
    self.rect.x += self.velocityX
    self.horizontalCollisions(platforms, players)
    self.rect.y += self.velocityY
    self.verticalCollisions(platforms, players)
    if self.jumpCooldown > 0:
      self.jumpCooldown -= 1
    if self.standingCooldown > 0:
      self.standingCooldown -= 1
    else:
      self.switchStandingImage()
      self.standingCooldown = 20

  def switchStandingImage(self):
    ''' this function handles animation for players at rest. It runs through a list of if/elif statements to select 
    the correct next image in the group'''
    if (self.image == self.leftRUp) or (self.image == self.leftLUp):
      self.image = self.leftImage
    elif self.image == (self.rightRUp) or (self.image == self.rightLUp):
      self.image = self.rightImage
    elif self.image == self.leftImage:
      self.image = self.leftShrug
    elif self.image == self.leftShrug:
      self.image = self.leftImage
    elif self.image == self.rightImage:
      self.image = self.rightShrug
    elif self.image == self.rightShrug:
      self.image = self.rightImage

  def handleKeys(self):
    ''' this method handles player movement on the x axis (horizontal). It takes itself as a parameter. It creates a list of the 
    keys pressed and then changes the x velocity instance variable accordingly; it matches the keys pressed to the controls 
    instance dictionary and if the key corresponding the the player's left or right movement has been pressed, it updates the 
    instance variable accordingly. This method also updates the player's walking animation by checking that the movement countdown 
    is zero and then changing the image to the next one in the correct carousel. If the conditions are not satisfied, it either decreases 
    the countdown or if no keys have been pressed, sets the is moving instance variable to false and resets the movement countdown. '''
    keys = pygame.key.get_pressed()
    self.velocityX = 0
    if keys[self.controls["left"]]:
      self.velocityX = -5
      if self.mvmtCooldown == 0:
        self.image = self.leftCarousel[self.carouselPos]
        if self.carouselPos != 3:
          self.carouselPos += 1
        else:
          self.carouselPos = 0
        self.mvmtCooldown = 10
      else:
        self.mvmtCooldown -= 1
      self.isMoving = True
    elif keys[self.controls["right"]]:
      self.velocityX = 5
      if self.mvmtCooldown == 0:
        self.image = self.rightCarousel[self.carouselPos]
        if self.carouselPos != 3:
          self.carouselPos += 1
        else:
          self.carouselPos = 0
        self.mvmtCooldown = 10
      else:
        self.mvmtCooldown -= 1
      self.isMoving = True
    else:
      self.mvmtCooldown = 0
      self.isMoving = False

  def jump(self):
    ''' this method handles the player jumping. It takes itself as a parameter and checks that the jump cooldown and double jump 
    conditions are satified before jumping. It then changes its y velocity (which in conjunction with the applyGravity method gives 
    the appearance of realistic jumping), adds a jump to the jump counter (in order to prevent triple-jumping), and sets the jump 
    cooldown to 10 (in order to prevent long aps from registering as multiple jumps). '''
    if self.jumpsLeft > 0 and self.jumpCooldown == 0:
      self.velocityY = -15
      self.jumpsLeft -= 1
      self.jumpCooldown = 10  # set cooldown period after jumping

  def applyGravity(self):
    ''' this function causes the players' downwards movement. It adds one to the player's y velocity (moving it towards the bottom of the screen.'''
    self.velocityY += 1 # gravity constant
      
  def reset(self, xy):
    ''' this function resets the player's position on the screen as well as the x and y velocity, jumps left, jump cooldown, and 
    toggle reactions instance variables. It takes itself and the xy coordinates as parameters. '''
    self.rect.topleft = xy
    self.velocityY = 0
    self.velocityX = 0
    self.jumpsLeft = 2
    self.jumpCooldown = 0
    self.toggleReactions = True

  def horizontalCollisions(self, platforms, players):
    ''' this function checks for horizontal collisions and applies their logic. It takes itself, the platform group, and the players 
    alive (as a list) as parameters; it then creates lists of collided platforms and players using pygame's spritecollide. If the platform 
    is the same colour as the player, it checks the player's movement direction and sets its side coordinate to the corresponding platform 
    side coordinate. If the toggleReactions instance variable is true, players will push one another (slower than walking speed) but not 
    go through one another'''
    collidedPlatforms = pygame.sprite.spritecollide(self, platforms, False)
    collidedPlayers = pygame.sprite.spritecollide(self, players, False)
    for platform in collidedPlatforms: # platform collision
      if self.colour == platform.colour:
        if self.velocityX > 0:  # Moving right
          self.rect.right = platform.rect.left
        elif self.velocityX < 0:  # Moving left
          self.rect.left = platform.rect.right
    if self.toggleReactions:
      for player in collidedPlayers: # player collision
        if player != self:  # Avoid self-collision
          if self.velocityX > 0:  # Moving right
            player.rect.left += 2
            self.rect.right = player.rect.left
          elif self.velocityX < 0:  # Moving left
            player.rect.right -= 2
            self.rect.left = player.rect.right

  def verticalCollisions(self, platforms, players):
    ''' this function check for vertical collisions and handles them. It takes itself, the platform gorup, and the players alive 
    (as a list) as parameters. It creates lists for the collided players and collided platforms using spritecollide. If the player colour 
    mathces the platform colour (bool), the bottom of the player becomes equal to the top of the platform. The same goes for the other 
    player if the toggle reactions instance variable is true.'''
    collidedPlatforms = pygame.sprite.spritecollide(self, platforms, False)
    collidedPlayers = pygame.sprite.spritecollide(self, players, False)
    for platform in collidedPlatforms: # platform collision
      if self.colour == platform.colour:
        if self.velocityY > 0:  # falling
          self.rect.bottom = platform.rect.top
          self.velocityY = 0
          self.jumpsLeft = 2
          self.jumpCooldown = 0
        elif self.velocityY < 0:  # jumping
          self.rect.top = platform.rect.bottom
          self.velocityY = 1  # gravity
    if self.toggleReactions:
      for player in collidedPlayers: # player collision
        if player != self:  # avoid self-collision
          if self.velocityY > 0:  # falling
            self.rect.bottom = player.rect.top
            self.velocityY = 0
            self.jumpsLeft = 2
            self.jumpCooldown = 0
          elif self.velocityY < 0:  # jumping
            self.rect.top = player.rect.bottom
            self.velocityY = 1  # gravity
      
class Platform(pygame.sprite.Sprite):
  ''' this is the class for the basic platforms in the black and white game. It uses pygame's sprite class and creates rectangular 
    objects that act as platforms to the player sprites. '''
  def __init__(self, xy, width, height, colour, colourFill):
    ''' this method initializes the platform class. It takes itself, the xy coordinates (tuple), the width (integer), height (integer), 
    colour (boolean), and colour to fill it with (tuple) as arguments. It initializes the pygame sprite module and creates a rectangle 
    in the size specified by width and height, then fills it with the colour specified by colourFill. It positions it with the top left 
    corner in the position of the xy tuple. '''
    pygame.sprite.Sprite.__init__(self)
    self.image = pygame.Surface((width, height))
    self.colourFill = colourFill
    self.image.fill(self.colourFill)
    self.colour= colour # bool
    self.rect = self.image.get_rect()
    self.rect.topleft = xy

class Switch(pygame.sprite.Sprite):
  ''' Sprite subclass for the switch platforms '''
  def __init__(self, xy, colour):
    ''' this method initializes the switching platforms in black and white. It takes itself, the xy coordinates (tuple), and 
    colour (bool) as arguments and initializes the original position and colour of the platform as well as loading its images 
    and assigning them to instance variables'''
    pygame.sprite.Sprite.__init__(self)
    self.colour = colour
    self.blackImage = pygame.image.load("switchBlack.png")
    self.whiteImage = pygame.image.load("switchWhite.png")
    if self.colour:
      self.image = self.whiteImage
    else:
      self.image = self.blackImage
    self.rect = self.image.get_rect()
    self.rect.topleft = xy
      
  def switchColour(self):
    ''' Switches colour by changing image and colour instance variable'''
    self.colour= not self.colour
    if self.colour:
      self.image = self.whiteImage
    else:
      self.image = self.blackImage

class Door(pygame.sprite.Sprite):
  ''' Sprite subclass for the door '''
  def __init__(self, xy):
    ''' Initializes sprite; takes itself and xy coordinates (tuple) as parameters and loads the image in the corresponding location'''
    pygame.sprite.Sprite.__init__(self)
    self.image = pygame.image.load("door (4).png")
    self.rect = self.image.get_rect()
    self.rect.topleft = xy


class Scorekeeper(pygame.sprite.Sprite):
  '''Sprite subclass ScoreKeeper to display the current points'''
  def __init__(self):
    '''initializer to set the font and score for the scorekeeper'''  
    pygame.sprite.Sprite.__init__(self)
    self.font = pygame.font.SysFont("Arial", 25)
    self.levelsCompleted = 1

  def getLevel(self):
    '''accessor to return current number of points'''
    return self.levelsCompleted

  def addLevel(self):
    ''' method to increase levels completed by one'''
    self.levelsCompleted += 1

  def update(self):
    ''' this module renders and positions the scorekeeper text on each refresh.'''
    self.image = self.font.render("Level " + str(self.levelsCompleted) + "/5", True, (0, 0, 0))
    self.rect = self.image.get_rect()
    self.rect.topright = (630, 10)  
    

class Subtitle(pygame.sprite.Sprite):
  ''' Sprite subclass for subtitles; displays text'''
  def __init__(self, msg, xy, fontSize):
    ''' Initializes Subtitle sprite; takes itself, message (string), xy coords (tuple), and font size (integet) as parameters and initializes the font'''
    pygame.sprite.Sprite.__init__(self)
    self.font = pygame.font.SysFont("Arial", fontSize)
    self.image = self.font.render(msg, True, (0, 0, 0))
    self.rect = self.image.get_rect()
    self.rect.topleft = xy  # position text at top center


