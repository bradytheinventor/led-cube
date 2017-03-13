#this file contains plane-related patterns, e.g. patterns that bounce planes
#   across the cube or spin them around the cube

#import fundamental plotting functions and time.sleep
from plot import *

from time import sleep

#spins a plane around the specified axis
def spin(axis, times, speed):
    for t in range(times):
        if axis == "x":
            fullcube(0)
            plotFill(0, 0, 0, 3, 0, 0)
            plotFill(0, 1, 1, 3, 1, 1)
            plotFill(0, 2, 2, 3, 2, 2)
            plotFill(0, 3, 3, 3, 3, 3)
            sleep(speed)
            
            fullcube(0)
            plotFill(0, 0, 1, 3, 1, 1)
            plotFill(0, 2, 2, 3, 3, 2)
            sleep(speed)
            
            fullcube(0)
            plotFill(0, 0, 2, 3, 1, 2)
            plotFill(0, 2, 1, 3, 3, 1)
            sleep(speed)
            
            fullcube(0)
            plotFill(0, 3, 0, 3, 3, 0)
            plotFill(0, 2, 1, 3, 2, 1)
            plotFill(0, 1, 2, 3, 1, 2)
            plotFill(0, 0, 3, 3, 0, 3)
            sleep(speed)
            
            fullcube(0)
            plotFill(0, 1, 2, 3, 1, 3)
            plotFill(0, 2, 0, 3, 2, 1)
            sleep(speed)
            
            fullcube(0)
            plotFill(0, 1, 0, 3, 1, 1)
            plotFill(0, 2, 2, 3, 2, 3)
            sleep(speed)
            
        elif axis == "y":
            fullcube(0)
            plotFill(0, 0, 0, 0, 3, 0)
            plotFill(1, 0, 1, 1, 3, 1)
            plotFill(2, 0, 2, 2, 3, 2)
            plotFill(3, 0, 3, 3, 3, 3)
            sleep(speed)
            
            fullcube(0)
            plotFill(0, 0, 1, 1, 3, 1)
            plotFill(2, 0, 2, 3, 3, 2)
            sleep(speed)
            
            fullcube(0)
            plotFill(0, 0, 2, 1, 3, 2)
            plotFill(2, 0, 1, 3, 3, 1)
            sleep(speed)
            
            fullcube(0)
            plotFill(0, 0, 3, 0, 3, 3)
            plotFill(1, 0, 2, 1, 3, 2)
            plotFill(2, 0, 1, 2, 3, 1)
            plotFill(3, 0, 0, 3, 3, 0)
            sleep(speed)
            
            fullcube(0)
            plotFill(1, 0, 2, 1, 3, 3)
            plotFill(2, 0, 0, 2, 3, 1)
            sleep(speed)
            
            fullcube(0)
            plotFill(1, 0, 0, 1, 3, 1)
            plotFill(2, 0, 2, 2, 3, 3)
            sleep(speed)

        elif axis == "z":
            fullcube(0)
            plotFill(3, 0, 0, 3, 0, 3)
            plotFill(2, 1, 0, 2, 1, 3)
            plotFill(1, 2, 0, 1, 2, 3)
            plotFill(0, 3, 0, 0, 3, 3)
            sleep(speed)
            
            fullcube(0)
            plotFill(0, 2, 0, 1, 2, 3)
            plotFill(2, 1, 0, 3, 1, 3)
            sleep(speed)
            
            fullcube(0)
            plotFill(0, 1, 0, 1, 1, 3)
            plotFill(2, 2, 0, 3, 2, 3)
            sleep(speed)
            
            fullcube(0)
            plotFill(0, 0, 0, 0, 0, 3)
            plotFill(1, 1, 0, 1, 1, 3)
            plotFill(2, 2, 0, 2, 2, 3)
            plotFill(3, 3, 0, 3, 3, 3)
            sleep(speed)
            
            fullcube(0)
            plotFill(1, 0, 0, 1, 1, 3)
            plotFill(2, 2, 0, 2, 3, 3)
            sleep(speed)
            fullcube(0)
            plotFill(2, 0, 0, 2, 1, 3)
            plotFill(1, 2, 0, 1, 3, 3)
            sleep(speed)

#bounces a plane along the specified axis
def bounce(axis, times, speed):
    for t in range(times):
        #move the plane along in one direction
        for n in range(4):
            fullcube(0)
            if axis == "x":
                plotFill(n, 0, 0, n, 3, 3)
            elif axis == "y":
                plotFill(0, n, 0, 3, n, 3)
            elif axis == "z":
                plotFill(0, 0, n, 3, 3, n)
            sleep(speed)

        #send the plane back
        for n in range(4):
            fullcube(0)
            if axis == "x":
                plotFill(3-n, 0, 0, 3-n, 3, 3)
            elif axis == "y":
                plotFill(0, 3-n, 0, 3, 3-n, 3)
            elif axis == "z":
                plotFill(0, 0, 3-n, 3, 3, 3-n)
            sleep(speed)
