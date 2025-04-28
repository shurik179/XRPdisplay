# SPDX-FileCopyrightText: Copyright 2025 Alexander Kirillov <shurik179@gmail.com>
#
# SPDX-License-Identifier: MIT

"""
`xrp display`
====================================================

This is a micropython library for XRP display by Alexander Kirillov.

* Author(s): Alexander Kirillov
* Version: 1.0
"""

# import micropython libraries 
from machine import Pin, SPI
import time
import sys
import neopixel
# For SPI display
import st7789_purefb as st7789
from ezFBfont import ezFBfont
import PTSans_NarrowBold_32 
import ezFBfont_helvB14_ascii_18 
import PTSans_Narrow_24 

disp_sck    = 18 # default SCK of SPI(0)
disp_mosi   = 19 # default MOSI of SPI(0)
disp_miso   = 16  # not use
disp_res    = 14
disp_dc     = 15
disp_cs     = 17
neopixel_pin = 37
buttonA_pin = 36
buttonB_pin = 12 


class XrpDisplay:
    def __init__(self):
        self.npxl = neopixel.NeoPixel(Pin(neopixel_pin, Pin.OUT), 3)
        #self.brightness = 64
        self.display = st7789.ST7789_SPI(
            SPI(0,  baudrate=80_000_000,sck=Pin(disp_sck), mosi=Pin(disp_mosi), miso=None),
            width = 135,
            height = 240,
            reset=Pin(disp_res, Pin.OUT),
            cs=Pin(disp_cs, Pin.OUT),
            dc=Pin(disp_dc, Pin.OUT),
            backlight = None,
            rotation = 3,
        )
        self.buttonA = Pin(buttonA_pin, Pin.IN, Pin.PULL_UP)
        self.buttonB = Pin(buttonB_pin, Pin.IN, Pin.PULL_UP)

        #colors
        self.BLACK    = 0x0000
        self.DARKGREY = 0x4208
        self.NAVY     = 0x0010
        self.BLUE     = 0x001f
        self.GREEN    = 0x0400
        self.TEAL     = 0x0410
        self.AZURE    = 0x041f
        self.LIME     = 0x07e0
        self.CYAN     = 0x07ff
        self.MAROON   = 0x8000
        self.PURPLE   = 0x8010
        self.OLIVE    = 0x8400
        self.GREY     = 0x8410
        self.SILVER   = 0xc618
        self.RED      = 0xf800
        self.ROSE     = 0xf810
        self.MAGENTA  = 0xf81f
        self.ORANGE   = 0xfc00
        self.YELLOW   = 0xffe0
        self.WHITE    = 0xffff

        # print(st7789.__name__, display.width, "x", display.height)
        self.display.fill(self.BLACK)
                
        self.largefont = ezFBfont(self.display, PTSans_NarrowBold_32, fg = self.WHITE, cswap = True)
        self.smallfont = ezFBfont(self.display, ezFBfont_helvB14_ascii_18, fg = self.WHITE, cswap = True)
        self.smallfont2 = ezFBfont(self.display, PTSans_Narrow_24, fg = self.WHITE, cswap = True)

  
        self.largefont.write('Welcome to XRP',20 , 40, fg = self.RED)
        #self.smallfont2.write('Press any button \nto continue', 5, 85)

        self.display.show()
        
    def clear(self):
        self.display.fill(self.BLACK)
        self.display.show()  

    def write_line(self, line, text, font = None, fg = None):
        if font is None:
            font = self.smallfont
        # first, clear the space from previous messages
        numlines = text.count('\n') + 1
        self.display.fill_rect(1, 22*(line-1)+3, self.display.width, 22*numlines, self.BLACK)
        font.write(text, 5, 22*(line-1)+3, fg = fg)
        self.display.show()

    def set_leds(self, left_color, right_color = None):
        if right_color is None:
            right_color = left_color
        self.npxl[1]=left_color
        self.npxl[2]=right_color
        self.npxl.write()
        
    def is_button_pressed(self, button) -> bool:
        """
        Returns the state of the button

        :return: True if the button is pressed, False otherwise
        :rtype: bool
        """
        return not button.value()
    
    def wait_for_button(self) -> int:
        """
        Halts the program until a button is pressed. Returns button index: 1 for button A, 2 for button B
        """

        # Wait until user presses a button
        press = None
        while press is None:      
            if self.is_button_pressed(self.buttonA):
                press = 1
            elif self.is_button_pressed(self.buttonB):
                press = 2
            else:
                time.sleep(0.01)                    
        
        # Wait until user to release button before running
        while self.is_button_pressed(self.buttonA) or self.is_button_pressed(self.buttonB):
            time.sleep(.01)
        
        return press
        