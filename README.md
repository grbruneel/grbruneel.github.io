Written by Grant Bruneel
Last edit 4/3/2020

This code is written to be used on a raspberry pi to control the automatic testing and relplace the PLC's
The size and attributes of the buttons are made for the 7-in. raspberry pi touch screen

* One time adjustments to make on the pi before starting *
The LED screen will be updisde down and you will have to go to the settings to fix this.
These settings can be made before putting the pi onto the screen.

1. Flip the Screen
Open the terminal and edit the boot config.txt file with the command
    sudo nano /boot/config.txt 
and then add the following line to the bottom of the file
    lcd_rotate=2

2. Download the Code file
Still pending on the best way to do this...

3. Autostart the code on startup
Open the terminal and edit the ...........

* Update the Pi and the code *
In terminal use the following commands
    sudo apt-get update
    sudo apt-get upgrade
and update the code with ....


