import serial
import numpy
import matplotlib
import time

arduinoUno = serial.Serial('COM3', baudrate = 19200)
time.sleep(0.5)
arduinoUno.flushInput()
time.sleep(0.5)

while True:
    
    # takes each line of string from the arduino code uploaded on the board and puts it into a variables for resistance
    arduinoUno.flushInput()
    time.sleep(1)

    inputs = arduinoUno.readline().decode('utf-8').strip()
    inputs = inputs.split()
    flex1 = float(inputs[0])
    flex2 = float(inputs[1])

    flex3 = float(inputs[2])

    # takes each line of string from the arduino code uploaded on the board and puts it into a variables for resistance
    angle1 = float(inputs[3])
    angle2 = float(inputs[4])
    angle3 = float(inputs[5])

    # print(flex1)
    # print(flex2)
    # print(flex3)
    # print(angle1)
    # print(angle2)
    # print(angle3)
    # print()

    print("Resistance 1: " +  str(flex1))
    print("Resistance 2: " +  str(flex2))
    print("Resistance 3: " +  str(flex3))
    print("Bend 1: " + str(angle1))
    print("Bend 2: " + str(angle2))
    print("Bend 3: " + str(angle3))
    print()

    time.sleep(1)