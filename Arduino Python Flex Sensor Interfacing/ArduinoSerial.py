# this is the code to interface with the Arduino using the serial module, which requires uses code from the Arduino software uploaded to the board
# anytime we use the sleep method, that is to give it time to get all the information properly
# to run, use start debugging, if it stops, there's something happening that i'm unsure of or the circuit needs re-adjusting
import serial
import time
import xlsxwriter
#import xlwt

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

testwb = xlsxwriter.Workbook("testdata.xlsx")
sheet1 = testwb.add_worksheet("Sheet 1")

# keep track of what lines we are writing the data in the excel sheet
row = 0
# col = 0

# infinitely checks for flex sensor values from the Arduino and stores them into variables for use
while True:

    # this try statement will try to run all the code under it, if an error occurs then it goes to the except statement
    # try:
        # flush inputs, so we reset inputs everytime and don't keep the same values from previous runs
        arduinoUno.flushInput()
        time.sleep(0.1)

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
        dataFloat = [flex1, flex2, flex3, angle1, angle2, angle3]
        
        dataString = ["Resistance 1: ", "Resistance 2: ", "Resistance 3: ",
        "Bend 1: ", "Bend 2: ", "Bend 3: "]

        for count, line in enumerate(dataString):
            print(line, str(dataFloat[count]))
        print()
        
        for count, line in enumerate(dataString):
            sheet1.write(row, 0, line)
            sheet1.write(row, 1, dataFloat[count])
            sheet1.write(row, 2, line)
            sheet1.write(row, 3, dataFloat[count])
            #col += 1
            row += 1
            # if count < 2:
            #     col = 0
            # else:
            #     continue
            # time.sleep(0.2)
        
        time.sleep(1)

        # x = input("Proceed? Y OR N: ")
        # if x == "Y" or x == "y":
        #     continue

        # if x == "N" or x == "n":
        #     arduinoUno.close()
        #     testwb.close()
        #     print("Exiting")
        #     break
        
        # while x != "n" and x != "N" and x != "y" and x != "Y":
        #     x = input("Invalid response, input again, Y OR N: ")

    # if any error occurs in the try statement, it closes everything and exits the program
    # except:
    #     arduinoUno.close()
    #     testwb.close()
    #     print("An error occured, exiting")
    #     break