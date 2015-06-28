import pygame
from pygame.locals import *
import time
import os

#Netcode?
import socket               # Import socket module
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)         # Create a socket object
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
#s.close                     # Close the socket when done



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
    pygame.init()
    joymotion = 1
    while joymotion > 0:
        for event in pygame.event.get():
            if event.type == pygame.JOYAXISMOTION:
                joyaxeone = str(pygame.joystick.Joystick(0).get_axis(0))
                joyaxetwo = str(pygame.joystick.Joystick(0).get_axis(1))
                joyaxethree = str(pygame.joystick.Joystick(0).get_axis(2))
                joyaxefour = str(pygame.joystick.Joystick(0).get_axis(3))
            #print (joyaxeone)
            #print (joyaxetwo)
            #print (joyaxethree)
            #print (joyaxefour)
            #s.connect((remhost, port))
            s.send(joyaxeone.encode('ascii'))
            print (s.recv(1024))