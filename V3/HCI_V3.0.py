import pygame
import textwrap
import csv
import pandas as pd 
import random


def drawText(surface, text, color, rect, font, aa=False, bkg=None):
    #rect = Rect(rect)
    y = rect.top
    lineSpacing = -2

    # get the height of the font
    fontHeight = font.size("Tg")[1]

    while text:
        i = 1

        # determine if the row of text will be outside our area
        if y + fontHeight < rect.bottom:
            break

        # determine maximum width of line,
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
            image = font.render(text[:i], aa, color)

        surface.blit(image, (rect.left, y))
        y += fontHeight + lineSpacing

        # remove the text we just blitted
        text = text[i:]

    return text

# All credits too Max Knivets for the wrap method
# https://medium.com/@knivecmaksim/pygame-tutorial-2-wrapping-text-1abedcedf7bf

def wrap_text(message, wraplimit):
    return textwrap.fill(message, wraplimit)

def message_display(myfont, textvars, color, xy, wrap, message):
    xy = xy[:] # so we won't modify the original values
    font_object = myfont
    message = wrap_text(message,wrap)
    for part in message.split('\n'):
         rendered_text = font_object.render(part, True, (color))
         screen.blit(rendered_text,(xy))
         xy[1] += 25
#         pygame.display.update()
         


#Setup for lab such as fonts,colors, text wrap dimensions, screen size, screen name, and flags

pygame.init()
pygame.font.init()


font = pygame.font.SysFont("monospace", 20)
errorFont = pygame.font.SysFont("microsoftnewtailue", 30)
inputText = pygame.font.Font("freesansbold.ttf",30)
titleFont = pygame.font.SysFont('Comic Sans MS', 30)

BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
BLUE     = (   0,   0, 255)
GREY     = ( 129, 129, 129)

textvars = {'large':[90,22,90], 'medium':[50,43,45], 'normal':[25,88,20], 'small':[15,148,10]}

size = (1200,750)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("HCI_V2.0")

width, height = pygame.display.get_surface().get_size()

rect = pygame.Rect(1000,750,0,0)

saved = False

newParFlag = False
findData = True

buttonsFlag = True
saveFlag = False
noSaveFlag = False
randomFlag = False

#
# Here is the pre-lab part of this program, different buttons can be set,these buttons can set flags that effect the 
# experiment. 
#



while findData:
    preLab = True
    parInput = ""
    saveChoice = ""
    while preLab:
        for event in pygame.event.get():
            
            #change button size and shape
            sButton = pygame.Rect(550, 450, 135, 50)
            sButton.center = (100,200)
            sButtonText = inputText.render("Save",False,(0,0,0))
        
            nButton = pygame.Rect(550,450,135,50)
            nButton.center = (200, 300)
            nButtonText = inputText.render("No Save",False,(0,0,0))
            
            rButton = pygame.Rect(550, 450, 135, 50)
            rButton.center = (300,200)
            rButtonText = inputText.render("Random",False,(0,0,0))
        
            #logic for pressing buttons 
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos  # gets mouse position
                if sButton.collidepoint(mouse_pos):
                    # prints current location of mouse
                    saveFlag = True 
                    buttonsFlag = False
                    saveChoice = "Save"
                if nButton.collidepoint(mouse_pos):
                    # prints current location of mouse
                    noSaveFlag = True 
                    buttonsFlag = False
                    saveChoice = "No Save"
                if rButton.collidepoint(mouse_pos):
                    # prints current location of mouse
                    randomFlag = True
                    buttonsFlag = False
                    saveChoice = "Random"
        
            #Logic for typing par numbers
            if event.type == pygame.KEYDOWN:
            
                if event.type == pygame.QUIT or event.key==pygame.K_ESCAPE :
                        pygame.quit()
                
                if (pygame.K_0 <= event.key <= pygame.K_9):
                    number = chr(event.key)
                    parInput += number
                    
                
                if (pygame.K_a <= event.key <= pygame.K_z) or event.key == pygame.K_SPACE: # checks the key pressed
                    character = chr(event.key) #converts the number to a character
                    parInput += str(character) #adds the number to the end of the string
                                
                if event.key == pygame.K_BACKSPACE:
                    parInput = parInput[:-1]
                
                if event.key == pygame.K_RETURN and (saveFlag == True or noSaveFlag == True or randomFlag == True):
                    preLab = False
            
            #Change top info of pre-lab here
            parNum = inputText.render("Par Num: "+ parInput, False, (0 ,0 ,0 ))
            parInfo = titleFont.render('Please give participant number', False, (0, 0, 0))
            screen.fill(WHITE)
            
            #printing objects to screen (Pre-Lab)
            #Change LOCATION of buttons AND text here
            if (buttonsFlag == True):
                pygame.draw.rect(screen, BLUE,sButton)
                screen.blit(sButtonText,(65,200))
                pygame.draw.rect(screen, BLUE,nButton)
                screen.blit(nButtonText,(140,300))
                pygame.draw.rect(screen, BLUE,rButton)
                screen.blit(rButtonText,(240,200))
            elif(saveChoice != ""):
                choice = inputText.render(saveChoice, False, (0 ,0 ,0))
                screen.blit(choice,(150,175))
            
            screen.blit(parInfo,(260,0))
            screen.blit(parNum, (500,400))
            pygame.display.update()
            pygame.display.flip()
    

    participant = "p" + parInput + ".csv"
    
    
    #participantData = pd.read_csv(participant)
    
    try:
        participantData = pd.read_csv(participant)
        break
    except FileNotFoundError:
        newParFlag = True
        break

