from pygltflib import *
import enum

# class to define the finger, to hold the number of flex sensors used and the start position of the finger in degrees(e.g. 90 degrees relative), the different phlanges
# the automatic assumption is the right hand's index finger
class Finger():
    
    # enum of each joint
    PROXIMAL_PHALANX = "PROXIMAL PHALANX"
    MIDDLE_PHALANX = "MIDDLE PHALANX"
    DISTAL_PHALANX = "DISTAL PHALANX"

    # assuming index finger
    finger = "INDEX"

    # array to keep track of the joint with an indexed flex sensor
    fingerJoints = ["ProximalPhalanx", "MiddlePhalanx", "DistalPhalanx"]
    flexSensors = [0, 1, 2]

    # initializing variables for the finger, the following are default values set if no values are passed
    def __init__(self, numOfFlexSensors=3, startPos=90.0):
        self.numOfFlexSensors = numOfFlexSensors
        self.startPos = startPos
    
    # return values as a string
    def __repr__(self):
        return "# of Flex Sensors: " + str(self.numOfFlexSensors) + " Start Position: " + str(self.startPos)

    def print_test(self):
        print("Finger Class")

    def setNumOfFlexSensors(self, numOfFlexSensors):
        self.numOfFlexSensors = numOfFlexSensors

    def setStartPos(self, startPos):
        self.startPos = startPos
    
    def getNumOfFlexSensors(self):
        return self.flexSensors

    def getStartPos(self):
        return self.startPos
        
fingerTest1 = Finger(3, 90.0)

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