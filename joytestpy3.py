import pygame
from pygame.locals import *
import time
import os

pygame.init()
# Set up the joystick
pygame.joystick.init()
stickname = 0
stickname = (pygame.joystick.Joystick(0).get_name())
if stickname == 0:
    print ("stuff here")
else:
    print ("Joystick detected")
    time.sleep(1)
    print (stickname + " was Detected")
    print (" ")
    pygame.joystick.Joystick(0).init()
    butnum = str(pygame.joystick.Joystick(0).get_numbuttons())
    print (butnum + " buttons total")
    print (" ")
    axnum = str(pygame.joystick.Joystick(0).get_numaxes())
    print  (axnum + " Analog axes")
    print (" ")
    hatnum = str(pygame.joystick.Joystick(0).get_numhats())
    print (hatnum + " Hat(s) or D-Pad(s) ")
    print (" ")
    print ("Joypad Ready")
    time.sleep(5)