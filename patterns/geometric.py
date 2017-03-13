#this file contains geometric shape-related patterns, i.e. patterns that draw
#   or manipulate geometric shapes more complicated than lines and planes

#import points list, time.sleep, random.randint, and fundamental plotting
#   functions
from LEDcubeCore import points
from time import sleep
from random import randint
from plot import *

#lights a wireframe cube at the specified point of the specified size
def wireframe(time, size, xF=0, yF=0, zF=0):
    fullcube(0)
    if size == 4:
        #if the cube is size 4, it fills the whole LED cube and thus can ignore
        #   the start point (xF, yF, zF)
        
        #fill cube, then cut out inner sections
        fullcube()
        plotFill(1, 0, 1, 2, 3, 2, 0)
        plotFill(1, 1, 0, 2, 2, 3, 0)
        plotFill(0, 1, 1, 3, 2, 2, 0)
        
    elif size == 3:
        #if the cube is smaller than size 4, plot cube relative to (xF, yF, zF)
        plotFill(xF, yF, zF, xF+2, yF+2, zF+2)
        plotFill(xF+1, yF, zF+1, xF+1, yF+2, zF+1, 0)
        plotFill(xF+1, yF+1, zF, xF+1, yF+1, zF+2, 0)
        plotFill(xF, yF+1, zF+1, xF+2, yF+1, zF+1, 0)
        
    elif size == 2:
        plotFill(xF, yF, zF, xF+1, yF+1, zF+1)
        
    elif size == 1:
        plot(xF, yF, zF)
    
    sleep(time)

#zooms a wireframe cube in and out of random corners
def woopwoop(times, speed, sX=0, sY=0, sZ=0):
    lastCorner=[0, 0, 0]
    cornerList = [0, 0, 0]
    
    for t in range(times):
        #play intro sequence
        if t == 0:
            fullcube(0)
            wireframe(speed, 1, sX, sY, sZ)
            wireframe(speed, 2, sX, sY, sZ)
            wireframe(speed, 3, sX, sY, sZ)
            wireframe(speed, 4)
            
        #pick a random corner that's different than last time
        while cornerList == lastCorner:
            cX = randint(0, 1)
            cY = randint(0, 1)
            cZ = randint(0, 1)
            cornerList = [cX, cY, cZ]

        #shrink to the corner, then enlarge out of it
        fullcube(0)
        wireframe(speed, 4)
        wireframe(speed, 3, cX, cY, cZ)
        wireframe(speed, 2, cX*2, cY*2, cZ*2)
        wireframe(speed, 1, cX*3, cY*3, cZ*3)
        sleep(speed)
        
        wireframe(speed, 2, cX*2, cY*2, cZ*2)
        wireframe(speed, 3, cX, cY, cZ)
        wireframe(speed, 4)

        #update lastCorner
        lastCorner = cornerList
        
        sleep(speed)

#plots a sphere inside the cube
def sphere(time):
    fullcube(0)
    plotFill(1, 0, 1, 2, 3, 2)
    plotFill(1, 1, 0, 2, 2, 3)
    plotFill(0, 1, 1, 3, 2, 2)
    sleep(time)

#spins a point in circles to create a cylinder, then repeats to erase itself
def spiral(times, speed):
    #this function naturally runs slower than most, so speed is divided by 2
    #   to normalize speed
    speed = speed/2
    
    fullcube(0)
    for t in range(times):
        #alternate between plotting 1 and 0
        for val in range(2):
            v = 1 - val

            #draw the spiraling point, then move up a layer
            for n in range(4):
                plotFill(1, n, 0, 2, n, 0, v)
                sleep(speed)
                
                plot(1, n, 0, v)
                plot(0, n, 1, v)
                sleep(speed)
                
                plotFill(0, n, 1, 0, n, 2, v)
                sleep(speed)
                
                plot(0, n, 2, v)
                plot(1, n, 3, v)
                sleep(speed)
                
                plotFill(1, n, 3, 2, n, 3, v)
                sleep(speed)
                
                plot(2, n, 3, v)
                plot(3, n, 2, v)
                sleep(speed)
                
                plotFill(3, n, 1, 3, n, 2, v)
                sleep(speed)
                
                plot(3, n, 1, v)
                if n < 3:
                    plot(2, n+1, 0, v)
                sleep(speed)

