# from enum import Enum
# from pygame.locals import *


from numpy.distutils.misc_util import blue_text
import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((640, 480))

running = 1
blue = (0,0,255)
l = t = 50
w = 50
h = 50

while running:
  
  for event in pygame.event.get():
    w+=1
    h+=1
    box = Rect(l, t, w, h)
    pygame.draw.rect(screen, blue, box)
    if event.type == QUIT:
      running = 0
    else:
      screen.fill((120, 120, 120))
      
    pygame.draw.rect(screen, blue, box)
      
    print (event)


  
  
  pygame.display.flip()

pygame.quit()



# pygame.init()

# # class Color(Enum):
# #     RED = 1
# #     GREEN = 2
# #     BLUE = 3
# #     YELLOW = 4
# #     ORANGE = 5
# #     WHITE = 6


# class pythonRubix():
#     def pythonRubix(self):
#         self.rubix = self.makeNewRubix() # will be 6 3x3 boards


#     #Returns new Rubix in a 6x3x3 list
#     def makeNewRubix(self):
        
        # return [
        #     [Color.RED, Color.RED, Color.RED],
        #     [Color.RED, Color.RED, Color.RED],
        #     [Color.RED, Color.RED, Color.RED],

        #     [Color.GREEN, Color.GREEN, Color.GREEN],
        #     [Color.GREEN, Color.GREEN, Color.GREEN],
        #     [Color.GREEN, Color.GREEN, Color.GREEN],

        #     [Color.BLUE, Color.BLUE, Color.BLUE],
        #     [Color.BLUE, Color.BLUE, Color.BLUE],
        #     [Color.BLUE, Color.BLUE, Color.BLUE],

        #     [Color.YELLOW, Color.YELLOW, Color.YELLOW],
        #     [Color.YELLOW, Color.YELLOW, Color.YELLOW],
        #     [Color.YELLOW, Color.YELLOW, Color.YELLOW],

        #     [Color.ORANGE, Color.ORANGE, Color.ORANGE],
        #     [Color.ORANGE, Color.ORANGE, Color.ORANGE],
        #     [Color.ORANGE, Color.ORANGE, Color.ORANGE],

        #     [Color.WHITE, Color.WHITE, Color.WHITE],
        #     [Color.WHITE, Color.WHITE, Color.WHITE],
        #     [Color.WHITE, Color.WHITE, Color.WHITE]


        # ]