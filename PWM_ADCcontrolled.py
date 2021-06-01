#!/usr/bin/python 
import sys
#import time

ADC0_PATH = "/sys/bus/iio/devices/iio:device0/in_voltage"
PWM0_PATH = "/sys/devices/platform/ocp/48300000.epwmss/48300200.pwm/pwm/pwmchip0"
dc = 0
ADCmax = 2768
c=1e-9
f =500 #1 = 1ns | f=1/period 20000000.0
mindc = int(0.05*period)

def readAnalog(number):
    """This function reads a RAW ADC value from the path"""
    aps = ADC0_PATH + str(number) + "_raw"
    fo1 = open(aps,"r")
    acr = fo1.read()
    return acr

def ctrlPWM(parameter, value, pwm0path=PWM0_PATH +"/pwm-0:0"):
    fo2 = open(pwm0path + parameter,"w")
    fo2.write(value)
    fo2.close()
    return

def f2t(freq):
    period = 1/(freq*c)
    return period

def dct(decimal):
    dc = int(period*float(decimal)/ADCmax)
    if dc<(0.05*period):
        dc = 0.05*period
    elif dc>(0.95*period):
        dc = 0.95*period
    return dc
    
#Application begins:
print("Starting ADC Script")
#config-pin P1_33 pwm
print("Reading Analog 0")

period = f2t(f)
#Set initial PWM values
ctrlPWM("/period", str(int(period)))
ctrlPWM("/duty_cycle", str(mindc))
ctrlPWM("/enable", "0")
ctrlPWM("/enable", "1")

while True:
    ctrlPWM("/duty_cycle", str(int(dct(readAnalog(0)))))
    
print("End of test Script")
