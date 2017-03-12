import RPi.GPIO as GPIO
import threading
from random import randint
from time import sleep

#code designed for 4x4x4 LED cube, can be modified for larger cubes
#these are the core functions, imported to LEDcube.py, which contains the
#                              patterns and program setup

"""--------------SETUP VARIABLES AND GPIOS---------------"""
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

#setup GPIO outputs
pins = [
    23, #pin 11, transistor 4
    24, #pin 8, transistor 3
    7, #pin 4, transistor 2
    8, #pin 14, transistor 1
    
    12, #pin 18, register 2 CLOCK
    13, #pin 21, register 2 LATCH
    10, #pin 15, register 2 SERIAL DATA
    
    16, #pin 23, register 1 CLOCK
    18, #pin 24, register 1 LATCH
    22] #pin 25, register 1 SERIAL DATA

transistors = [8, 7, 24, 23]

for pin in pins:
    GPIO.setup(pin, GPIO.OUT)

#three-dimensional list containing LED point values
points = [[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
          [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
          [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
          [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]]

"""-------------CLASS DEFINITIONS----------------"""
#this class handles interactions between the code and the physical shift registers
class ShiftRegister():
    def __init__(self, datapin, clockpin, latchpin):
        self.datapin = datapin
        self.clockpin = clockpin
        self.latchpin = latchpin

    def clock(self, n):
        #input data
        if n != "NONE":
            GPIO.output(self.datapin, n)
        #clock clock (whee)
        GPIO.output(self.clockpin, 1)
        GPIO.output(self.clockpin, 0)
        #reset data pin
        if n != "NONE":
            GPIO.output(self.datapin, 0)

    def latch(self):
        #latch and reset register
        GPIO.output(self.latchpin, 1)
        GPIO.output(self.latchpin, 0)

    def clear(self):
        #clear and reset register by filling with low values
        for i in range(16):
            self.clock(0)
        self.latch()

#sequence class, used to run through patterns defined in LEDcube.py
class Sequence():
    def __init__(self, patterns):
        self.patterns = patterns

    def getParameters(self, parameters):
        self.parameters = []
        for i in range(len(self.patterns)):
            self.parameters.append(parameters[i])

    def getTimes(self, reps):
        self.reps = reps

    def run(self, times, speed):
        if times == "infinity":
            times = 10000
        t=times
        while t > 0:
            for p in range(len(self.patterns)):
                if not self.parameters[p] == "N":
                    self.patterns[p](self.parameters[p], self.reps[p], speed)
                else:
                    self.patterns[p](self.reps[p], speed)
            if not t > 9999:
                t -= 1

class threadRunClass():
    def __init__(self, running):
        self.running = running

#this class runs in a separate thread, continuously reading the 'points' list
#   and writing its values to the LED cube
class Multiplexer():
    def __init__(self):
        print("Initializing multiplexer...")
        
        self.running = True
        self.register1 = ShiftRegister(10, 12, 13)
        self.register2 = ShiftRegister(22, 16, 18)

    #the second parameter has to exist for the thread to run, but does nothing
    def multiplex(self, p):
        while self.running:
            for y in range(len(points)):
                #turn previous layer off before updating LEDs
                GPIO.output(transistors[y-1], 0)
                
                for x in range(len(points[y])):
                    for z in range(len(points[y][x])):
                        #pick which register to write to - each controls half
                        #   of the cube
                        if x < 2:
                            self.register2.clock(points[y][x][z])
                        else:
                            self.register1.clock(points[y][x][z])

                #write register values to cube and enable layer
                self.register1.latch()
                self.register2.latch()
                GPIO.output(transistors[y], 1)
                
                sleep(0.001)
