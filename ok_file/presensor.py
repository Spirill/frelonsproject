import os
import RPi.GPIO as GPIO
import time

# Pin Definitons:
sensor1 = 17 # Broadcom pin 17 
sensor2 = 18 # Broadcom pin 18 
sensor3 = 19 # Broadcom pin 19 

# Pin Setup:
GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme
GPIO.setup(sensor1, GPIO.IN) # LED pin set as output
GPIO.setup(sensor2, GPIO.IN) # LED pin set as output
GPIO.setup(sensor3, GPIO.IN) # LED pin set as output

def my_callback():
    if(GPIO.input(sensor1) == 1):
     print("sensor 1 : presence")
    elif ( GPIO.input(sensor1) == 0):
        print("sensor 1 : nothing")
    else :
        print("Sensor 1 : no value")

def my_callback2():
    if(GPIO.input(sensor2) == 1):
     print("sensor 2 : presence")
    elif ( GPIO.input(sensor2) == 0):
        print("sensor 2 : nothing")
    else :
        print("Sensor 2 : no value")

def my_callback3():
    if(GPIO.input(sensor3) == 1):
     print("sensor 3 : presence")
    elif ( GPIO.input(sensor3) == 0):
        print("sensor 3 : nothing")
    else :
        print("Sensor 3 : no value")


# else is happening in the program, the function my_callback will be run  
GPIO.add_event_detect(sensor1, GPIO.BOTH, callback= lambda *a : my_callback(), bouncetime=300)  
#GPIO.add_event_detect(sensor2, GPIO.FALLING, callback=my_callback2, bouncetime=300)
#GPIO.add_event_detect(sensor3, GPIO.FALLING, callback=my_callback3, bouncetime=300)

#GPIO.remove_event_detect(port_number)