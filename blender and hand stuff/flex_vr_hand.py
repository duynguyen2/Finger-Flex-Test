# this is the code to interface with the Arduino using the serial module, which requires uses code from the Arduino software uploaded to the board
# to run, use start debugging, if it stops, there's something happening that i'm unsure of or the circuit needs re-adjusting
# currently, all 3 flex sensors interact with the index finger of the hand model
# STATUS: works properly on the first run, continuous runs will vary
# TODO: maybe optimize depending on future plans
import bpy
import math
import serial
import time

# initialize the arduino to connect
# COM3 is the port for Duy's Arduino, change to yours accordingly as it may be different
# possibly may change this so that a user may input the COM port
# baudrate is the rate of speed that data is being sent, set it whatever you like as long as it matches the Arduino code
arduinoUno = serial.Serial('COM3', baudrate = 115200)
time.sleep(2)

# collect the the armatures, other helper variables
hand = bpy.data.objects['Armature']
bpy.ops.object.mode_set(mode = 'POSE')

# setting limits for the finger to bend and scaling it to match the actual bend
lowerLimit = [0, 0, 0]
higherLimit = [1023, 1023, 1023]
actuationAngle = [360, 360, 360]

# setting the axes the finger should rotate in
axis = ['X', 'X', 'X']

# creating an array for each phalanx to change them based on index (rather than making 3 separate variables)
fingerBones = [
    hand.pose.bones['indexProximal'],
    hand.pose.bones['indexMiddle'],
    hand.pose.bones['indexDistal']
]

# set the rotation mode
for bone in range(3):
    fingerBones[bone].rotation_mode = 'XYZ'

# array to store the last value
last = [0, 0, 0]

# this loop takes the values from the Arduino, scales them to a way to bend the finger
for x in range(150):
    # send a signal to the Arduino to retrieve values from the flex sensors
    arduinoUno.write(b'READ\n')
    inputs = arduinoUno.readline()
    print(inputs)
    decodedInputs = inputs.decode().split(' ')
    
    # calculate the values and normalize them
    for bone in range(3):
        extractedValue = float(decodedInputs[bone].rstrip())
        current = ((higherLimit[bone] - extractedValue) * actuationAngle[bone] / (higherLimit[bone] - lowerLimit[bone]))
        if(current < 0):
            current = 0
        
        # rotate the bones based on their respective flex sensor and store the last value
        fingerBones[bone].rotation_euler.rotate_axis(axis[bone], math.radians(current - last[bone]))
        last[bone] = current
        
    # redraw the model in the window
    bpy.ops.wm.redraw_timer(type = 'DRAW_WIN_SWAP', iterations = 1)

bpy.ops.wm.redraw_timer(type = 'DRAW_WIN_SWAP', iterations = 1)
arduinoUno.close()