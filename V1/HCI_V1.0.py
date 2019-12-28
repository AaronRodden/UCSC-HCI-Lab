import pygame
import random
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt

def paragraphToScreen(blurb):
    i = 0
    j = 1
    enter = False
    for character in blurb:
        if enter == True:
            j+=1
            i = 0
            enter = False
            continue
        if (character == '.'):
            enter = True
        char = font.render(character,False, (0, 0, 0))
        screen.blit(char, (i*10,j*20))
        i+=1


pygame.init()
pygame.font.init()

font = pygame.font.SysFont("monospace", 15)
smallText = pygame.font.Font("freesansbold.ttf",20)
titleFont = pygame.font.SysFont('Comic Sans MS', 30)

BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
BLUE     = (   0,   0, 255)

size = (1200,750)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("HCI_V1.0")

preLab = True

while preLab:
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            pygame.quit()
        
        button1 = pygame.Rect(550, 450, 100, 50)
        button1.center = (200,300)
        textRect1 = smallText.render("C1",False,(0,0,0))
        
        button2 = pygame.Rect(550,450,100,50)
        button2.center = (200, 400)
        textRect2 = smallText.render("C2",False,(0,0,0))
        
        button3 = pygame.Rect(550, 450, 100, 50)
        button3.center = (400,300)
        textRect3 = smallText.render("C3",False,(0,0,0))
        
        button4 = pygame.Rect(550,450,100,50)
        button4.center = (400, 400)
        textRect4 = smallText.render("C4",False,(0,0,0))
        
        if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos  # gets mouse position
                if button1.collidepoint(mouse_pos):
                    # prints current location of mouse
                    file = open("c1.txt", "r")
                    print('button1 was pressed at {0}'.format(mouse_pos))
                    preLab = False
                if button2.collidepoint(mouse_pos):
                    # prints current location of mouse
                    file = open("c2.txt", "r")
                    print('button2 was pressed at {0}'.format(mouse_pos))
                    preLab = False
                if button3.collidepoint(mouse_pos):
                    # prints current location of mouse
                    file = open("c3.txt", "r")
                    print('button3 was pressed at {0}'.format(mouse_pos))
                    preLab = False
                if button4.collidepoint(mouse_pos):
                    # prints current location of mouse
                    file = open("c4.txt", "r")
                    print('button2 was pressed at {0}'.format(mouse_pos))
                    preLab = False
                    
        
        
        screen.fill(WHITE)
        pygame.draw.rect(screen, BLUE,button1)
        screen.blit(textRect1,(190,290))
        pygame.draw.rect(screen, BLUE,button2)
        screen.blit(textRect2,(190,390))
        pygame.draw.rect(screen, BLUE,button3)
        screen.blit(textRect3,(390,290))
        pygame.draw.rect(screen, BLUE,button4)
        screen.blit(textRect4,(390,390))
        
        
        pygame.display.flip()

#file = open("c2.txt", "r")


blurb = file.read()


clock = pygame.time.Clock()

memString = ""

#blurbRemove = pygame.USEREVENT + 1
#pygame.time.set_timer(blurbRemove,5000)
blurbRemove = False

recallSentences = []
recallScore = []

running = True
reading = True

delayLoop = pygame.USEREVENT + 1
setTimer = False

while running:
    
    for event in pygame.event.get():
        
        if reading == True:
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key==pygame.K_ESCAPE :
                running=False
            
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                print("erase blurb!")
                reading = False
            
            
            screen.fill(WHITE)
            
            paragraphToScreen(blurb)
    
            pygame.display.flip()
            clock.tick(60)
        else:
            
            if setTimer == False:
                pygame.time.set_timer(delayLoop,5000)
                delay = True
                setTimer = True
            
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key==pygame.K_ESCAPE :
                running=False
            
            if event.type == delayLoop:
                delay = False
            
            if (delay == True):
                delayText = titleFont.render('Delay', False, (0, 0, 0))
                screen.fill(WHITE)
                screen.blit(delayText,(260,0))
                pygame.display.update()
                pygame.display.flip()
                clock.tick(60)
            
            else:
                recalling = True
                memString = ""
                while recalling:
                    
                    for event in pygame.event.get():
                    
                        if event.type == pygame.KEYDOWN:
                            
                            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key==pygame.K_ESCAPE :
                                recalling = False
                                running = False
                                reading = True
                            
                            if event.key == pygame.K_RETURN:
                                recalling = False
                                pygame.time.set_timer(delayLoop,5000)
                                delay = True
                                
                                recallSentences.append(memString)
                                #score algo will go hear
                                recallScore.append(0)
                        
                            if (pygame.K_a <= event.key <= pygame.K_z) or event.key == pygame.K_SPACE: # checks the key pressed
                                character = chr(event.key) #converts the number to a character
                                memString += str(character) #adds the number to the end of the string
                        
                            if event.key == pygame.K_BACKSPACE:
                                memString = memString[:-1]
                    
                    
                    recallText = titleFont.render('Recall', False, (0, 0, 0))
                    recall = font.render(memString, False, (0 ,0 ,0 ))
                    screen.fill(WHITE)
                    screen.blit(recallText,(260,0))
                    screen.blit(recall, (200,400))
                    pygame.display.update()
                    pygame.display.flip()
                    
                    
                    clock.tick(60)
        
print(recallSentences)
print(recallScore)
s = pd.DataFrame({'Sentences':recallSentences,'Score':recallScore})
print(s)
s.to_csv('V1_Out.csv', encoding='utf-8')

#
#response = ["adsfdsaf","qwerqwer"]
#currParData = pd.read_csv('test.csv')
#frames = [currParData,response]
#result = pd.concat(frames)
#currParData.append({'Response':response },ignore_index=True)
#print(result)

pygame.quit()