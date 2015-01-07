Install instructions for pi-power
=================================

These are the instructions for installing pi-power on a Raspberry Pi.
For more details see [www.penguintutor.com/pi-power](www.penguintutor.com/pi-power)



__Warning - this software does not require any authentication__
**Anyone with access to the network that the Raspberry Pi is on can 
turn the sockets on and off.**



This program uses the Python Bottle library.

It is important to install bottle through pip (or manually if you prefer)
as the version installed using apt-get on the Raspberry Pi will not work

To install bottle enter the following two commands whilst connected to the Internet.

sudo apt-get install python-pip
sudo pip install bottle

The energenie module is also required 

sudo pip install energenie


After extracting the files from the tar file run the web-power.py script as root.

ie.:

$ sudo ./web-power.py

The code is configured to use the standard http port, which is port 80. 
If you already have a web server running (eg. Apache / Lighttpd) then the port number will need to be changed in the web-power.py file first.



Connect to the webserver using a web browser. You will need to know the ip address which can be found using:

$ ip addr

The program is designed to run standalone without any other web servers installed on the computer. If you need this alongside another web server then you may need to change the port number in the web-power.py file.


The menu options can be customized by editing the index.html file.


The program can be set to startup automatically by copying the startup script to init.d

sudo cp web-power.startup /etc/init.d/web-power 
sudo chown root:root /etc/init.d/web-power
sudo chmod 755 /etc/init.d/web-power
sudo update-rc.d web-power


