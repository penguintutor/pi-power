#!/usr/bin/env python3
# Web remote for the Energenie Pi remote
# see http://www.penguintutor.com/
# Copyright Stewart Watkiss 2014-2015


# web-power is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this software.  If not, see <http://www.gnu.org/licenses/>

from gpiozero import Energenie
import bottle
from bottle import route, request, response, template, static_file

sockets = [None]
sockets.append(Energenie(1))
sockets.append(Energenie(2))
sockets.append(Energenie(3))
sockets.append(Energenie(4))

# allow on all ip addresses
HOST = ''
# port 80 - standard web port (assumes no other web server installed)
# If using apache or another browser then change this to a different value
PORT = 80

# Folder where this is installed and the index.html file is located
# The index.html file is exposed to the webserver as well as any files in a subdirectory called public (ie. /home/pi/pi-power/public) 
DOCUMENT_ROOT = '/home/pi/pi-power'

# Create the bottle web server
app = bottle.Bottle()


# public files
# *** WARNING ANYTHING STORED IN THE PUBLIC FOLDER WILL BE AVAILABLE TO DOWNLOAD BY ANYONE CONNECTED TO THE SAME NETWORK ***
@app.route ('/public/<filename>')
def server_public (filename):
    return static_file (filename, root=DOCUMENT_ROOT+"/public")
    
# Handle switch on request
@app.route ('/switchon')
def switchon():
    socket = int(request.query.socket)
    # If single socket requested
    if (socket > 0 and socket <= 4) :
        #print 'Switching on {}'.format(socket)
        sockets[socket].on()
        return 'Requested switch on {}'.format(socket)
    # If all sockets requested
    elif (socket == 0) : 
        for i in range (1, 5):
            sockets[i].on()
        return 'Requested switch on ALL'
    else :
        return 'Invalid request'
            
        
@app.route ('/switchoff')
def switchoff():
    socket = int(request.query.socket)
    # If single socket requested
    if (socket > 0 and socket <= 4) :
        #print 'Switching off {}'.format(socket)
        sockets[socket].off()
        return 'Requested switch off {}'.format(socket)
    # If all sockets requested
    elif (socket == 0) :
        for i in range (1, 5):
            sockets[i].off()
        return 'Requested switch off ALL'
    else:
        return 'Invalid request'
        

# Serve up the default index.html page
@app.route ('/')
def server_home ():
    return static_file ('index.html', root=DOCUMENT_ROOT)

app.run(host=HOST, port=PORT)