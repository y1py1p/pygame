#-----------------------------------------------------------------------------
# Name:        Pixerlator 9001
# Purpose:     A fun memory game that tests how fast and how long you can remember the pattern of a 5x5 drawing,
#              as well as the ability to create your own, mini pixel art.
#
# Author:      Yana Petcheva
# Created:     05-06-23
# Updated:     06-06-23
#-----------------------------------------------------------------------------
import pygame
import random
import os
import os.path

'''
This class controls each individual rectangle on the grid
'''

class Pixel:
    def __init__(self, x, y, colour):
        '''
        This function controls each individual rectangle on the grid by assigning it an x and y value,
        and a colour, all attributes of the pixel self
        Parameters
        ----------
        self, x, y , colour
                
        Returns
        -------
        None
        '''

        self.colour = colour
        self.rect = pygame.Rect(x, y, 126, 126)

    def draw(self, surface):
        pygame.draw.rect(surface, self.colour, self.rect)
        '''
        This function controls each individual rectangle on the grid by drawing it with the given x and y and colour
        Parameters
        ----------
        self, surface
                
        Returns
        -------
        None
        '''
    def changeColour(self, newColour, pos):
        if self.rect.collidepoint(pos):
            self.colour = newColour
        '''
        This function controls the changing on the indiviudal rects colour depending on the collision with mouse(pos)
        Parameters
        ----------
        self, newColour, pos
                
        Returns
        -------
        None
        '''
    def setColour(self, newColour):
        self.colour = newColour
        '''
        This function controls the changes the active indiviudal rects colour 
        Parameters
        ----------
        self, newColour
                
        Returns
        -------
        None
        '''
    def getColour(self):
        return self.colour
        '''
        This function returns the changed indiviudal rects colour 
        Parameters
        ----------
        self
                
        Returns
        -------
        None
        '''
'''
This class controls the colours of squares in the toolbar
'''
class Colour:
    def __init__(self, x, y, colour):
        self.colour = colour
        self.rect = pygame.Rect(x, y, 50, 50)
        '''
        This function sets the x,y and colour for the squares in the toolbar used for colouring
        Parameters
        ----------
        self, x, y, colour
                
        Returns
        -------
        None
        '''
    def draw(self, surface):
        pygame.draw.rect(surface, self.colour, self.rect)
        '''
        This function draws the squares in the toolbar
        Parameters
        ----------
        self, surface
                
        Returns
        -------
        None
        '''
    def colided(self, pos):
        if self.rect.collidepoint(pos):
            return True
        else:
            return False
        '''
        This function checks if the mouse(pos) has collided with one of the colours in the toolbar
        Parameters
        ----------
        self, pos
                
        Returns
        -------
        True or False
        '''
    def getColour(self):
        return self.colour
        '''
        This function returns colour in which the mouse has collided with 
        Parameters
        ----------
        self
                
        Returns
        -------
        colour
        '''
def setRandomColours(pixels, colours):
    correct = []
    for i in pixels:
        colour = random.choice(colours)
        i.setColour(colour)
        correct.append(colour)
    return correct
    '''
    This function makes the pattern for the minigame, saving both the correct code used later for checking if the
    drawing is correct but also randomizing from the list of colours to set the colour of the squares in the grid
    Parameters
    ----------
    pixels, colours
            
    Returns
    -------
    correct
    '''
#     The Game
def main():
    gameState = -1
    timer = 0
    pygame.init()
    pygame.font.init()
    my_font = pygame.font.SysFont('Comic Sans MS', 30)
    surfaceSize = 640
    frameRate = 1000
    mainSurface = pygame.display.set_mode((surfaceSize, 740))
