#!/usr/bin/python 
import sys
import time

ADC0_PATH = "/sys/bus/iio/devices/iio:device0/in_voltage"
voltage, vmax = 0.0, 1.8

def readAnalog(number):
    """This function reads a RAW ADC value from the path"""
    ps = ADC0_PATH + str(number) + "_raw"
    fo = open(ps,"r")
    value = fo.read()
    return value
    
def convert(decimal):
    voltage = float(decimal)*(vmax/4095)
    return voltage
    
#Application begins:
print("Starting ADC Script")

print("Reading Analog 0")
for i in range (1, 10):
    print("Analog Channel 0 Input = " + str(readAnalog(0)))
    print("Voltage = " + str(convert(readAnalog(0)))[0:5])
    print('-'*10)
    time.sleep(1)
    
print("End of test Script")