from machine import Timer, Pin
import time

green_led = Pin("LED",Pin.OUT)
red_led = Pin(15,Pin.OUT)
switch_button = Pin(14,Pin.IN,Pin.PULL_DOWN)

while True:
    if switch_button.value():
        red_led.toggle()
        time.sleep(0.5)