#     Each code for the colours
    blue = (66, 135, 245)
    purple = (133, 20, 181)
    clock = pygame.time.Clock()  
    green = (22, 179, 14)
    yellow = (232, 225, 23)
    orange = (247, 148, 17)
    red = (217, 48, 22)
    brown= (92, 55, 6)
    black = (0, 0, 0)
    bar = (212, 188, 230)
    white = (255, 255, 255)
    pygame.mouse.set_visible(True) 
    colour = [red, orange, yellow, green, blue, purple, brown, white]
    colours = []
    background = pygame.image.load('image/background.png')
    background1 = pygame.image.load('image/background1.png')
    background2 = pygame.image.load('image/background2.png')
    paintbrush = pygame.image.load('image/paintbrush.png')
    mute = pygame.image.load('image/pressmute.png')
    reload = pygame.image.load('image/reload.png')
    correct = []
    for i in range(len(colour)):
        colours.append(Colour(11+i*71, 25, colour[i]))
    currentColour = white
    boxes = []
    pixels = []
    music = 1
#     Positions for the pixels
    for i in (96, 225, 353, 483, 613):
        for j in (2, 131, 260, 389, 518):
            boxes.append([(j, i), (126, 126)])
            pixels.append(Pixel(j, i, white))
            
    grid = pygame.image.load('image/grid5x5.png')
    check = pygame.image.load('image/check.png')
#     Checks if Music File exists
    path = './music.txt'
    checkFile = os.path.isfile(path)
    while True:
#         Music Control
        keys = pygame.key.get_pressed()
        if keys[pygame.K_m]:
            music = 0
            if music == 0:
                filew = open('music.txt', 'w')
                filew.write(f'{music}')
                filew.close()
        if keys[pygame.K_e]:
            music = 1
            if music == 1:
                filew = open('music.txt', 'w')
                filew.write(f'{music}')
                filew.close()
#         Music
        if gameState == -1:
            if checkFile == True:
                filer = open('music.txt', 'r')
                valuemusic = int(filer.readline())
                pygame.mixer.music.load("music/musicgame.mp3")
                pygame.mixer.music.set_volume(0.1*valuemusic)
                pygame.mixer.music.play(-1, 0.0)
            else:
                pygame.mixer.music.set_volume(0.1)
                # pygame.mixer.music.play(-1, 0.0)
            gameState = 0
        pos = (pygame.mouse.get_pos())
        ev = pygame.event.poll()    
        if ev.type == pygame.QUIT:  
            break
        if(gameState == 0):
            pygame.mouse.set_visible(True) 
            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_ESCAPE:
                    break
            mainSurface.fill((255, 255, 255))
            mainSurface.blit(background, (0,-50))
            mainSurface.blit(mute, (10,0))
            mainSurface.blit(reload, (110,50))
            if(ev.type == pygame.MOUSEBUTTONDOWN):
#                 Home Screen Buttons
                pos = (pygame.mouse.get_pos())
                if(pos[0] >= 200) and (pos[0] <= 440) and (pos[1] >= 340) and (pos[1] <= 390):
                    correct = setRandomColours(pixels, colour)
                    currentSeconds = 10
                    pygame.time.set_timer(pygame.USEREVENT, 1000)
                    gameState = 2
                if(pos[0] >= 200) and (pos[0] <= 440) and (pos[1] >= 455) and (pos[1] <= 505):
                    for i in pixels:
                        i.setColour(white)
                        currentColour = white
                        gameState = 3
                if(pos[0] >= 150) and (pos[0] <= 490) and (pos[1] >= 570) and (pos[1] <= 620):
                    for i in pixels:
                        i.setColour(white)
                        gameState = 4
#                         MiniGame Drawing Function
        if(gameState == 1):
            pygame.mouse.set_visible(False) 
            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_ESCAPE:
                    break
            mainSurface.fill((255, 255, 255))
            mainSurface.blit(grid, (-43,60))
            pygame.draw.rect(mainSurface, (bar), ((0, 0), (640, 94)))
            for i in colours:
                i.draw(mainSurface)
            

            for i in pixels:
                i.draw(mainSurface)

            if(ev.type == pygame.MOUSEBUTTONDOWN):
                for i in colours:
                    if(i.colided(pos)):
                        currentColour = i.getColour()

                for i in pixels:
                    i.changeColour(currentColour, pos)
            mainSurface.blit(check, (570, 30))
            if(ev.type == pygame.MOUSEBUTTONDOWN):
                if(pos[0] >= 570) and (pos[0] <= 625) and (pos[1] >= 26) and (pos[1] <= 71):
                    gameState = 5
            mainSurface.blit(paintbrush, (pos[0],pos[1]))
