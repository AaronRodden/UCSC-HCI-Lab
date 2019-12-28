import pygame
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt


def drawText(surface, text, color, rect, font, aa=False, bkg=None):
    y = rect.top
    lineSpacing = -2

    # get the height of the font
    fontHeight = font.size("")[1]

    while text:
        i = 1

        # determine if the row of text will be outside our area
        if y + fontHeight < rect.bottom:
            break

        # determine maximum width of line
        while font.size(text[:i])[0] < rect.width and i < len(text):
            i += 1

        # if we've wrapped the text, then adjust the wrap to the last word      
        if i < len(text): 
            i = text.rfind(" ", 0, i) + 1

        # render the line and blit it to the surface
        if bkg:
            image = font.render(text[:i], 1, color, bkg)
            image.set_colorkey(bkg)
        else:
            image = font.render(text[:i], False, color)

        surface.blit(image, (rect.left, y))
        y += fontHeight + lineSpacing

        # remove the text we just blitted
        text = text[i:]

    return text

BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
BLUE     = (   0,   0, 255)

pygame.init()
pygame.font.init()

size = (1200,750)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("test")
font = pygame.font.SysFont("monospace", 20)

rect = pygame.draw.rect(screen,BLACK,(10,10,10,10), 0)
text = ""

test = True

while test:
    for event in pygame.event.get():
        
        if event.type == pygame.KEYDOWN:
            if event.type == pygame.QUIT or event.key==pygame.K_ESCAPE :
                        pygame.quit()
        
        y = 5
        fontHeight = 10
        lineSpacing = 5
        while text:
            i = 1
            # determine if the row of text will be outside our area
            if fontHeight + y < rect.bottom:
                break
    
            # determine maximum width of line
            while font.size(text[:i])[0] < rect.width and i < len(text):
                i += 1
    
            # if we've wrapped the text, then adjust the wrap to the last word      
            if i < len(text): 
                i = text.rfind(" ", 0, i) + 1
    
            # render the line and blit it to the surface
            if None:
                image = font.render(text[:i], 1, BLACK, None)
                image.set_colorkey(None)
            else:
                image = font.render(text[:i], False, BLACK)
    
            screen.blit(image, (rect.left, y))
            y += fontHeight + lineSpacing
    
            # remove the text we just blitted
            text = text[i:]
        
        screen.fill(WHITE)
        pygame.display.update()
        pygame.display.flip()