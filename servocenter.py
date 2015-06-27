#!/usr/bin/python

from Adafruit_PWM_Servo_Driver import PWM
import time

# ===========================================================================
# Example Code
# ===========================================================================

# Initialise the PWM device using the default address
pwm = PWM(0x40)
# Note if you'd like more debug output you can instead run:
#pwm = PWM(0x40, debug=True)

servoMin = 80  # Min pulse length out of 4096
servoCenter = 330 # math center
servoMax = 580  # Max pulse length out of 4096

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

  # Change speed of continuous servo on channel O
pwm.setPWM(0, 0, servoCenter)
pwm.setPWM(1, 0, servoCenter)
pwm.setPWM(2, 0, servoCenter)
pwm.setPWM(3, 0, servoCenter)
pwm.setPWM(4, 0, servoCenter)
pwm.setPWM(5, 0, servoCenter)
pwm.setPWM(6, 0, servoCenter)
pwm.setPWM(7, 0, servoCenter)
pwm.setPWM(8, 0, servoCenter)
pwm.setPWM(9, 0, servoCenter)
pwm.setPWM(10, 0, servoCenter)
pwm.setPWM(11, 0, servoCenter)
pwm.setPWM(12, 0, servoCenter)
pwm.setPWM(13, 0, servoCenter)
pwm.setPWM(14, 0, servoCenter)
pwm.setPWM(15, 0, servoCenter)
pwm.setPWM(16, 0, servoCenter)