#             MiniGame Randomized Memorizing Screen
        if gameState == 2:
            pygame.mouse.set_visible(True) 
            if ev.type == pygame.USEREVENT:
                currentSeconds -= 1
                if currentSeconds == 0:
                    gameState = 1
                    pygame.time.set_timer(pygame.USEREVENT, 0)
                    for i in pixels:
                        i.setColour(white)
                        
            mainSurface.fill((255, 255, 255))
            mainSurface.blit(grid, (-43,60))
            pygame.draw.rect(mainSurface, (bar), ((0, 0), (640, 94)))
            countdown = my_font.render('Time left: {0}'.format(currentSeconds), True, (0, 0, 0))
            mainSurface.blit(countdown, (0, 0))
            for i in pixels:
                i.draw(mainSurface)
#                 Drawing Screen
        if gameState == 3:
            pygame.mouse.set_visible(False) 
            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_ESCAPE:
                    break
            mainSurface.fill((255, 255, 255))
            mainSurface.blit(grid, (-43,60))
            pygame.draw.rect(mainSurface, (bar), ((0, 0), (640, 94)))
            for i in colours:
                i.draw(mainSurface)
            for i in pixels:
                i.draw(mainSurface)
            if(ev.type == pygame.MOUSEBUTTONDOWN):
                for i in colours:
                    if(i.colided(pos)):
                        currentColour = i.getColour()
                for i in pixels:
                    i.changeColour(currentColour, pos)
#                     Save Picture Function(Writing a file)
            if keys[pygame.K_a]:
                pygame.image.save(mainSurface, ("drawing.jpg"))
            mainSurface.blit(check, (570, 30))
            if(ev.type == pygame.MOUSEBUTTONDOWN):
                if(pos[0] >= 570) and (pos[0] <= 625) and (pos[1] >= 26) and (pos[1] <= 71):
                    gameState = 0
            mainSurface.blit(paintbrush, (pos[0],pos[1]))
#             How To Play Screen
        if gameState == 4:
            pygame.mouse.set_visible(True)
            mainSurface.fill((255, 255, 255))
            mainSurface.blit(background2, (-5, 0))
            if(ev.type == pygame.MOUSEBUTTONDOWN):
                if(pos[0] >= 230) and (pos[0] <= 420) and (pos[1] >= 650) and (pos[1] <= 710):
                    gameState = 0
#                     Win/Loss screen for minigame
        if gameState == 5:
            pygame.mouse.set_visible(True)
            mainSurface.fill((255, 255, 255))
            mainSurface.blit(background1, (-5, 0))
            pixelColours = [i.getColour() for i in pixels]
            if pixelColours == correct:
                win = my_font.render('Congrats! You got them all right!'.format(currentSeconds), True, (0, 0, 0))
                mainSurface.blit(win, (100, 200))
            numCorrect = 0
            for i in range(25):
                if correct[i] == pixelColours[i]:
                    numCorrect += 1
                    finalScore = numCorrect*4
            percent = my_font.render(f'{finalScore}'.format(currentSeconds), True, (0, 0, 0))
            mainSurface.blit(percent, (310, 470))
            if(ev.type == pygame.MOUSEBUTTONDOWN):
                if(pos[0] >= 250) and (pos[0] <= 410) and (pos[1] >= 605) and (pos[1] <= 665):
                    gameState = 0
        pygame.display.flip()
        clock.tick(frameRate)

    pygame.quit() 

main()
