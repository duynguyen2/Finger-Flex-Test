# this code will be edited as more physical components comes in
import pyfirmata
import time

board = pyfirmata.Arduino('/dev/ttyACM0')

# i believe this just toggles the LED depending 
while True:
    board.digital[13].write(1)
    time.sleep(1)
    board.digital[13].write(0)
    time.sleep(1)