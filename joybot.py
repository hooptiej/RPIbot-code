#import pygame
#from pygame.locals import *
import time
import os

#Netcode?
import socket               # Import socket module
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 56565                # Reserve a port for your service.
s.bind(('', port))        # Bind to the port
#data = s.recv(1024).decode()


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
while True:
   #print ('Got connection from', addr)              
   c.send('Thank you for connecting')
   joydata = c.recv(1024).decode()
   print (joydata)
   #rxmess = (joydata.encode('ascii'))
   c.send(joydata.encode('ascii'))
   #c.close()                # Close the connection
   #some changes to commit
