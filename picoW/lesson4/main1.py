from machine import Pin
import time
led=Pin(0,Pin.OUT)
i=0
while True:
    i+=1
    print(f"{i}")
    led.on()
    time.sleep(0.2)
    led.off()
    time.sleep(0.2)
   
