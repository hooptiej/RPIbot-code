#!/usr/bin/python

from Adafruit_PWM_Servo_Driver import PWM
import time
import os
clear = lambda : os.system('tput reset')
import pygame
from pygame.locals import *
clock = pygame.time.Clock()
clear()
# Initialise the PWM device using the default address
pwm = PWM(0x40)
# Note if you'd like more debug output you can instead run:
#pwm = PWM(0x40, debug=True)

servoMin = 210  # Min pulse length out of 4096
servoCenter = 330 # math center
servoMax = 450  # Max pulse length out of 4096

def setServoPulse(channel, pulse):
    pulseLength = 1000000                   # 1,000,000 us per second
    pulseLength /= 60                       # 60 Hz
    print "%d us per period" % pulseLength
    pulseLength /= 4096                     # 12 bits of resolution
    print "%d us per bit" % pulseLength
    pulse *= 1000
    pulse /= pulseLength
    pwm.setPWM(channel, 0, pulse)

pwm.setPWMFreq(60)                        # Set frequency to 60 Hz
print " "
print "Biped Test Control center V.a"
print " "
time.sleep(1)
#clear()
print " "
print "checking for joysick"
pygame.init()
pygame.joystick.init()
stickname = 0
stickname = (pygame.joystick.Joystick(0).get_name())
if stickname == 0:
    print "..."
else:
    print " "
    print "Joystick detected"
    time.sleep(1)
    #clear()
    print " "
    print stickname + " was Detected"
    pygame.joystick.Joystick(0).init()
    time.sleep(1)
    print " "
    print (pygame.joystick.Joystick(0).get_numbuttons())
    print "buttons total"
    print (pygame.joystick.Joystick(0).get_numaxes())
    print "number of axes"
    print (pygame.joystick.Joystick(0).get_numhats())
    print "Hats or D-Pads"
    print " "
    # print "Returning to main menu in 5 seconds"
    print " "
    time.sleep(2)
    loop = 1
    while loop > 0:
        #clear()
        for event in pygame.event.get(): # User did something
            if event.type == pygame.JOYBUTTONDOWN:
                print("Joystick button pressed.")
                button = str(pygame.joystick.Joystick(0).get_button(0))
                button = str(pygame.joystick.Joystick(0).get_button(1))
                button = str(pygame.joystick.Joystick(0).get_button(2))
                button = str(pygame.joystick.Joystick(0).get_button(3))
                button = str(pygame.joystick.Joystick(0).get_button(4))
                button = str(pygame.joystick.Joystick(0).get_button(5))
                button = str(pygame.joystick.Joystick(0).get_button(6))
                button = str(pygame.joystick.Joystick(0).get_button(7))
                button = str(pygame.joystick.Joystick(0).get_button(8))
                button = str(pygame.joystick.Joystick(0).get_button(9))
                button = str(pygame.joystick.Joystick(0).get_button(10))
                button = str(pygame.joystick.Joystick(0).get_button(11))
            if event.type == pygame.JOYBUTTONUP:
                print("Joystick button released.")
            if event.type == pygame.JOYAXISMOTION:
                joyaxeone = str(pygame.joystick.Joystick(0).get_axis(0))
                print (joyaxeone)
                joyaxetwo = str(pygame.joystick.Joystick(0).get_axis(1))
                joyaxethree = str(pygame.joystick.Joystick(0).get_axis(2))
                joyaxefour = str(pygame.joystick.Joystick(0).get_axis(3))
                print("Stick moving.")
            if event.type == pygame.JOYHATMOTION:
                print("D-Pad Moving.")
                hat = str(pygame.joystick.Joystick(0).get_hat(0))