#instead of file handling this program has the passages here
        
experimentInput = 'experiment_input.csv'

instructionsRow = pd.read_csv(experimentInput,nrows = 0)
storyRow = pd.read_csv(experimentInput,nrows = 0,skiprows = [0,0])
questionsRow = pd.read_csv(experimentInput,nrows = 0,skiprows = [0,1])
answersRow = pd.read_csv(experimentInput,nrows = 0,skiprows = [0,1,2])
questions = []
trueAnswers = []

for index, question in enumerate(questionsRow.columns):
    if index == 0:
        continue 
    questions.append(question)
    trueAnswers.append(answersRow.columns[index])
#print(questions)
#print(answers)

story = storyRow.columns[1]

instructions = instructionsRow.columns[1]
#
# Instructions/Encoding phase of the experiment 
#

if (newParFlag == True):
    newPar = True
    readingInstructions = True
    readingBlurb = True
    
    recallSentences = []
    recallScore = []
    xy = [20,100] #for writing to the screen
    
    #location of the buttons/text on buttons
    bXY = [587, 463]
    doneXY = [577,463]
    bText = "OK"
    doneText = "DONE"
    
    while newPar:
        for event in pygame.event.get():
            
            #Experiment instructions 
            
            if readingInstructions == True:
            
                if event.type == pygame.KEYDOWN:
                
                    if event.type == pygame.QUIT or event.key==pygame.K_ESCAPE :
                            pygame.quit()
                            
                    if event.key == pygame.K_RETURN:
                        readingInstructions = False
                
                #printing objects to screen (Instructions)
                screen.fill(WHITE)
                message_display(font,textvars,BLACK,xy,95,instructions)
                pygame.display.update()
                pygame.display.flip()
        
            #Encoding phase 
            else:
                if readingBlurb == True:
                    
                    if event.type == pygame.KEYDOWN:
                    
                        if event.type == pygame.QUIT or event.key==pygame.K_ESCAPE :
                                pygame.quit()
                        
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        mouse_pos = event.pos
                            
                        if (mouse_pos[0] > 550 and mouse_pos[0] < 630) and (mouse_pos[1] > 460 and mouse_pos[1] < 510):
                            readingBlurb = False
                            
                            if (saveFlag == True):
                                saveOrNot = 1
#                                print("save choice")
                            if (noSaveFlag == True):
                                saveOrNot = 0
#                                print("no save choice")
                            if (randomFlag == True):
                                saveOrNot = (random.randint(0,1))
