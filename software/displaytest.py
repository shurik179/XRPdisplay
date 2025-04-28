from machine import Pin
import time
import xrpdisplay

# LED colors. These can't be used for display colors - those use different format!!
# As usual, each color ranges 0-255, but we suggest using values of 64 or lower - 
# even that is quite bright.
# Blue is dimmer than red and green, so we use higher values 
RED = (32,0,0)
GREEN = (0,32,0)
BLUE = (0,0,64)


d = xrpdisplay.XrpDisplay();
# Setting LED colors. First argument is color of left LED, second, of right.
# Second argument is optional; if omitted, same color is used for both LEDs:
# d.set_leds(RED)
d.set_leds(RED, BLUE)
d.write_line(5,'        Press any button \n               to continue')
# buttons. There are 2 buttons, labeled A and B. This command waits
# until a button is pressed, returns button index: 1 for A, 2 for B
x = d.wait_for_button()
# you can also check if a button is currently pressed:
# if d.is_button_pressed(d.buttonA): 
# basic display usage
d.clear()
d.write_line(2, f'Pressed button {x}')
# you can also choose font and text color (fg).
# Available fonts are d.smallfont (default), d.smallfont2 (slightly more narrow) and d.largefont
# Available colors (all prefixed with d.):
# BLACK, DARKGREY, NAVY,BLUE,GREEN,TEAL,AZURE,LIME,CYAN,MAROON
# PURPLE, OLIVE, GREY, SILVER, RED, ROSE, MAGENTA,ORANGE,YELLOW,WHITE

d.write_line(3, "smallfont2", font = d.smallfont2, fg = d.BLUE)
d.write_line(4, "Largefont", font = d.largefont)
# Note that largefont is higher than line height, so it also uses part of line 5
d.write_line(6, "Press button to continue", fg=d.YELLOW)
d.wait_for_button()
for i in range(1,7):
    d.write_line(i, f'This is line {i}')
time.sleep(3)
# more advanced use. You can use any framebuffer commands,
# see https://docs.micropython.org/en/latest/library/framebuf.html
# Note that you have to clear display before
# and use display.show() after graphics commands
# you can also use write command, documented at
# https://github.com/easytarget/microPyEZfonts/blob/main/WRITER.md
# with any of the avialable fonts (d.smallfont, d.smallfont2, d.largefont)
d.clear()
d.display.fill_rect(30,30, 180, 75, d.GREEN) 
d.largefont.write('THE END',60 , 52, fg = d.RED, bg = d.GREEN)
d.display.show()




