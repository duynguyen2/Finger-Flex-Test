# this is the code to interface with the Arduino using the serial module, which requires uses code from the Arduino software uploaded to the board
# anytime we use the sleep method, that is to give it time to get all the information properly
# to run, use start debugging, if it stops, there's something happening that i'm unsure of or the circuit needs re-adjusting
import bpy
import serial
import time

# initialize the arduino to connect
# COM3 is the port for Duy's Arduino, change to yours accordingly as it may be different
# possibly may change this so that a user may input the com port
# baudrate is the rate of speed that data is being sent, set it whatever you like as long as it matches the Arduino code
arduinoUno = serial.Serial('COM3', baudrate = 19200)
time.sleep(0.4)

# flush will clear any inputs or data left on the serial port
# clearing anything left on the serial port from before
arduinoUno.flushInput()
time.sleep(0.5)

# infinitely checks for flex sensor values from the Arduino and stores them into variables for use
#
while True:

    # flush inputs, so we reset inputs everytime and don't keep the same values from previous runs
    arduinoUno.flushInput()
    time.sleep(0.5)

    # takes each line printed to the serial port, from the arduino code uploaded on the board, and puts it into a variables for resistance
    inputs = arduinoUno.readline().decode('utf-8').strip()
    inputs = inputs.split()

    # converts the data from the Arduino to data types for python, variable names are subject to change to fit our project
    flex1 = float(inputs[0])
    flex2 = float(inputs[1])
    flex3 = float(inputs[2])

    angle1 = float(inputs[3])
    angle2 = float(inputs[4])
    angle3 = float(inputs[5])

    # these prints are to test that they properly are stored as floating points
    print(flex1)
    print(flex2)
    print(flex3)
    print(angle1)
    print(angle2)
    print(angle3)
    print()

    # print the data
    print("Resistance 1: " +  str(flex1))
    print("Resistance 2: " +  str(flex2))
    print("Resistance 3: " +  str(flex3))
    print("Bend 1: " + str(angle1))
    print("Bend 2: " + str(angle2))
    print("Bend 3: " + str(angle3))
    print()

    time.sleep(0.5)