#                                print("random save choice")
    
                            if saveOrNot == 1:
                                #save file to local directory
                                save = open("story.txt", "w")
                                for line in story:
                                    save.write(line)
                                save.close()
                                
                                saved = True
                                savePopUp = True
                                popMsg = "!!! This file saved correctly, you will have access to it later. The recall task will need specific information from this story, so there is no need to rehearse. !!! "
                                while savePopUp:
                                    for event in pygame.event.get():
                                        
                                        
                                        if event.type == pygame.MOUSEBUTTONDOWN:
                                            mouse_pos = event.pos  # gets mouse position

                            
                                            # checks if mouse position is over the button  
                                            if (mouse_pos[0] > 550 and mouse_pos[0] < 630) and (mouse_pos[1] > 460 and mouse_pos[1] < 510):
                                                savePopUp = False
                                        
                                        if event.type == pygame.KEYDOWN:
                                            
                                            if event.type == pygame.QUIT or event.key==pygame.K_ESCAPE :
                                                    pygame.quit()
                                        
                                        #printing objects to screen (Successful saving msg)
                                        buttonText = font.render(bText, False,BLACK, (0,0,0))
                                        screen.fill(WHITE)
                                        message_display(errorFont,textvars,BLACK,xy,95,popMsg)
                                        buttonSave = pygame.draw.rect(screen, GREY,(550,450,100,50))
                                        buttonSave.move(600,height + 100)
                                        message_display(font,textvars,BLACK,bXY,95,bText)
                                        pygame.display.update()
                                        pygame.display.flip()
                                    
                            else:
                                noSavePopUp = True
                                popMsg = "!!! Sorry, this file failed to save. A future recall task will need specific information from the story so it is advised to rehearse information from the story. !!!"
                                while noSavePopUp:
                                    
                                    for event in pygame.event.get():
                                        
                                        if event.type == pygame.MOUSEBUTTONDOWN:
                                            mouse_pos = event.pos  # gets mouse position
#                                            print(mouse_pos)
                            
                                            # checks if mouse position is over the button                           
                                            if (mouse_pos[0] > 550 and mouse_pos[0] < 630) and (mouse_pos[1] > 460 and mouse_pos[1] < 510):
                                                noSavePopUp = False
                                        
                                        if event.type == pygame.KEYDOWN:
                                            if event.type == pygame.QUIT or event.key==pygame.K_ESCAPE :
                                                    pygame.quit()
                                    
                                        
                                        buttonText = font.render(bText, False,BLACK, (0,0,0))
                                        screen.fill(WHITE)
                                        
                                        #printing objects to screen (Failed to save msg)
                                        message_display(errorFont,textvars,BLACK,xy,95,popMsg)
                                        buttonNoSave = pygame.draw.rect(screen, GREY,(550,450,100,50))
                                        buttonNoSave.move(600,height + 100)
                                        message_display(font,textvars,BLACK,bXY,95,bText)
                                        pygame.display.update()
                                        pygame.display.flip()
                    
                    #printing objects to screen (Story Encoding)
                    if (readingBlurb == True):                
                        screen.fill(WHITE)
                        message_display(font,textvars,BLACK,xy,95,story)
                        buttonDone = pygame.draw.rect(screen, GREY,(550,450,100,50))
                        buttonDone.move(600,height + 100)
                        message_display(font,textvars,BLACK,doneXY,95,doneText)
                        pygame.display.update()
                        pygame.display.flip()
                        
                    if (readingBlurb == False):
                        delay = True
                        while delay:
                            for event in pygame.event.get():
                                
                                if event.type == pygame.KEYDOWN:
                                    if event.type == pygame.QUIT or event.key==pygame.K_ESCAPE :
                                        pygame.quit()
                                
                                
                                if event.type == pygame.MOUSEBUTTONDOWN:
                                    mouse_pos = event.pos  # gets mouse position
