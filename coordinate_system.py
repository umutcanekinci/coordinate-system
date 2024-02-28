import pygame

pygame.init()

width = 640
height = 640
size = (width, height)
window = pygame.display.set_mode(size)
white = (255, 255, 255) # rgb
red = (255, 0, 0)
green = (0, 255, 0)
magenta = (255, 0, 255)
gray = (178, 190, 181)
run = True

def DrawPageLines(surface, color, apsisColor, oordinateColor, topLeftPoint, bottomRightPoint, multiplier, coordinateWidth=1, pageLinesWidth=1, unitCirle=False):
    
    width = bottomRightPoint[0] - topLeftPoint[0]
    height = bottomRightPoint[1] - topLeftPoint[1]

    #-# column lines #-#
    for i in range(int(width/multiplier) + 1):
        pygame.draw.line(surface, color, (topLeftPoint[0] + (i)*multiplier, topLeftPoint[1]), (topLeftPoint[0] + (i)*multiplier, bottomRightPoint[1]), pageLinesWidth)
    
    #-# row lines #-#
    for i in range(int(height/multiplier) + 1):
        pygame.draw.line(surface, color, (topLeftPoint[0], topLeftPoint[1] + (i)*multiplier), (bottomRightPoint[0], topLeftPoint[1] + (i)*multiplier), pageLinesWidth)

    #-# coordinate apsis and oordinat #-#
    spaceLength = 30
    rowSpace = 5
    
    #-# oordinate #-#
    pygame.draw.line(surface, oordinateColor, (topLeftPoint[0] + (width/2), topLeftPoint[1] - spaceLength), (topLeftPoint[0] + (width/2), topLeftPoint[1] + height + spaceLength), coordinateWidth)
    
    #-# apsis #-#
    pygame.draw.line(surface, apsisColor, (topLeftPoint[0] - spaceLength, topLeftPoint[1] + (height/2)), (bottomRightPoint[0] + spaceLength, topLeftPoint[1] + (height/2)), coordinateWidth)
    
    #-# oordinate top side rows #-#
    pygame.draw.line(surface, oordinateColor, (topLeftPoint[0] + (width/2), topLeftPoint[1] - spaceLength), (topLeftPoint[0] + (width/2) + rowSpace, topLeftPoint[1] - spaceLength + rowSpace), coordinateWidth)
    pygame.draw.line(surface, oordinateColor, (topLeftPoint[0] + (width/2), topLeftPoint[1] - spaceLength), (topLeftPoint[0] + (width/2) - rowSpace, topLeftPoint[1] - spaceLength + rowSpace), coordinateWidth)
    
    #-# oordinate bot side rows #-#
    pygame.draw.line(surface, oordinateColor, (topLeftPoint[0] + (width/2), topLeftPoint[1] + height + spaceLength), (topLeftPoint[0] + (width/2) - rowSpace, topLeftPoint[1] + height + spaceLength - rowSpace), coordinateWidth)
    pygame.draw.line(surface, oordinateColor, (topLeftPoint[0] + (width/2), topLeftPoint[1] + height + spaceLength), (topLeftPoint[0] + (width/2) + rowSpace, topLeftPoint[1] + height + spaceLength - rowSpace), coordinateWidth)

    #-# apsis left side rows #-#
    pygame.draw.line(surface, apsisColor, (topLeftPoint[0] - spaceLength, topLeftPoint[1] + (height/2)), (topLeftPoint[0] - spaceLength + rowSpace, topLeftPoint[1] + (height/2) + rowSpace), coordinateWidth)
    pygame.draw.line(surface, apsisColor, (topLeftPoint[0] - spaceLength, topLeftPoint[1] + (height/2)), (topLeftPoint[0] - spaceLength + rowSpace, topLeftPoint[1] + (height/2) - rowSpace), coordinateWidth)
    
    #-# apsis right side rows #-#
    pygame.draw.line(surface, apsisColor, (bottomRightPoint[0] + spaceLength, topLeftPoint[1] + (height/2)), (bottomRightPoint[0] + spaceLength - rowSpace, topLeftPoint[1] + (height/2) - rowSpace), coordinateWidth)
    pygame.draw.line(surface, apsisColor, (bottomRightPoint[0] + spaceLength, topLeftPoint[1] + (height/2)), (bottomRightPoint[0] + spaceLength - rowSpace, topLeftPoint[1] + (height/2) + rowSpace), coordinateWidth)

    #-# unit circle #-#
    if unitCirle:
        pygame.draw.circle(surface, white, (topLeftPoint[0] + width/2, topLeftPoint[1] + height/2), multiplier, 1)
        
while run:
    
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run = False
    
    DrawPageLines(window, gray, green, magenta, (100,100), (500 ,500), 25, 3, 2, True)

    pygame.display.update()

pygame.quit()