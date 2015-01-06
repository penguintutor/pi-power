#!/usr/bin/env python
# Web remote for the Energenie Pi remote
# see http://www.penguintutor.com/
# Copyright Stewart Watkiss 2014


# grobota is free software: you can redistribute it and/or modify
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

from energenie import switch_on, switch_off
import bottle
from bottle import route, request, response, template, static_file

app = bottle.Bottle()

# allow on all ip addresses
HOST = ''
# port 80 - standard web port (assumes no other web server installed)
PORT = 80

DOCUMENT_ROOT = '/home/pi/pi-power'

# public files
# *** WARNING ANYTHING STORED IN THE PUBLIC FOLDER WILL BE AVAILABLE TO DOWNLOAD ***
@app.route ('/public/<filename>')
def server_public (filename):
    return static_file (filename, root=DOCUMENT_ROOT+"/public")
    
@app.route ('/switchon')
def switchon():
    socket = int(request.query.socket)
    if (socket >= 0 and socket <= 4) :
        #print 'Switching on {}'.format(socket)
        switch_on (socket)
        if (socket == 0) : 
            return 'Requested switch on ALL'
        else :
            return 'Requested switch on {}'.format(socket)
        
@app.route ('/switchoff')
def switchoff():
    socket = int(request.query.socket)
    if (socket >= 0 and socket <= 4) :
        #print 'Switching off {}'.format(socket)
        switch_off (socket)
        if (socket == 0) :
            return 'Requested switch off ALL'
        else :
            return 'Requested switch off {}'.format(socket)

@app.route ('/')
def server_home ():
    return static_file ('index.html', root=DOCUMENT_ROOT)

app.run(host=HOST, port=PORT)