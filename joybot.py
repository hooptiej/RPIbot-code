import time
import os
import pickle
import Adafruit_I2C
import Adafruit_PWM_Servo_Driver
from Adafruit_PWM_Servo_Driver import PWM

# Initialize the Servo Controller
pwm = PWM(0x40)
servoMin = 80  # Min pulse length out of 4096
servoCenter = 330 # math center
servoMax = 550  # Max pulse length out of 4096
servoPos = servoCenter
servopos = servoCenter
def setServoPulse(channel, pulse):
  pulseLength = 1000000                   # 1,000,000 us per second
  pulseLength /= 60                       # 60 Hz
  #print "%d us per period" % pulseLength
  pulseLength /= 4096                     # 12 bits of resolution
  #print "%d us per bit" % pulseLength
  pulse *= 1000
  pulse /= pulseLength
  pwm.setPWM(channel, 0, pulse)
pwm.setPWMFreq(60)    
#end Servo controller init           



#Initalize Netcode
import socket               # Import socket module
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 56565                # Reserve a port for your service.
s.bind(('', port))        # Bind to the port



print(" ")
print ("Host name:")
print(host)
print (" ")
print ("Port assigned")
print(port)
print ("")
print ("Opening Socket to listen")
s.listen(5)# Now wait for client connection.
c, addr = s.accept()     # Establish connection with client. 
cm = 'Connected to RasPi Bot'
c.send(cm.encode('ascii')) 
print ('Controller connected from', addr) 
while True:             
    joydata = c.recv(2048)#.decode()
    joyd = pickle.loads(joydata)
    joyaxeone = (joyd[1]) #camera tilt left stick
    joyaxetwo = (joyd[2]) #cam tilt left stick 
    joyaxethree = (joyd[3]) #throttle - right stick
    joyaxefour = (joyd[4]) #steering servo - right stick
    frameref = "ack"
    printref = str(frameref)
    c.send(printref.encode('ascii'))
    print("Rx!")
    #Servo Positioning 
    campan = 0
    camtilt = 0
    campan = servoCenter
    camtilt = servoCenter
    if joyaxeone  > 0:
        camtilt = camtilt + 1
    elif joyaxeone < 0:
        camtilt = camtilt - 1 
    else
    if joyaxetwo  > 0:
        campan = campan + 1
    elif joyaxerwo < 0:
        campan = campan - 1 
    else
    pwm.setPWM(14, 0, camtilt)
    pwm.setPWM(15, 0, campan)
    #c.close()                # Close the connection
