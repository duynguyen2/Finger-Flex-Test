# this code will be edited as more physical components comes in
# this file uses pyfirmata, which you need to download and upload the firmata code using Arduino software to use
# we will try to avoid using this unless something comes up as this does not work properly for now
# pyfirmata lets us code the Arduino with just python
import pyfirmata
import time

# from https://www.theamplituhedron.com/articles/How-to-replicate-the-Arduino-map-function-in-Python-for-Raspberry-Pi/
# this is a map function made to replicate what the Arduino map function does
# there's an _ because python has a map function so this is to make it less confusing
def _map(x, in_min, in_max, out_min, out_max):
    return int((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)

# 1023

# reading the board
board = pyfirmata.Arduino('COM3')

# interating through the inputs of the board
it = pyfirmata.util.Iterator(board)
it.start()
time.sleep(1)

# measured voltage from arduino
VCC = 4.81

# measured resistance from each 4.7k resistors
R_DIV1 = 46200.0; # measured resistance of 4.7k resistor 1
R_DIV2 = 46800.0; # measured resistance of 4.7k resistor 2
R_DIV3 = 46500.0; # measured resistance of 4.7k resistor 3

# measured resistance from flex sensors when straight
STRAIGHT_RESISTANCE1 = 26800.0; # measured resistance when straight
STRAIGHT_RESISTANCE2 = 27600.0; # measured resistance when straight
STRAIGHT_RESISTANCE3 = 26200.0; # measured resistance when straight

# measured resistance from flex sensors when bent 90 deg
# possibly off
BEND_RESISTANCE1 = 73500.0; # resistance at 90 deg
BEND_RESISTANCE2 = 72800.0; # resistance at 90 deg
BEND_RESISTANCE3 = 73600.0; # resistance at 90 deg

# Read the ADC, and calculate voltage and resistance from it
flexADC1 = board.get_pin('a:0:i') # reading ADC value from A0
time.sleep(1)
print(flexADC1)
print(flexADC1.read())

flexADC2 = board.get_pin('a:1:i') # reading ADC value from A1
time.sleep(1)
print(flexADC2)
print(flexADC2.read())
    
flexADC3 = board.get_pin('a:3:i') # reading ADC value from A3
time.sleep(1)
print(flexADC3)
print(flexADC3.read())

# infinitely reading flex sensor values
while True:

    # voltage divider calculation for the voltage given the data from ADC
    # the arduino converts the analog voltage to digital 10 bit number, range from 0 to 1023 (2^10)
    flexV1 = flexADC1.read() * VCC / 1023.0
    time.sleep(1)
    flexV2 = flexADC2.read() * VCC / 1023.0
    time.sleep(1)
    flexV3 = flexADC3.read() * VCC / 1023.0
    time.sleep(1)

    # voltage divider calculation to find the flex sensor's resistance
    flexR1 = R_DIV1 * (VCC / flexV1 - 1.0)
    flexR2 = R_DIV2 * (VCC / flexV2 - 1.0)
    flexR3 = R_DIV3 * (VCC / flexV3 - 1.0)

    # Use the calculated resistance to estimate the sensor's
    # bend angle:
    angle1 = _map(flexR1, STRAIGHT_RESISTANCE1, BEND_RESISTANCE1,
                   0, 90.0)
    angle2 = _map(flexR2, STRAIGHT_RESISTANCE2, BEND_RESISTANCE2,
                   0, 90.0)
    angle3 = _map(flexR3, STRAIGHT_RESISTANCE3, BEND_RESISTANCE3,
                   0, 90.0)
  
    print("Resistance1: " + str(flexR1) + " ohms");
    print("Resistance2: " + str(flexR2) + " ohms");
    print("Resistance3: " + str(flexR3) + " ohms");

    print("Bend 1: " + str(angle1) + " degrees");
    print("Bend 2: " + str(angle2) + " degrees");
    print("Bend 3: " + str(angle3) + " degrees");
    print();
    time.sleep(0.5)