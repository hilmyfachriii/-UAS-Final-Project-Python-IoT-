#ESP32 Micropython example to read a input Pin (push button)
#let us import Pin and sleep modules

print('Hello Input Pins ;) ')
from machine import Pin
from time import sleep

#LED is connected ti D2 as output
led = Pin(2, Pin.OUT)
#push button is connected to Pin 13 , you can change it as needed
push_button = Pin(13, Pin.IN)

#we are good..
#let us create a loop to always monitor the button status and drive the LED on or off

while True:
    logic_state = push_button.value() #read the button state into logic_state variable
    if logic_state == True: # if button is pressed, turn on LED
        led.value(1)
    else:           # if button is pressed, turn off LED
        led.value(0)