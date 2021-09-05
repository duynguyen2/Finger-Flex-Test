from pygltflib import *
from enum import Enum

class Joint(Enum):

    # enum of each joint
    PROXIMAL_PHALANX = "PROXIMAL PHALANX"
    MIDDLE_PHALANX = "MIDDLE PHALANX"
    DISTAL_PHALANX = "DISTAL PHALANX"

# class to define the finger, to hold the number of flex sensors used and the start position of the finger in degrees(e.g. 90 degrees relative), the different phlanges
# the automatic assumption is the right hand's index finger
class Finger():

    # assuming index finger
    finger = "INDEX"

    # array to keep track of the joint with an indexed flex sensor
    fingerJoints = [Joint.PROXIMAL_PHALANX, Joint.MIDDLE_PHALANX, Joint.DISTAL_PHALANX]
    flexSensors = [0, 1, 2]

    # dictionary to define each joint as an index from 0-2
    fingerDictionary = {
        "ProximalPhalanx": 0,
        "MiddlePhalanx": 1,
        "DistalPhalanx": 2
    }

    # initializing variables for the finger, the following are default values set if no values are passed
    def __init__(self, numOfFlexSensors=3, startPos=90.0):
        self.numOfFlexSensors = numOfFlexSensors
        self.startPos = startPos
    
    # return all values as a string
    def __repr__(self):
        return "# of Flex Sensors: " + str(self.numOfFlexSensors) + " Start Position: " + str(self.startPos)

    # print the class
    def print_test(self):
        print("Finger Class")

    # set the number of Flex Sensors
    def setNumOfFlexSensors(self, numOfFlexSensors):
        self.numOfFlexSensors = numOfFlexSensors

    # set the start position
    def setStartPos(self, startPos):
        self.startPos = startPos
    
    # return the number of flex sensors
    def getNumOfFlexSensors(self):
        return self.flexSensors

    # returns the start position
    def getStartPos(self):
        return self.startPos
    
    # returns the array of joints in order
    def getJoints(self):
        return self.fingerJoints
        
# all the commands below are testing that the class and its methods function correctly

fingerTest1 = Finger(3, 90.0)
# x = Joint.PROXIMAL_PHALANX
# print(x)
# print(str(fingerTest1.fingerJoints))
# print(str(fingerTest1.fingerDictionary))

# fingerTest2 = Finger(1, 45.0)
# fingerTest3 = Finger(2)
# fingerTest4 = Finger(3, 45.0)

# fingerTest1.print_test()
# fingerTest2.print_test()
# fingerTest3.print_test()
# print("# of Flex Sensors for test 1: " + str(fingerTest1.getNumOfFlexSensors()) + " Start Position: " + str(fingerTest1.getStartPos()))
# print("# of Flex Sensors for test 2: " + str(fingerTest2.getNumOfFlexSensors()) + " Start Position: " + str(fingerTest2.getStartPos()))
# print("# of Flex Sensors for test 3: " + str(fingerTest3.getNumOfFlexSensors()) + " Start Position: " + str(fingerTest3.getStartPos()))
# print("# of Flex Sensors for test 4: " + str(fingerTest4.getNumOfFlexSensors()) + " Start Position: " + str(fingerTest4.getStartPos()))

# print(fingerTest1)