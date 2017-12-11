# Application - HelloWorld_2.py

# import the sense_hat module
from sense_hat import SenseHat

# create an instance (object) from the SenseHat class
sense = SenseHat()

# Below we create a String variable called textToDisplay
# (a variable that is considered text) We also assign the
# value of Hello World to that String variable
textToDisplay = "Hello World"

# Create a tuple in the format Red, Green, Blue (RGB)
# The following puts no values in Red or Green, but puts a
# full value in the Blue section. This will result in a
# blue background
backgroundColor = (0,0,255)

# The following tuple will result in yellow text
textColor = (255, 255, 0)

# Correct display orientation needed
sense.set_rotation(180)

# Display text
sense.show_message(textToDisplay,
                   text_colour = textColor,
                   back_colour = backgroundColor)

# Clear the LED screen
sense.clear()
