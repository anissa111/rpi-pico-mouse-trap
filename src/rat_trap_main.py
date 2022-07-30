import network
import urequests
import dht
from time import sleep,localtime
from machine import Pin, RTC

from ifttt import *

# set time
rtc = RTC()

# connect to pico wifi
wlan = network.WLAN(network.STA_IF)
wlan.active(True)

# get wifi SSD and password
file = open("wifi.txt", "r")
ssid = file.readline().split()[0]
pwd = file.readline()
file.close()

# get ifttt config
file = open("ifttt.txt", "r")
api_key = file.readline()
file.close()

# run configurations
max_retry = 5
running = True

while running:
    
    # check if connected to wifi
    wifi_retry = 0
    while not wlan.isconnected():
        
        # wait 1 min before retry
        if wifi_retry > 0:
            sleep(60)
            
        # attemp connect to wifi access point
        wlan.connect(ssid, pwd)
        sleep(5)
        
        # increment attemp count
        wifi_retry = wifi_retry + 1
        
        # trigger if max attempts reached and quit
        if wifi_retry > max_retry:
            
            # trigger ifttt
            hook = "something_wrong"
            v1 = "garage_trap"
            v2 = "wifi_fail"
            trigger_ifttt("something_wrong", api_key, v1="garage_trap", v2="wifi_fail")
            running = False
            break
        
        
        
        
        

applet = "test_trap"

ts = rtc.datetime()
ts = "%02d%02d%02d"%(ts[4:7])

message = "https://maker.ifttt.com/trigger/" + applet + "/with/key/" + api_key

print(message)
print("trying post message")
urequests.post(message)
print("posted message??")
