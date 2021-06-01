Welcome to my Project

The repository is intended for updating some "sub-projects" related to a main project which consists of a PWM controlled by an analog input in the PocketBeagle board

PROGRAMS DESCRIPTION

-ADCpy.py

Currently functional. It's a simple python script for measuring a voltage level in any of the 5 main ADC ports (AIN0, AIN1, AIN2, AIN3, AIN4). Maximun supported voltage input is 1.8V so a circuitry arrange is needed to avoid damaging the computer. The proposed arrange consists of a voltage divider, with a resistor(or resistors) an a potenciometer to vary voltage in full ADC range.

On the resistor arrange, the variable output of the potenciometer is connected to the desired Analog Channel input, wich is later specified in the script (currently set to Analog Channel 0, PIN_19), a 3.3V connection to one end of the arrange and GND to the remaining end. Refer to Diagrama de conexiones.png for a wiring diagram.

*************************************************************************************************************************************

-PWM_ADCcontrolled.py 

Currently functional, but needs some tweaking.

The same principles and wiring described above for ADCpy.py, form which this script is derived, are the same. The former script allows to control a PWM duty cycle from a voltage level that is read in a analog channel, script allows to vary the PWM frequency as well. PWM output used is PWM0A(silk screen) PIN_36, refer to Diagrama de conexiones.png.

Refer to Esquemático completo.png for a functional application for the current project. The example application is a class-A chopper circuit with pure resitive load (RL) which was tested and validated with an osciloscope. Vcc is any voltage source, for wich I personally used a commercial DC-DC voltage converter powersource with a DC input supplied by a diode bridge that rectifies a transformer output. The L7812CV IC was used with an independent diode bridge thus it is possible to mange the optocupler PC123 as high side driver for the power MOSFET.


