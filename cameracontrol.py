#!/usr/bin/python
# hooptiej on the case
import Adafruit_I2C
import Adafruit_PWM_Servo_Driver
from Adafruit_PWM_Servo_Driver import PWM
import time
import os
clear = lambda : os.system('tput reset')
import pygame
from pygame.locals import *
clock = pygame.time.Clock()
clear()
# ===========================================================================
# Example Code
# ===========================================================================

# Initialise the PWM device using the default address
pwm = PWM(0x40)
# Note if you'd like more debug output you can instead run:
#pwm = PWM(0x40, debug=True)

servoMin = 80  # Min pulse length out of 4096
servoCenter = 330 # math center
servoMax = 550  # Max pulse length out of 4096


servoPos = servoCenter
servopos = servoCenter
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
print "Centering All Servos"
print " "
time.sleep(2)
  
  # set all servos to center to start
choice = 0
loop = 1
choicetwo = 0
choicejoytest = 0
pygame.init()
pygame.joystick.init()
pygame.joystick.Joystick(0).init()
hattest = 1

servoposX = 0
servoposY = 0
servoposX = servoCenter
servoposY = servoCenter

pwm.setPWM(14, 0, servoposX)
pwm.setPWM(15, 0, servoposY)
            
while hattest > 0:
  #  print " "
 #   print("Monitoring X-Y on Main Stick")
#    print " "
    for event in pygame.event.get():
        if event.type == pygame.JOYAXISMOTION:
            joyposone = pygame.joystick.Joystick(0).get_axis(0)                    
            joypostwo = pygame.joystick.Joystick(0).get_axis(1)
#            print "got axed"
	    #if joyposone == 0:
                #servoposX = servoCenter               
            if joyposone > 0:
                servoposX = servoposX - 1
            elif joyposone < 0:
                servoposX = servoposX + 1
            print " "
            if servoposX >= servoMax:
                servoposX = servoMax
            if servoposX <= servoMin:
                servoposX = servoMin
            #if joypostwo == 0:
            #        servoposY = servoCenter
            if joypostwo > 0:
                servoposY = servoposY + 1
            elif joypostwo < 0:
                servoposY = servoposY - 1
            print " "
            if servoposX >= servoMax:
                servoposY = servoMax
            if servoposX <= servoMin:
                servoposY = servoMin
            pwm.setPWM(14, 0, servoposX)
            pwm.setPWM(15, 0, servoposY)
            #time.sleep(.1)
            #clock.tick(15)
           # clear()
		
