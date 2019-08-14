Welcome to CircuitPython!
#############################

Time to set the record STRAIGHT: CircuitPython RULEs and don't try to argue, 
we won't budge an INCH! With this 6" long dev board, you can see how 
CircuitPython deveopment MEASURES up against the standard compile/upload 
cycle with a handy reference guide to common packages.

Best of all, this ruler is smart! You can plug it into your computer, and 
turn it into a 4-button keypad that will type those pesky Ohm, Mu and Pi 
symbols (see below on how to do that).

We worked with Digi-Key, our favorite electronics component supplier, to
design this super cool ruler and have it released in celebration of 
CircuitPython day, which we observe on August 8 every year. (8/8 is the 
snakiest of dates, don't you agree?)

Visit the PyRuler product page here for more info: 
    https://adafruit.com/product/4319

For the latest version of CircuitPython for this board, visit
    https://circuitpython.org/board/pyruler/

#############################

The PyRuler has a very tiny disk drive so we have disabled Mac OS X indexing
which could take up that valuable space. 

So *please* do not remove the empty .fseventsd/no_log, .metadata_never_index 
or .Trashes files! 

#############################

The pre-loaded demo shows off what your PyRuler can do with CircuitPython.
All the code is stored in a code.py file. Edit it with the Mu code editor and
save to restart the program.
The demo program watches for capacitive finger touches on the 4 pads and will
light up the matching LED to let you know it was detected. 

You can turn the PyRuler into a keyboard! Edit code.py and find the line that asays

# Set this to True to turn the touchpads into a keyboard
ENABLE_KEYBOARD = False

Change the 'False' value to 'True' and save. Now when you touch the Ohm, Mu, 
or Pi symbol, that key will be typed out.
Open up your browser, click on the address bar and touch the Digi-Key logo for

For more details on how to use CircuitPython, visit 
    https://adafruit.com/product/4319 
and check out all the tutorials we have!
The PyRuler contains the circuitry for a Trinket M0 so you may also want to
visit 
    https://adafruit.com/product/3500
To learn more about the amazing projects you can build with a Trinket M0

#############################
CircuitPython Quick Start:

Changing the code is as easy as editing main.py in your favorite text editor. 
We recommend Mu, Atom, Notepad++, or Visual Studio Code. After the file is 
saved, CircuitPython will automatically reload the latest code. 

Connecting to the serial port will give you access to better error messages and
interactive CircuitPython (known as the REPL). On Windows we recommend 
Tera Term or PuTTY. On Mac OSX and Linux, 'screen' can be used from a terminal.
