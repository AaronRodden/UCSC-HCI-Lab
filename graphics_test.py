import pygame
import random
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt

pygame.init()
pygame.font.init()

myfont = pygame.font.SysFont('Comic Sans MS', 30)
secondFont = pygame.font.SysFont("monospace", 15)

def drawRect(rand):
    
    if (rand == 1):
        pygame.draw.rect(screen, RED, [55, 50, 20, 25])
    elif (rand == 2):
        pygame.draw.rect(screen, BLUE, [55, 50, 20, 25])
    elif (rand == 3):
        pygame.draw.rect(screen, GREEN, [55, 50, 20, 25])
    elif (rand == 4):
        pygame.draw.rect(screen, BLACK, [55, 50, 20, 25])


BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
BLUE     = (   0,   0, 255)

PI = 3.141592653

size = (700,500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("graphics test")

rectAppear = pygame.USEREVENT + 1
rectRemove = pygame.USEREVENT + 2
pygame.time.set_timer(rectAppear,5000)

clock = pygame.time.Clock()

count = 0
memCount = 0

memString = ""

inputTracker = []
inputTimer = []

thinking = False 

running = True

rectDraw = False
rectErase = False

randRect = random.randint(1,4)

prime = True

while running:

    
    for event in pygame.event.get():
        #print(count)
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key==pygame.K_ESCAPE :
            running=False
        
        if (count >= 0):
            prime = False
        
        if (prime == True):
            
            if event.type == rectAppear:
                rectDraw = True
                
            if event.type == rectRemove:
                rectErase = True
            
            # --- Game logic
            
            # --- Drawing 
            screen.fill(WHITE)
            
            if (rectDraw == True):
                drawRect(randRect)
                pygame.time.set_timer(rectRemove,1000)
    
            if (rectErase == True):
                screen.fill(WHITE)
                rectDraw = False
                rectErase = False
                randRect = random.randint(1,4)
                count += 1
                
            pygame.display.flip()
            
            #pygame.display.update()
            #print(clock)
            clock.tick(60)
            
        else: 
            
            #print("Memory Phase")
            textsurface = myfont.render('Memory Phase', False, (0, 0, 0))
            
            
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key==pygame.K_ESCAPE :
                running=False
            
            if memCount > 19:
                running = False
                continue
                
            questionString = "Question " + str(memCount+1)
            question = myfont.render(questionString, False, (0, 0, 0))
            
            #need to do some logic that saves the time the first time then doesent update untill the question is answered
            if (thinking == False):
                start_time = pygame.time.get_ticks()
                print (start_time)
                thinking = True
                
            if event.type == pygame.KEYDOWN:
                
                if event.key == pygame.K_RETURN:
                    memCount+= 1
                
                if (pygame.K_a <= event.key <= pygame.K_z) or event.key == pygame.K_SPACE: # checks the key pressed
                    character = chr(event.key) #converts the number to a character
                    memString += str(character) #adds the number to the end of the string
                
                if event.key == pygame.K_BACKSPACE:
                    memString = memString[:-1]
                
                
#                if event.key == pygame.K_DOWN:
#                    elapsed_time = (pygame.time.get_ticks() - start_time) / 1000.0
#                    print("User pressed down")
#                    inputTracker.append("DOWN")
#                    inputTimer.append(elapsed_time)
#                    memCount+=1
#                    thinking = False
#                elif event.key == pygame.K_UP:
#                    elapsed_time = (pygame.time.get_ticks() - start_time) / 1000.0
#                    print("User pressed up")
#                    inputTracker.append("UP")
#                    inputTimer.append(elapsed_time)
#                    memCount+=1
#                    thinking = False
#                elif event.key == pygame.K_LEFT:
#                    elapsed_time = (pygame.time.get_ticks() - start_time) / 1000.0
#                    print("User pressed left")
#                    inputTracker.append("LEFT")
#                    inputTimer.append(elapsed_time)
#                    memCount+=1
#                    thinking = False
#                elif event.key == pygame.K_RIGHT:
#                    elapsed_time = (pygame.time.get_ticks() - start_time) / 1000.0
#                    print("User pressed right")
#                    inputTracker.append("RIGHT")
#                    inputTimer.append(elapsed_time)
#                    memCount+=1
#                    thinking = False
            
            recall = secondFont.render(memString, False, (0 ,0 ,0 ))
            
            screen.fill(WHITE)
            screen.blit(textsurface,(260,0))
            screen.blit(question, (50, 100))
            screen.blit(recall, (260,400))
            pygame.display.flip()
            clock.tick(60)
            

print (inputTracker)  
print(inputTimer)
s = pd.Series(inputTracker,inputTimer)
print(s)
s.to_csv('output.csv', encoding='utf-8')
#f.close()
pygame.quit()
