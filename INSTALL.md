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

This will install the program into directory `pi-power` in your home director. If using a different directory then you will need to edit the DOCUMENT_ROOT and bottle.TEMPLATE_PATH settings within web-power.py (see later) and the ExecStart entry in the web-power.service script.


The `web-power.py` script can then be run as root.

```bash
sudo ~/pi-power/web-power.py
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
**Important**
If installing to a directory other than `/home/pi/pi-power` then update the `DOCUMENT_ROOT` and `bottle.TEMPLATE_PATH` in `web-power.py` to the install folder.


### Customising using templates and themes
The software supports templates and themes within those templates. The templates are stored in the views folder. 
The default template is the initial template based on previous version of Pi-power. The image template provides a 2x2 image based display.
These can be set using the variable:
custom_template

Within the template is support for themes. These are folders where custom images and CSS can be placed to customize the display. This can be setup using the variable: 
custom_theme

The images should be stored in a directory based on the template and theme name. For instance:
custom_template = "image"
custom_theme = "christmas"
The folder name is image_christmas

### Integration with other services
To integrate with other web services then it can either be embedded through an iFrame, or you can have the other service link direct. The home_link and home_title variables can be used to provide a path back to the calling application if required.

## Setting the program to automatically start on boot

The program can be set to startup automatically by copying the startup file to the systemd service folder and then enabling this.

```bash
sudo cp ~/pi-power/web-power.service /etc/systemd/system/
sudo systemctl enable web-power.service
```

***Important***
If using a directory other than /home/pi then you will first need to update the ExecStart entry with the full path.

## Turning the sockets on and off automatically

In addition to using the web interface the sockets can be set to switch on and off automatically. This can be achieved using cron and the crontab configuration file. 

See the following page for more details:
http://www.penguintutor.com/projects/pi-power 

