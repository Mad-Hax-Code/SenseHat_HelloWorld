# Application - HelloWorld_2.py

# import the sense_hat module
from sense_hat import SenseHat

# create an instance (object) from the SenseHat class
sense = SenseHat()

# Below we create a String variable called textToDisplay
# Then assign the value of Hello World to that variable
textToDisplay = "Hello World"

# Set text and background colors using tuples in RGB format
textColor = (255,255,0)
backColor = (0,0,255)

# Correct the display orientation if neccessary
sense.set_rotation(180)

# Display the text stored in the textToDisplay variable on
# sense hat LED matrix
sense.show_message(textToDisplay,
                   text_colour = textColor,
                   back_colour = backColor)

# Clear the LED screen
sense.clear()
