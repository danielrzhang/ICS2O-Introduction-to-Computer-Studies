############################################################
# File Name: HouseCode.py                                  #
# Description: Code for the house and animations summative #
# Author: Daniel Zhang                                     #
# Date: 10/28/2019                                         #
############################################################
from math import pi
from random import randint


import pygame
import sys

pygame.init()

# Variables
width = 800
height = 600
gameWindow = pygame.display.set_mode((width, height))
white = (255, 255, 255)
black = (30, 30, 30)
lightBlack = (49, 51, 33)
green = (0, 210, 50)
forestGreen = (34, 139, 34)
frontRed = (245, 0, 0)
backRed = (150, 0, 0)
windowBlue = (30, 144, 255)
doorBrown = (139, 69, 19)
knobYellow = (255, 215, 0)
sunYellow = (255, 255, 0)
truckSilver = (192, 192, 192)
shadowGray = (10, 65, 100)
smokeGray = (195, 195, 195)
cloudWhite = (240, 240, 240)
cloudX1 = randint(100, 250)
cloudY1 = randint(50, 300)
cloudX2 = randint(300, 450)
cloudY2 = randint(50, 300)
cloudX3 = randint(500, 650)
cloudY3 = randint(50, 300)
deg360 = 2 * pi
deg180 = pi
font = pygame.font.SysFont("Times New Roman", 20)

def createWindows(x, y, width, height):
    pygame.draw.rect(gameWindow, windowBlue, (x, y, width, height), 0)
    pygame.draw.line(gameWindow, black, (x, y + (round(height / 2))), (x + width, y + (round(height / 2))), round(height / 12))
    pygame.draw.line(gameWindow, black, (x + (round(width / 2)), y), (x + (round(width / 2)), y + height), round(width / 12))
    pygame.draw.rect(gameWindow, windowBlue, (x + 160, y, width, height), 0)
    pygame.draw.line(gameWindow, black, (x + 160, y + (round(height / 2))), ((x + 160 + width), y + (round(height / 2))), round(height / 12))
    pygame.draw.line(gameWindow, black, ((x + 160) + (round(width / 2)), y), ((x + 160) + (round(width / 2)), y + height), round(width / 12))
    pygame.draw.rect(gameWindow, windowBlue, (x, y + 125, width, height), 0)
    pygame.draw.line(gameWindow, black, (x, (y + 125) + (round(height / 2))), (x + width, (y + 125) + (round(height / 2))), round(height / 12))
    pygame.draw.line(gameWindow, black, (x + (round(height / 2)), y + 125), (x + round(height / 2), y + 125 + height), round(width / 12))
    pygame.draw.rect(gameWindow, windowBlue, (x + 160, y + 125, width, height), 0)
    pygame.draw.line(gameWindow, black, (x + 160, (y + 125) + (round(height / 2))), (x + 160 + width, (y + 125) + (round(height / 2))), round(height / 12))
    pygame.draw.line(gameWindow, black, ((x + 160) + (round(width / 2)), y + 125), ((x + 160) + (round(width / 2)), y + 125 + width), round(width / 12))

def createClouds():
    pygame.draw.ellipse(gameWindow, cloudWhite, (cloudX1, cloudY1, 80, 80), 0)
    pygame.draw.ellipse(gameWindow, cloudWhite, (cloudX1 + 100, cloudY1, 80, 80), 0)
    pygame.draw.ellipse(gameWindow, cloudWhite, (cloudX1 + 30, cloudY1 - 35, 125, 125), 0)
    pygame.draw.ellipse(gameWindow, cloudWhite, (cloudX2, cloudY2, 80, 80), 0)
    pygame.draw.ellipse(gameWindow, cloudWhite, (cloudX2 + 100, cloudY2, 80, 80), 0)
    pygame.draw.ellipse(gameWindow, cloudWhite, (cloudX2 + 30, cloudY2 - 35, 125, 125), 0)
    pygame.draw.ellipse(gameWindow, cloudWhite, (cloudX3, cloudY3, 80, 80), 0)
    pygame.draw.ellipse(gameWindow, cloudWhite, (cloudX3 + 100, cloudY3, 80, 80), 0)
    pygame.draw.ellipse(gameWindow, cloudWhite, (cloudX3 + 30, cloudY3 - 35, 125, 125), 0)
    
