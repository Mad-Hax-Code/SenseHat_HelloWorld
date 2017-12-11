# Application - HelloWorld_3.py

# import the sense_hat module
from sense_hat import SenseHat

# Create an instance (object) of the SenseHat() class called 'sense'
sense = SenseHat()

# Get text input from the user and store it in a String
# variable called textToDisplay
textToDisplay = input("Enter text: ")

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

# Clear the LED matrix
sense.clear()
