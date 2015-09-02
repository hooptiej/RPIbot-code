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

# set servo channels
lankle = 15
rankle = 0

lfoot = 13
rfoot = 2

lhip = 11
rhip = 4

rwaist = 9
lwaist = 6

ranklepos = servoCenter
lanklepos = servoCenter
rfootpos = servoCenter
lfootpos = servoCenter
rwaistpos = servoCenter
lwaistpos = servoCenter
rhippos = servoCenter
lhippos = servoCenter


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
print "Biped Test Control center V.a2"
print " "
print "Centering Servos"



choice = 0
loop = 1
choicetwo = 0 
choicejoytest = 0
while loop == 1:
    #center servos
    pwm.setPWM(lwaist, 0, lwaistpos)
    pwm.setPWM(rwaist, 0, rwaistpos)
    pwm.setPWM(lfoot, 0, lfootpos)
    pwm.setPWM(rfoot, 0, rfootpos)
    pwm.setPWM(lankle, 0, lanklepos)
    pwm.setPWM(rankle, 0, ranklepos)
    pwm.setPWM(lhip, 0, lhippos)
    pwm.setPWM(rhip, 0, rhippos)
    #print what options you have
    print " select a joint to move"
    print " 1. Left Foot"
    print " Position = ",lfootpos
    print " 2. Left Ankle"
    print " 3. Left Hip"
    print " 4. Left Waist"
    print " 0. to quit"
    choice = input("Press a Number Now")
    if choice == 0:
        loop = 0
    if choice == 1:
        print "servo Center is"
        print (servoCenter)
        choicetwo = int(input("Enter Position Number Now (210-450)"))
        lfootpos = choicetwo
        