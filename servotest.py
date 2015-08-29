#!/usr/bin/python

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

servoMin = 210  # Min pulse length out of 4096
servoCenter = 330 # math center
servoMax = 450  # Max pulse length out of 4096


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
while loop == 1:  
#print what options you have
    clear()
    print "Welcome to servotest run"
    print " "
    print "your options are:"
    print " "
    print "1) center servos"
    print "2) center and sweep test a servo"
    print "3) check for joystick/gamepad"
    print "5) quit"
    choice = input("Choose your option: ")
    if choice == 1:
            pwm.setPWM(0, 0, servoPos)
            pwm.setPWM(1, 0, servoPos)
            pwm.setPWM(2, 0, servoPos)
            pwm.setPWM(3, 0, servoPos)
            pwm.setPWM(4, 0, servoPos)
            pwm.setPWM(5, 0, servoPos)
            pwm.setPWM(6, 0, servoPos)
            pwm.setPWM(7, 0, servoPos)
            pwm.setPWM(8, 0, servoPos)
            pwm.setPWM(9, 0, servoPos)
            pwm.setPWM(10, 0, servoPos)
            pwm.setPWM(11, 0, servoPos)
            pwm.setPWM(12, 0, servoPos)
            pwm.setPWM(13, 0, servoPos)
            pwm.setPWM(14, 0, servoPos)
            pwm.setPWM(15, 0, servoPos)
	    choice = 0
    elif choice == 2:
	clear()
        print " "
        print "Select a Servo Numbered  0-15 to sweep test and show center"
        print " "
	choicetwo = input("press a number now:")
	servochannel = choicetwo
	if choicetwo >= 0:
		print " "
		print "Centering Servo channel " , (choicetwo)
		pwm.setPWM(servochannel, 0, servopos)
		time.sleep(2)
		print "Starting Sweep to Max + throw"
		while servopos < servoMax:
			servopos = servopos + 5
			pwm.setPWM(servochannel, 0, servopos)
			time.sleep(0.1)
			print "."
		print "Maximum + throw"
		time.sleep(2)
		print " "
		print "Starting sweep to Max - throw"
		while servopos > servoMin:
			servopos = servopos - 5
                        pwm.setPWM(servochannel, 0, servopos)
			time.sleep(0.1)
			print "."
		print "Maximum - throw"
		time.sleep(2)
		print "Start sweep to Center"
		while servopos != servoCenter:
			servopos = servopos + 5
                        pwm.setPWM(servochannel, 0, servopos)
			time.sleep(0.1)
			print "."
		print "servo is centered"
		time.sleep(3)
    elif choice == 3:
	clear()
	print " "
    	print "checking for joysick"
	pygame.init()
	# Set up the joystick
	pygame.joystick.init()
	stickname = 0
	stickname = (pygame.joystick.Joystick(0).get_name())
	if stickname == 0:
	    print "..."
	else:
	    print " "
   	    print "Joystick detected"
	    time.sleep(1)
	    clear()
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
    elif choice == 4:
	    pygame.init()
	    clear()
	    pygame.joystick.init()
	    # print pygame.joystick.Joystick(0).get_init()
	    print "joystick controlled test"
	    time.sleep(2)
	    print " "
            print "Select servo channels to test with main stick "
	    time.sleep(1)
	    choicethree = input("enter servo channel for X now : ")
	    choicefour = 0
	    choicefour = input("enter servo channel for Y now : ")
	    servochannelx = choicethree
	    servochannely = choicefour
	    time.sleep(1)
	    hattest = 1
	    clear()
	    servoposX = 0
	    servoposY = 0
	    servoposX = servoCenter
	    servoposY = servoCenter

	    while hattest > 0:
	  	  for event in pygame.event.get():
			if event.type == pygame.JOYAXISMOTION:
				print " "
				print("Monitoring X-Y on Main Stick")
	 			print " "
	    			joyposone = pygame.joystick.Joystick(0).get_axis(0)

				joypostwo = pygame.joystick.Joystick(0).get_axis(1)
				#if joyposone == 0:
				#	servoposX = servoCenter
					
				if joyposone > 0:
					servoposX = servoposX - 3
				elif joyposone < 0:
					servoposX = servoposX + 3
				print " "
				if servoposX >= servoMax:
					servoposX = servoMax
				if servoposX <= servoMin:
					servoposX = servoMin
                                #if joypostwo == 0:
                                #        servoposY = servoCenter

                                if joypostwo > 0:
                                        servoposY = servoposY + 3
                                elif joypostwo < 0:
                                        servoposY = servoposY - 3
                                print " "
                                if servoposX >= servoMax:
                                        servoposY = servoMax
                                if servoposX <= servoMin:
                                        servoposY = servoMin
                                pwm.setPWM(servochannelx, 0, servoposX)
				pwm.setPWM(servochannely, 0, servoposY)
				#time.sleep(.1)
				clock.tick(15)			
				#clear()


	    time.sleep(3)
    elif choice == 5:
                loop = 0
print "Stopping Test"
print " "
print " "
print " "
clear()
            
