# Install instructions for pi-power


These are the instructions for installing pi-power on a Raspberry Pi.
For more details see [www.penguintutor.com/pi-power](www.penguintutor.com/pi-power)

__Warning - this software does not require any authentication__
**Anyone with access to the network that the Raspberry Pi is on can turn the sockets on and off.**

## Hardware Requirements

This program is for a Raspberry Pi using a pi-mote add-on from Energenie.


## Pre-requisites

This program requires a recent version of GPIO Zero and the Python 3 bottle library. It is recommended thatyou first update your system using

```bash
sudo apt-get update
sudo apt-get dist-upgrade
```

If you do not already have Python bottle installed this can be installed using

```bash
sudo apt-get install python3-bottle
```

## Install Pi-power software

This program is available from GitHub. The latest version can be installed using:

```bash
cd /home/pi
git clone https://github.com/penguintutor/pi-power.git
```

This will install the program into directory `/home/pi/pi-power`. If using a different directory then you will need to edit the DOCUMENT_ROOT setting within web-power.py


The `web-power.py` script can then be run as root.

```bash
sudo /home/pi/pi-power/web-power.py
```

The code is configured to use the standard http port, which is port 80. 
The program is designed to run standalone without any other web servers installed on the computer. If you already have a web server running (eg. Apache / Lighttpd) then the port number will need to be changed in the web-power.py file first. If a port greater than 1024 then the program does not need to be run as root and so the sudo part of the command can be removed.

Connect to the webserver using a web browser. You will need to know the ip address which can be found using:

```bash
$ ip addr
```

## Customizing the program
The customizations are made in the configuration files for the program. If upgrading the program then the following settings will be set back to their defaults. 

### Change the network port
To assign a different port update the `PORT` entry in `web-power.py`. Setting the port above 1024 will allow the program to be run as a normal user. 

### Change the install directory
If installing to a directory other than `/home/pi/pi-power` then update the `DOCUMENT_ROOT` in `web-power.py` to the install folder.

### Give the buttons user-friendly names
The socket names (Socket 1) are coded directly into index.html
Change these to custom names.

## Setting the program to automatically start on boot

The program can be set to startup automatically by copying the startup file to the systemd service folder and then enabling this.

```bash
sudo cp /home/pi/pi-power/web-power.service /etc/systemd/system/
sudo systemctl enable web-power.service
```

## Turning the sockets on and off automatically

In addition to using the web interfact the sockets can be set to switch on and off automatically. This can be achieved using cron and the crontab configuration file. 

See the following page for more details:
http://www.penguintutor.com/raspberrypi/pi-power 

