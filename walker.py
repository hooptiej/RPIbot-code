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
la = 15
ra = 0

lf = 13
rf = 2

lh = 11
rh = 4

rw = 6
lw = 9

lfpos = 325      #1
rfpos = 300      #5


lapos = 210     #2
rapos = 410     #6


lhpos = 350       #3
rhpos = 350       #7


lwpos = 340     #4
rwpos = 350     #8


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
time.sleep(1)

#center servos
pwm.setPWM(lw, 0, lwpos)
pwm.setPWM(rw, 0, rwpos)
pwm.setPWM(lf, 0, lfpos)
pwm.setPWM(rf, 0, rfpos)
pwm.setPWM(la, 0, lapos)
pwm.setPWM(ra, 0, rapos)
pwm.setPWM(lh, 0, lhpos)
pwm.setPWM(rh, 0, rhpos)

choice = 0
loop = 1
choicetwo = 0 
while loop == 1:
    #print what options you have
    clear()
    print " select a joint to move"
    print " 1. Left Foot"
    print " Position = ",lfpos
    print " 2. Left Ankle"
    print " Position = ",lapos
    print " 3. Left Hip"
    print " Position = ",lhpos
    print " 4. Left Waist"
    print " Position = ",lwpos
    print " 5. Right Foot"
    print " Position = ",rfpos
    print " 6. Right Ankle"
    print " Position = ",rapos
    print " 7. Right Hip"
    print " Position = ",rhpos
    print " 8. Right Waist"
    print " Position = ",rwpos
    print " 0. for chorded test"
    print " Press Q to Quit"
    choice = input("Press a Number Now : ")
    if choice == Q:
        loop = 0
    elif choice == 1:
        #Left foot
        choicetwo = int(input("Enter Position Number Now (210-450)"))
        dist = choicetwo - lfpos
        print "traveling ",dist
        if dist < 0:
            dist = dist * -1
            while dist > 0:
                lfpos = lfpos - 1
                pwm.setPWM(lf, 0, lfpos)
                dist = dist - 1
                time.sleep(.005)
        elif dist > 0:
            while dist > 0:
                lfpos = lfpos + 1
                pwm.setPWM(lf, 0, lfpos)
                dist = dist - 1
                time.sleep(.005)
        
    elif choice == 2:
        #Left ankle
        choicetwo = int(input("Enter Position Number Now (210-450)"))
        dist = choicetwo - lapos
        print "traveling ",dist
        if dist < 0:
            dist = dist * -1
            while dist > 0:
                lapos = lapos - 1
                pwm.setPWM(la, 0, lapos)
                dist = dist - 1
                time.sleep(.005)
        elif dist > 0:
            while dist > 0:
                lapos = lapos + 1
                pwm.setPWM(la, 0, lapos)
                dist = dist - 1
                time.sleep(.005)
    elif choice == 3:
        #Left hip
        choicetwo = int(input("Enter Position Number Now (210-450)"))
        dist = choicetwo - lhpos
        print "traveling ",dist
        if dist < 0:
            dist = dist * -1
            while dist > 0:
                lhpos = lhpos - 1
                pwm.setPWM(lh, 0, lhpos)
                dist = dist - 1
                time.sleep(.005)
        elif dist > 0:
            while dist > 0:
                lhpos = lhpos + 1
                pwm.setPWM(lh, 0, lhpos)
                dist = dist - 1
                time.sleep(.005)
    elif choice == 4:
        #Left waist
        choicetwo = int(input("Enter Position Number Now (210-450)"))
        dist = choicetwo - lwpos
        print "traveling ",dist
        if dist < 0:
            dist = dist * -1
            while dist > 0:
                lwpos = lwpos - 1
                pwm.setPWM(lw, 0, lwpos)
                dist = dist - 1
                time.sleep(.005)
        elif dist > 0:
            while dist > 0:
                lwpos = lwpos + 1
                pwm.setPWM(lw, 0, lwpos)
                dist = dist - 1
                time.sleep(.005)
    elif choice == 5:
        #right foot
        choicetwo = int(input("Enter Position Number Now (210-450)"))
        dist = choicetwo - rfpos
        print "traveling ",dist
        if dist < 0:
            dist = dist * -1
            while dist > 0:
                rfpos = rfpos - 1
                pwm.setPWM(rf, 0, rfpos)
                dist = dist - 1
                time.sleep(.005)
        elif dist > 0:
            while dist > 0:
                rfpos = rfpos + 1
                pwm.setPWM(rf, 0, rfpos)
                dist = dist - 1
                time.sleep(.005)
    elif choice == 6:
        #right ankle
        choicetwo = int(input("Enter Position Number Now (210-450)"))
        dist = choicetwo - rapos
        print "traveling ",dist
        if dist < 0:
            dist = dist * -1
            while dist > 0:
                rapos = rapos - 1
                pwm.setPWM(ra, 0, rapos)
                dist = dist - 1
                time.sleep(.005)
        elif dist > 0:
            while dist > 0:
                rapos = rapos + 1
                pwm.setPWM(ra, 0, rapos)
                dist = dist - 1
                time.sleep(.005)
    elif choice == 7:
        #right hip
        choicetwo = int(input("Enter Position Number Now (210-450)"))
        dist = choicetwo - rhpos
        print "traveling ",dist
        if dist < 0:
            dist = dist * -1
            while dist > 0:
                rhpos = rhpos - 1
                pwm.setPWM(rh, 0, rhpos)
                dist = dist - 1
                time.sleep(.005)
        elif dist > 0:
            while dist > 0:
                rhpos = rhpos + 1
                pwm.setPWM(rh, 0, rhpos)
                dist = dist - 1
                time.sleep(.005)
    elif choice == 8:
        #right waist
        choicetwo = int(input("Enter Position Number Now (210-450)"))
        dist = choicetwo - rwpos
        print "traveling ",dist
        if dist < 0:
            dist = dist * -1
            while dist > 0:
                rwpos = rwpos - 1
                pwm.setPWM(rw, 0, rwpos)
                dist = dist - 1
                time.sleep(.005)
        elif dist > 0:
            while dist > 0:
                rwpos = rwpos + 1
                pwm.setPWM(rw, 0, rwpos)
                dist = dist - 1
                time.sleep(.005)
    elif choice == 0:
        choicetwo = input("Press 1 for squat and stand test")
        if choicetwo ==1:
            
    else:
        print " Try again Bozo "