# Application - HelloWorld_1.py

# import the sense_hat module
from sense_hat import SenseHat

# use the SenseHat() class to create an object 'sense'
sense = SenseHat()

# Use the show_message() method of the 'sense' object to display
# your message. The sense hat led screen should scroll Hello World
sense.show_message("Hello World")

# Rotate the display by 180 degrees
sense.set_rotation(180)
# display the message with new orientation
sense.show_message("Hello World")

# Rotate the display by 90 degrees
sense.set_rotation(90)
# display the message with new orientation
sense.show_message("Hello World")

# Rotate the display by 270 degrees
sense.set_rotation(270)
# display the message with new orientation
sense.show_message("Hello World")
