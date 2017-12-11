# Application - HelloWorld_3.py

# import the sense_hat module
from sense_hat import SenseHat

# Create an instance (object) of the SenseHat() class called 'sense'
sense = SenseHat()

# Get text input from the user and store it in a String variable called userText
userText = input("Enter text: ")

# Set text and background colors
textColor = (255,255,0)
backColor = (0,0,255)

# Correct the display orientation if neccessary
sense.set_rotation(180)

# Display the text stored in the userText variable on sense hat LED matrix
sense.show_message(userText, text_colour = textColor, back_colour = backColor)

# Clear the LED matrix
sense.clear()
