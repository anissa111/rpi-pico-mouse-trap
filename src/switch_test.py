from machine import Pin
import time

switch = Pin(14, Pin.IN, Pin.PULL_DOWN)

while True:
    if switch.value():
        print("trap closed")
        time.sleep(0.5)