# Animation variables
generalShift = 1
originalSkyG = 100
originalSkyB = 175
skyBlue = (0, originalSkyG, originalSkyB)
skyChangeG = 10
skyChangeB = 5
sunX = -50
sunY = 200
moonX = -50
moonY = 200

skyColourR = 255
skyColourG = 100
skyColourB = 70

skyColour = (skyColourR, skyColourG, skyColourB)

houseShadowX1 = 700
houseShadowX2 = 750
houseShadowX3 = 690
houseShadowY3 = 590
houseShadowX4 = 675

treeShadowLeafX1 = 135
treeShadowLeafX2 = 105
treeShadowLeafX3 = 220
treeTrunkShadowX1 = 230
treeTrunkShadowX2 = 175

truckShadowBodyX1 = 1000
truckShadowBodyX2 = 700
truckShadowWindowX1 = 740 
truckShadowWindowX2 = 830
truckShadowWindowX3 = 875
truckShadowWindowX4 = 820

randomCloudX = randint(100, 700) 
randomCloudY = randint(100, 200)
 
## Main Program ##

while True:
    # Sunrise, Day, Sunset, and Night Sequence
    pygame.event.clear()
    pygame.time.delay(10)
    pygame.draw.rect(gameWindow, skyColour, (0, 0, 800, 600), 0) # Sky
    pygame.draw.rect(gameWindow, green, (0, 400, 800, 200), 0) # Grass
    if (sunX < 200) and (moonX == -50): # Sunrise -> Sky Blue Day
        skyColourR -= generalShift * 0.84
        skyColourG -= generalShift * 0.06
        skyColourB += generalShift * 0.66
        skyColour = (skyColourR, skyColourG, skyColourB)
    elif (sunX < 750) and (moonX == -50): # Sky Blue Day
        skyColour = (skyColourR, skyColourG, skyColourB)
    elif (sunX < 850) and (moonX == -50): # Sky Blue Day -> Sunset
        skyColourR += generalShift * 2.1
        skyColourG += generalShift * 0.7
        skyColourB -= generalShift * 2.35
        skyColour = (skyColourR, skyColourG, skyColourB)
    elif (sunX == 850) and (moonX < 50):
        skyColourR -= generalShift * 2.5
        if skyColourR < 0:
            skyColourR = 0
        skyColourG -= generalShift * 1.6
        if skyColourG < 0:
            skyColourG = 0
        if skyColourB < 0:
            skyColourB = 0
        skyColourB = skyColourB
        skyColour = (skyColourR, skyColourG, skyColourB)
    elif (sunX == 850) and (moonX < 750): # Sunset -> Night 
        skyColour = (skyColourR, skyColourG, skyColourB)
    elif (sunX == 850) and (moonX < 850): # Night -> Sunrise
        skyColourR += generalShift * 2.55
        if skyColourR > 255:
            skyColourR = 255
        skyColourG += generalShift
        skyColourB += generalShift * 0.7
        skyColour = (skyColourR, skyColourG, skyColourB)
        
    # Sun and Moon Paths
    pygame.draw.circle(gameWindow, sunYellow, (sunX, round(sunY)), 50 , 0)
    pygame.draw.circle(gameWindow, white, (moonX, round(moonY)), 35, 0)
    if (sunX < 850) and (moonX < 850):
        sunX += generalShift
        sunY = 0.002 * ((sunX - 400) ** 2) - 20
    elif (sunX >= 850) and (moonX < 850):
        moonX += generalShift
        moonY = 0.002 * ((moonX - 400) ** 2) - 20
    else:
        sunX = -50
        sunY = 100
        moonX = -50
        moonY = 100
        sunX += generalShift
        sunY = 0.002 * ((sunX - 400) ** 2) - 20

    # House Shadow
    pygame.draw.polygon(gameWindow, shadowGray, ((600, 450), (houseShadowX1, 520), (houseShadowX2, 590), (houseShadowX3, houseShadowY3), (houseShadowX4, 590), (250, 500)), 0)
    if (-50 < sunX < 850) and (moonX == -50):
        houseShadowX1 -= generalShift * 0.195
        houseShadowX2 -= generalShift * 0.4
        houseShadowX3 -= generalShift * 0.5
        houseShadowY3 += generalShift * 0.04
        houseShadowX4 -= generalShift * 0.65
    elif (sunX == 850) and (moonX == -50):
        houseShadowX1 = 700
        houseShadowX2 = 750
        houseShadowX3 = 690
        houseShadowY3 = 590
        houseShadowX4 = 675
    elif (sunX == 850) and (-50 < moonX < 850):
        houseShadowX1 -= generalShift * 0.195
        houseShadowX2 -= generalShift * 0.4
        houseShadowX3 -= generalShift * 0.5
        houseShadowY3 += generalShift * 0.04
        houseShadowX4 -= generalShift * 0.65
    else:
        houseShadowX1 = 700
        houseShadowX2 = 750
        houseShadowX3 = 690
        houseShadowY3 = 590
        houseShadowX4 = 675
    
    # Tree Shadow
    pygame.draw.ellipse(gameWindow, shadowGray, (treeShadowLeafX1, 475, 160, 160), 0)
    pygame.draw.ellipse(gameWindow, shadowGray, (treeShadowLeafX2, 490, 100, 100), 0)
    pygame.draw.ellipse(gameWindow, shadowGray, (treeShadowLeafX3, 490, 100, 100), 0)
    pygame.draw.polygon(gameWindow, shadowGray, ((100, 450), (150, 450), (treeTrunkShadowX1, 500), (treeTrunkShadowX2, 500)), 0)
    if (-50 < sunX < 850) and (moonX == -50):
        treeShadowLeafX1 -= generalShift * 0.25
        treeShadowLeafX2 -= generalShift * 0.25
        treeShadowLeafX3 -= generalShift * 0.25
        treeTrunkShadowX1 -= generalShift * 0.25
        treeTrunkShadowX2 -= generalShift * 0.25
    elif (sunX == 850) and (moonX == -50):
        treeShadowLeafX1 = 135
        treeShadowLeafX2 = 105
        treeShadowLeafX3 = 220
        treeTrunkShadowX1 = 230
        treeTrunkShadowX2 = 175
    elif (sunX == 850) and (-50 < moonX < 850):
        treeShadowLeafX1 -= generalShift * 0.25
        treeShadowLeafX2 -= generalShift * 0.25
        treeShadowLeafX3 -= generalShift * 0.25
        treeTrunkShadowX1 -= generalShift * 0.25
        treeTrunkShadowX2 -= generalShift * 0.25
    else:
        treeShadowLeafX1 = 135
        treeShadowLeafX2 = 105
        treeShadowLeafX3 = 220
        treeTrunkShadowX1 = 230
        treeTrunkShadowX2 = 175

    # Truck Shadow
    pygame.draw.circle(gameWindow, shadowGray, (665, 505), 22, 0)
    pygame.draw.circle(gameWindow, shadowGray, (810, 505), 22, 0)
    pygame.draw.polygon(gameWindow, shadowGray, ((625, 505), (810, 505), (truckShadowBodyX1, 550), (truckShadowBodyX2, 550)), 0)
    pygame.draw.polygon(gameWindow, shadowGray, ((truckShadowWindowX1, 550), (truckShadowWindowX2, 550), (truckShadowWindowX3, 580), (truckShadowWindowX4, 580)), 0)
    if (-50 < sunX < 850) and (moonX == -50):
        truckShadowBodyX1 -= generalShift * 0.15
        truckShadowBodyX2 -= generalShift * 0.15
        truckShadowWindowX1 -= generalShift * 0.14
        truckShadowWindowX2 -= generalShift * 0.1
        truckShadowWindowX3 -= generalShift * 0.18
        truckShadowWindowX4 -= generalShift * 0.18
    elif (sunX == 850) and (moonX == -50):
        truckShadowBodyX1 = 1000
        truckShadowBodyX2 = 700
        truckShadowWindowX1 = 740 
        truckShadowWindowX2 = 830
        truckShadowWindowX3 = 875
        truckShadowWindowX4 = 820
    elif (sunX == 850) and (-50 < moonX < 850):
        truckShadowBodyX1 -= generalShift * 0.15
        truckShadowBodyX2 -= generalShift * 0.15
        truckShadowWindowX1 -= generalShift * 0.14
        truckShadowWindowX2 -= generalShift * 0.1
        truckShadowWindowX3 -= generalShift * 0.18
        truckShadowWindowX4 -= generalShift * 0.18
    else:
        truckShadowBodyX1 = 1000
        truckShadowBodyX2 = 700
        truckShadowWindowX1 = 740 
        truckShadowWindowX2 = 830
        truckShadowWindowX3 = 875
        truckShadowWindowX4 = 820

    # Clouds
    createClouds()
    if (cloudX1 < 1000) and (cloudX2 < 1000) and (cloudX3 < 1000):
        cloudX1 += generalShift * 0.5
        cloudX2 += generalShift * 0.7
        cloudX3 += generalShift * 0.9
    elif (cloudX1 >= 1000) and (cloudX2 < 1000) and (cloudX3 < 1000):
        cloudX1 = -200
        cloudX1 += generalShift * 0.5
        cloudX2 += generalShift * 0.7
        cloudX3 += generalShift * 0.9
    elif (cloudX1 < 1000) and (cloudX2 >= 1000) and (cloudX3 < 1000):
        cloudX1 += generalShift * 0.5
        cloudX2 = -200
        cloudX2 += generalShift * 0.7
        cloudX3 += generalShift * 0.9
    elif (cloudX1 < 1000) and (cloudX2 < 1000) and (cloudX3 >= 1000):
        cloudX1 += generalShift * 0.5
        cloudX2 += generalShift * 0.7
        cloudX3 = -200
        cloudX3 += generalShift * 0.9

    # House 
    pygame.draw.rect(gameWindow, frontRed, (250, 200, 300, 300), 0) # Front house wall
    pygame.draw.polygon(gameWindow, backRed, ((550, 200), (600, 200), (600, 450), (550, 500)), 0) # Side of house
    pygame.draw.polygon(gameWindow, lightBlack, ((250, 200), (550, 200), (450, 50)), 0) # Front roof
    pygame.draw.polygon(gameWindow, black, ((450, 50), (550, 200), (600, 200)), 0) # Side roof
    pygame.draw.rect(gameWindow, doorBrown, (370, 395, 60, 105), 0) # Door
    pygame.draw.ellipse(gameWindow, knobYellow, (410, 440, 10, 10), 0) # Door knob

    # Tree
    pygame.draw.rect(gameWindow, doorBrown, (100, 300, 50, 150), 0)
    pygame.draw.circle(gameWindow, forestGreen, (125, 270), 90, 0)
    pygame.draw.circle(gameWindow, forestGreen, (65, 290), 60, 0)
    pygame.draw.circle(gameWindow, forestGreen, (185, 290), 60, 0)

    # Truck Roof layering
    for hoodLayers in range(689, 711, 1):
        pygame.draw.arc(gameWindow, truckSilver, (hoodLayers, 340, 40, 30), deg360, deg180, 15)
        
    # Silver Truck
    pygame.draw.polygon(gameWindow, truckSilver, ((690, 350), (665, 450), (750, 450), (750, 350)), 0)
    pygame.draw.rect(gameWindow, truckSilver, (625, 405, 200, 55), 0)
    pygame.draw.circle(gameWindow, black, (665, 460), 25, 0)
    pygame.draw.circle(gameWindow, black, (810, 460), 25, 0)
    pygame.draw.circle(gameWindow, smokeGray, (665, 460), 15, 0)
    pygame.draw.circle(gameWindow, smokeGray, (810, 460), 15, 0)
    pygame.draw.polygon(gameWindow, windowBlue, ((700, 355), (740, 355), (740, 400), (690, 400)), 0)
    pygame.draw.rect(gameWindow, black, (720, 415, 20, 6), 0)
    pygame.draw.line(gameWindow, black, (750, 405), (750, 460), 3)
    pygame.draw.rect(gameWindow, sunYellow, (625, 415, 10, 25), 0)
          
    # Smoke
    for smoke in range(-10, 100, 20):
        pygame.draw.circle(gameWindow, smokeGray, (350, smoke), 25, 0)
    
    pygame.draw.rect(gameWindow, frontRed, (325, 70, 40, 90), 0) # Front Chimney
    pygame.draw.polygon(gameWindow, backRed, ((365, 70), (375, 80), (375, 150), (365, 160)), 0) # Side Chimney   

    # Loop vertical fence posts
    for fencePosts in range(15, 800, 50):
        pygame.draw.rect(gameWindow, white, (fencePosts, 520, 15, 200), 0)
    pygame.draw.rect(gameWindow, white, (0, 540, 800, 10), 0) # Fence bar
    
    # Text
    if (sunX < 850) and (moonX == -50):
        display = font.render("My House" , 10, black)
        gameWindow.blit(display, (10, 10))
    elif (sunX == 850) and (moonX < 850):
        display = font.render("My House", 10, white)
        gameWindow.blit(display, (10, 10))
    
    # Window Function Call
    createWindows(290, 250, 60, 60)

    pygame.display.update()