#                                    print(mouse_pos)
                            
                                    if (mouse_pos[0] > 550 and mouse_pos[0] < 630) and (mouse_pos[1] > 460 and mouse_pos[1] < 510):
                                        delay = False
                                
                                #printing objects to screen (Delay)
                                delayText = titleFont.render("Delay", False, (0,0,0))
                                screen.fill(WHITE)
                                delayButton = pygame.draw.rect(screen, GREY,(550,450,100,50))
                                delayButton.move(600,height - 100)
                                message_display(font,textvars,BLACK,bXY,95,doneText)
                                screen.blit(delayText,(550,75))
                                pygame.display.update()
                                pygame.display.flip()
                
                #Recall Phase 
                else:
                    recalling = True
                    memString = ""
                    word = ""
                    lineMult = 100
                    multLines = False
                    flag = False
                    line = []
                    xy = [20,200]
                    qXY = [10,80]
                    seed = random.randint(0,100)
                    random.Random(seed).shuffle(questions)
                    random.Random(seed).shuffle(trueAnswers)
                    answers = []
                    savedArr = []
                    qCount = 0
                    while recalling:
                        
                        for event in pygame.event.get():
                        
                            #print(len(memString))
                            
                            if event.type == pygame.KEYDOWN:
                                
                                if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key==pygame.K_ESCAPE :
                                    pygame.quit()
                                
                                if event.key == pygame.K_RETURN:
                                    qCount += 1
                                    if (qCount == len(questions)):
                                        recalling = False
                                        newPar = False
                                    answers.append(memString)
                                    if (saved == True):
                                        savedArr.append(1)
                                    else:
                                        savedArr.append(0)
                                    
                                    memString = ""
#                                    recalling = False
#                                    newPar = False
                                    
                                    recallSentences.append(memString)
                                    #score algo will go hear
                                    recallScore.append(0)
                                    
                                #answer typing logic 
                            
                                if (pygame.K_a <= event.key <= pygame.K_z) or event.key == pygame.K_SPACE: # checks the key pressed
                                    if (event.key == pygame.K_SPACE):
                                        #print(word)
                                        line.append(word)
                                        word = ""
                                    if pygame.key.get_mods() & pygame.KMOD_SHIFT:
                                            
                                        character = chr(event.key)
                                        character = character.upper()
                                        memString += str(character)
                                        word += str(character)
                                    else: 
                                        character = chr(event.key) #converts the number to a character
                                        memString += str(character) #adds the number to the end of the string
                                        word += str(character)
                                        
                                if pygame.K_0 <= event.key <= pygame.K_9: 
                                    character = chr(event.key) #converts the number to a character
                                    memString += str(character) #adds the number to the end of the string
                                    word += str(character)
                                
                                if(event.key == pygame.K_COMMA or event.key == pygame.K_PERIOD):
                                    character = chr(event.key)
                                    memString += str(character)
                                    word += str(character)
                                    
                                if(event.key == pygame.K_1 and pygame.key.get_mods() & pygame.KMOD_SHIFT):
                                            character = '!'
                                            memString += str(character)
                                            word += str(character)
                                            
                                if(event.key == pygame.K_SLASH and pygame.key.get_mods() & pygame.KMOD_SHIFT):
                                            character = '?'
                                            memString += str(character)
                                            word += str(character)
                                    
                                    
                                if event.key == pygame.K_BACKSPACE:
                                    memString = memString[:-1]
                                    word = word[:-1]
                                
                        #printing objects to screen (Answering Questions)
                        if (recalling == True):
                            recall = font.render(memString, False, (0 ,0 ,0 ))
                            screen.fill(WHITE)
                            message_display(inputText,textvars,BLACK,qXY,95,questions[qCount])
                            message_display(font,textvars,BLACK,xy,95,memString)
                            pygame.display.flip()

# saves experiment to a csv file 
    finalData = list(zip(questions,answers,trueAnswers,savedArr))
    s = pd.DataFrame(data = finalData, columns=['questions','answers','correct_answers','saved'])
    s.to_csv(participant, encoding='utf-8')
    print(s)

if newParFlag == False:
    print(participantData)
    pygame.quit()

pygame.quit()                
