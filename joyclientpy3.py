import pygame
from pygame.locals import *
import time
import os

#Netcode?
import socket               # Import socket module
s = socket.socket()         # Create a socket object
lochost = socket.gethostname() # Get local machine name
port = 56565                # Reserve a port for your service.
remhost = ("192.168.1.14")
#s.bind((lochost, port))        # Bind to the port
print(" ")
print ("local Host name:")
print(lochost)
print (" ")
print ("Port assigned")
print(port)

print ("attempting to connec to:")
print (remhost, port)
s.connect((remhost, port))
print (s.recv(1024))
s.close                     # Close the socket when done



#joycode
#pygame.init()
# Set up the joystick
pygame.joystick.init()
stickname = 0
stickname = (pygame.joystick.Joystick(0).get_name())
if stickname == 0:
    print ("BORKED!")
else:
    print ("Joystick detected")
    print(" ")
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
    print (" ")
    time.sleep(5)
    