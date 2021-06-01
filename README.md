Welcome to my Project

The repository is intended for updating some "sub-projects" related to a main project which consists of a PWM controlled by an analog input in the PocketBeagle board

PROGRAMS DESCRIPTION

-PWM_ADCcontrolled.py 

  Is currently functional. It requires a potenciometer to control a voltage level form 0 to 1.8V in any of the 5 main ADC ports (AIN0, AIN1, AIN2, AIN3, AIN4). Maximun voltage input is 1.8V so a
  circuitry arrange is needed to avoid damaging the computer. The arrange consists of a voltage divider, with a resistor(or resistors) an a potenciometer to vary voltage in full ADC range.

  Once the resistor arrange is complete the variable output of the potenciometer is connected to the desired Analog Channel input wich is later specified in the script (currently set to Analog Channel 0, PIN_19), a 3.3V connection to on end of the arrange and GND to the remaining end. 

  PWM output is PWM0A(silk screen) PIN_36
