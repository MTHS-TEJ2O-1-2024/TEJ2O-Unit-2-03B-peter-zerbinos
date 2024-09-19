"""
Copyright (c) 2020 MTHS All rights reserved

Created by: Peter Zerbinos
Created on: Sep 2024
This program does basic math
"""

from microbit import display, sleep, Image

# clear + pause
display.clear()
sleep(1000)

# statement
display.scroll("A rectangle has dimensions 5 cm & 3 cm.")

# clear + pause
display.clear()
sleep(1000)

# calculate perimeter + smiley
perimeter = 2 * (5 + 3)
display.scroll("The perimeter would be: {} cm".format(perimeter))
display.show(Image.HAPPY)

# clear + pause
display.clear()
sleep(1000)

# calculate area + smiley
area = 5 * 3
display.scroll("The area would be: {} cm^2".format(area))
display.show(Image.HAPPY)

# clear + pause
display.clear()
sleep(1000)
