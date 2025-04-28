#################
Usage
#################

Connecting to XRP controller
############################
To connect it to XRP controller, put the switch on the controller in "off" position. C
onnect all motors, servos, and sensors you intend to use to XRP controller. It is also advisabe to unplug 
the battery cable. 

Plug the board into the headers on the controller as shown in the photos. Make sure they 
are aligned and not off by one. Whne plugging in, you might need to push hard - but never push 
on the display itself.  

After plugging in, you can reconnect the battery and turn the swithc on the board to "on"; switch on the 
controller should stay in off position.

Software installation
######################

Download all files in software/lib folder of the |github| and copy them to /lib folder of your XRP controller 
(I use Thonny edtor for that). 

Now run `displaytest.py` file for demonstration of the board capabilities. This file is amply commented, 
making it easy to copy. 

Library reference
#################

To use the display in your own micropython code, use the commnads below 

Initialization
--------------

To initialize the display, put htis in the beginning of your code:


.. code-block:: python
   import xrpdisplay
   d = xrpdisplay.XrpDisplay()


All functions below will be methods of object `d`. 

Neopixels
---------

.. function:: set_leds(lcolor, rcolor)
   Sets the colors of the two Neopixel LEDs. `lcolor` sets the color of left LED, and `rcolor`, 
   of the right one.  `rcolor` is optional; if omitted, both LEDs are set to the same color. 
   Each color should be a triple of numbers ranging 0-255, desribing intensity of red, green, and blue LEDs, e.g. 
   `d.set_leds( (64, 0, 0 ) )` to set both LEDs red. 

   Note: it is recommended that you only use values 0-64 for each color intensity; even that is quite bright. 
   Using intensity of 255 woudl make the LEDs blindingly bright. 

Buttons
-------

.. function:: wait_for_button()
   Waits until user presses and releases one of two buttons. Returns button index: 1 for button A, 2 for button B. 


.. function:: is_button_pressed(button)
   Returns true if the corresponding button is pressed and zero otherwise. `button` must be one of `d.buttonA`, `d.buttonB`. 


Display
-------       




