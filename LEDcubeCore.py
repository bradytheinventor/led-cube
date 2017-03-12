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
    
    11, #pin 17, RGB red (register 2 CLEAR)
    12, #pin 18, register 2 CLOCK
    13, #pin 21, register 2 LATCH
    10, #pin 15, register 2 SERIAL DATA
    
    15, #pin 22, RGB green (register 1 CLEAR)
    16, #pin 23, register 1 CLOCK
    18, #pin 24, register 1 LATCH
    22, #pin 25, register 1 SERIAL DATA
    26] #pin something, RGB blue

transistors = [8, 7, 24, 23]

for pin in pins:
    GPIO.setup(pin, GPIO.OUT)

#three-dimensional list containing LED point values
points = [[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
          [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
          [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
          [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]]

"""-------------CLASS DEFINITIONS----------------"""
class ShiftRegister():
    def __init__(self, datapin, clockpin, latchpin, clearpin):
        self.datapin = datapin
        self.clockpin = clockpin
        self.latchpin = latchpin
        self.clearpin = clearpin

        #disable register clearing
        GPIO.output(self.clearpin, 1)

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
        #GPIO.output(self.clearpin, 0)
        #sleep(0.0000001)
        #GPIO.output(self.clearpin, 1)

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

#essential part of the code, this takes a 3D list and outputs it to the cube
class Multiplexer():
    def __init__(self):
        print("Initializing multiplexer...")
        self.running = True
        self.register1 = ShiftRegister(10, 12, 13, 11)
        self.register2 = ShiftRegister(22, 16, 18, 15)

    #the second parameter has to exist, but is ignored by my code,
    #   so I just gave it a fun strange name
    def multiplex(self, fluggamuggachuggahugga):
        while self.running:
            for y in range(len(points)):
                GPIO.output(transistors[y-1], 0)
                for x in range(len(points[y])):
                    for z in range(len(points[y][x])):
                        if x < 2:
                            self.register2.clock(points[y][x][z])
                        else:
                            self.register1.clock(points[y][x][z])
                            
                self.register1.latch()
                self.register2.latch()
                GPIO.output(transistors[y], 1)
                sleep(0.001)
