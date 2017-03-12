#import core functions
from LEDcubeCore import *
from math import sin, sqrt

"""----DECLARE VARIABLE----"""
threadRunning = True

"""----------------PLOT FUNCTIONS---------------"""
#sets a specific LED high or low
def plot(x, y, z, n=1):
    points[y][x][z] = n

#fills from (x1,y1,z1) to (x2,y2,z2) with n
def plotFill(x1, y1, z1, x2, y2, z2, n=1):
    #if point2 > point1, swap them
    if x1 > x2:
        x2Old = x2
        x2 = x1
        x1 = x2Old
    if y1 > y2:
        y2Old = y2
        y2 = y1
        y1 = y2Old
    if z1 > z2:
        z2Old = z2
        z2 = z1
        z1 = z2Old
    for y in range(y1, y2+1):
        for x in range(x1, x2+1):
            for z in range(z1, z2+1):
                plot(x, y, z, n)

#a quick and easy way to use plotRect to light the whole cube
def fullcube(n=1):
    plotFill(0, 0, 0, 3, 3, 3, n)

#and a quick way to clear the whole cube
def clear(n=0):
    plotFill(0, 0, 0, 3, 3, 3, n)

#just in case you like camelCase, this runs the same as fullcube
def fullCube(n=1):
    fullcube(n)

"""-------------------PATTERNS-------------------"""
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
        for n in range(4):
            fullcube(0)
            if axis == "x":
                plotFill(n, 0, 0, n, 3, 3)
            elif axis == "y":
                plotFill(0, n, 0, 3, n, 3)
            elif axis == "z":
                plotFill(0, 0, n, 3, 3, n)
            sleep(speed)
        
        for n in range(4):
            bounceList = [3, 2, 1, 0]
            fullcube(0)
            if axis == "x":
                plotFill(bounceList[n], 0, 0, bounceList[n], 3, 3)
            elif axis == "y":
                plotFill(0, bounceList[n], 0, 3, bounceList[n], 3)
            elif axis == "z":
                plotFill(0, 0, bounceList[n], 3, 3, bounceList[n])
            sleep(speed)

#lights a wireframe cube at the specified point, that's the specified size
def wireframe(time, size, xF=0, yF=0, zF=0):
    fullcube(0)
    if size == 4:
        #fill cube, then cut out inner sections
        fullcube()
        plotFill(1, 0, 1, 2, 3, 2, 0)
        plotFill(1, 1, 0, 2, 2, 3, 0)
        plotFill(0, 1, 1, 3, 2, 2, 0)
    elif size == 3:
        #plot cube relative to (xF, yF, zF)
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
def woopwoop(times, speed, startX=0, sY=0, sZ=0):
    lastCorner=[0, 0, 0]
    cornerList = [0, 0, 0]
    for t in range(times):
        #intro sequence
        if t == 0:
            fullcube(0)
            wireframe(speed, 1, startX, sY, sZ)
            wireframe(speed, 2, startX, sY, sZ)
            wireframe(speed, 3, startX, sY, sZ)
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

#makes a pseudo-sinusoidal pattern
#this will probably use real sines eventually, but for now it's hardcoded
#it also has variants 'sine', 'worm', and 'bounce'
def sinewave(variant="sine", times=1, speed=0.075):
    for t in range(times):
        if variant == "sine":
            if t==0:
                fullcube(0)
                plotFill(0, 0, 0, 3, 0, 3)
                sleep(speed)
                fullcube(0)
                plotFill(0, 0, 0, 3, 0, 2)
                plotFill(0, 1, 3, 3, 1, 3)
                sleep(speed)
                fullcube(0)
                plotFill(0, 0, 0, 3, 0, 1)
                plotFill(0, 1, 2, 3, 1, 2)
                plotFill(0, 2, 3, 3, 2, 3)
                sleep(speed)
            fullcube(0)
            plotFill(0, 0, 0, 3, 0, 0)
            plotFill(0, 1, 1, 3, 1, 1)
            plotFill(0, 2, 2, 3, 2, 2)
            plotFill(0, 3, 3, 3, 3, 3)
            sleep(speed)
            fullcube(0)
            plotFill(0, 1, 0, 3, 1, 0)
            plotFill(0, 2, 1, 3, 2, 1)
            plotFill(0, 3, 2, 3, 3, 3)
            sleep(speed)
            fullcube(0)
            plotFill(0, 2, 0, 3, 2, 0)
            plotFill(0, 3, 1, 3, 3, 2)
            plotFill(0, 2, 3, 3, 2, 3)
            sleep(speed)
            fullcube(0)
            plotFill(0, 3, 0, 3, 3, 1)
            plotFill(0, 2, 2, 3, 2, 2)
            plotFill(0, 1, 3, 3, 1, 3)
            sleep(speed)
            fullcube(0)
            plotFill(0, 3, 0, 3, 3, 0)
            plotFill(0, 2, 1, 3, 2, 1)
            plotFill(0, 1, 2, 3, 1, 2)
            plotFill(0, 0, 3, 3, 0, 3)
            sleep(speed)
            fullcube(0)
            plotFill(0, 2, 0, 3, 2, 0)
            plotFill(0, 1, 1, 3, 1, 1)
            plotFill(0, 0, 2, 3, 0, 3)
            sleep(speed)
            fullcube(0)
            if t==(times-1):
                plotFill(0, 1, 0, 3, 1, 0)
                plotFill(0, 0, 1, 3, 0, 3)
                sleep(speed)
                fullcube(0)
                plotFill(0, 0, 0, 3, 0, 3)
                sleep(speed)
            else:
                plotFill(0, 1, 0, 3, 1, 0)
                plotFill(0, 0, 1, 3, 0, 2)
                plotFill(0, 1, 3, 3, 1, 3)
                sleep(speed)
                fullcube(0)
                plotFill(0, 0, 0, 3, 0, 1)
                plotFill(0, 1, 2, 3, 1, 2)
                plotFill(0, 2, 3, 3, 2, 3)
                sleep(speed)
        elif variant == "worm":
            fullcube(0)
            plotFill(0, 0, 0, 3, 0, 3)
            sleep(speed)
            fullcube(0)
            plotFill(0, 0, 0, 3, 0, 2)
            plotFill(0, 1, 3, 3, 1, 3)
            sleep(speed)
            fullcube(0)
            plotFill(0, 0, 0, 3, 0, 1)
            plotFill(0, 1, 2, 3, 1, 2)
            plotFill(0, 2, 3, 3, 2, 3)
            sleep(speed)
            fullcube(0)
            plotFill(0, 0, 0, 3, 0, 0)
            plotFill(0, 1, 1, 3, 1, 1)
            plotFill(0, 2, 2, 3, 2, 2)
            plotFill(0, 3, 3, 3, 3, 3)
            sleep(speed)
            fullcube(0)
            plotFill(0, 1, 0, 3, 1, 0)
            plotFill(0, 2, 1, 3, 2, 1)
            plotFill(0, 3, 2, 3, 3, 2)
            plotFill(0, 2, 3, 3, 2, 3)
            sleep(speed)
            fullcube(0)
            plotFill(0, 2, 0, 3, 2, 0)
            plotFill(0, 3, 1, 3, 3, 1)
            plotFill(0, 2, 2, 3, 2, 2)
            plotFill(0, 1, 3, 3, 1, 3)
            sleep(speed)
            fullcube(0)
            plotFill(0, 3, 0, 3, 3, 0)
            plotFill(0, 2, 1, 3, 2, 1)
            plotFill(0, 1, 2, 3, 1, 2)
            plotFill(0, 0, 3, 3, 0, 3)
            sleep(speed)
            fullcube(0)
            plotFill(0, 2, 0, 3, 2, 0)
            plotFill(0, 1, 1, 3, 1, 1)
            plotFill(0, 0, 2, 3, 0, 3)
            sleep(speed)
            fullcube(0)
            plotFill(0, 1, 0, 3, 1, 0)
            plotFill(0, 0, 1, 3, 0, 3)
            sleep(speed)
            fullcube(0)
            plotFill(0, 0, 0, 3, 0, 3)
            sleep(speed)
        elif variant == "bounce":
            fullcube(0)
            plotFill(0, 0, 0, 3, 0, 3)
            sleep(speed)
            fullcube(0)
            plotFill(0, 0, 0, 3, 0, 2)
            plotFill(3, 1, 0, 3, 1, 3)
            sleep(speed)
            fullcube(0)
            plotFill(0, 0, 0, 3, 0, 1)
            plotFill(0, 1, 2, 3, 1, 2)
            plotFill(0, 2, 3, 3, 2, 3)
            sleep(speed)
            fullcube(0)
            plotFill(0, 0, 0, 3, 0, 0)
            plotFill(0, 1, 1, 3, 1, 1)
            plotFill(0, 2, 2, 3, 2, 2)
            plotFill(0, 3, 3, 3, 3, 3)
            sleep(speed)
            fullcube(0)
            plotFill(0, 1, 0, 3, 1, 0)
            plotFill(0, 2, 1, 3, 2, 1)
            plotFill(0, 3, 2, 3, 3, 3)
            sleep(speed)
            fullcube(0)
            plotFill(0, 2, 0, 3, 2, 0)
            plotFill(0, 3, 1, 3, 3, 3)
            sleep(speed)
            fullcube(0)
            plotFill(0, 3, 0, 3, 3, 3)
            sleep(speed)
            fullcube(0)
            plotFill(0, 3, 0, 3, 3, 2)
            plotFill(0, 2, 3, 3, 2, 3)
            sleep(speed)
            fullcube(0)
            plotFill(0, 3, 0, 3, 3, 1)
            plotFill(0, 2, 2, 3, 2, 2)
            plotFill(0, 1, 3, 3, 1, 3)
            sleep(speed)
            fullcube(0)
            plotFill(0, 3, 0, 3, 3, 0)
            plotFill(0, 2, 1, 3, 2, 1)
            plotFill(0, 1, 2, 3, 1, 2)
            plotFill(0, 0, 3, 3, 0, 3)
            sleep(speed)
            fullcube(0)
            plotFill(0, 2, 0, 3, 2, 0)
            plotFill(0, 1, 1, 3, 1, 1)
            plotFill(0, 0, 2, 3, 0, 3)
            sleep(speed)
            fullcube(0)
            plotFill(0, 1, 0, 3, 1, 0)
            plotFill(0, 0, 1, 3, 0, 3)
            sleep(speed)

#sends random voxels down the y axis
#this is a slightly resource-demanding program, so it runs at double speed
#has variants 'rain' and 'snow'
def rain(snow=False, times=1, speed=0.075):
    speed = speed / 2
    drops = []
    for t in range(times):
        #create a new drop
        rX = randint(0, 3)
        rZ = randint(0, 3)
        drops.append([rX, 3, rZ])
        #for each raindrop
        for d in drops:
            #move the drop down one voxel, and erase its old position
            if d[1] < 3:
                plot(d[0], d[1]+1, d[2], 0)
            plot(d[0], d[1], d[2])
            sleep(speed)
            #if it hits the ground, stop updating it
            if d[1] == 0:
                if not snow == True and not snow == "snow":
                    plot(d[0], d[1], d[2], 0)
                drops.remove(d)
            d[1] -= 1
        sleep(speed)

#sends random voxels up and down the cube
def voxelSend(times, speed):
    plotFill(0, 0, 0, 3, 0, 3)
    plotFill(0, 3, 0, 3, 3, 3)
    sleep(speed)
    layerL = [3, 2, 1, 0]
    for t in range(times):
        vX = randint(0, 3)
        vY = randint(0, 1) * 3
        vZ = randint(0, 3)

        for n in range(0, 4):
            if vY == 0:
                if n > 0:
                    plot(vX, n-1, vZ, 0)
                plot(vX, n, vZ)
            elif vY == 3:
                if n > 0:
                    plot(vX, layerL[n]+1, vZ, 0)
                plot(vX, layerL[n], vZ)
            sleep(speed)

#fills the cube with random voxels
#this has to run at a much faster speed than other programs
def voxelRand(times, speed):
    speed = speed / 10
    speed = speed * 2
    voxels = []
    #plot random points to fill the cube
    for t in range(times):
        vX = randint(0, 3)
        vY = randint(0, 3)
        vZ = randint(0, 3)
        plot(vX, vY, vZ, 1)
        sleep(speed)
    fullcube()
    sleep(speed*2)
    #plot random points to empty the cube
    for t in range(times):
        vX = randint(0, 3)
        vY = randint(0, 3)
        vZ = randint(0, 3)
        plot(vX, vY, vZ, 0)
        sleep(speed)
    #smoothly erase any remaining points
    plotFill(0, 3, 0, 3, 3, 3, 0)
    sleep(speed*2)
    plotFill(0, 2, 0, 3, 2, 3, 0)
    sleep(speed*2)
    plotFill(0, 1, 0, 3, 1, 3, 0)
    sleep(speed*2)
    fullcube(0)
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
    speed = speed/2
    fullcube(0)
    for t in range(times):
        for val in range(2):
            v = 1 - val
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


"""-------------TRANSITIONS---------------"""
#these are some transitions designed to smooth out jumps between animations
#this is a HUGE function, but there isn't really any way to shrink it

def transition(name, hasToBeHere, speed):
    if name == "start-xbounce":
        plot(0, 0, 0)
        sleep(speed)
        fullcube(0)
        plotFill(0, 0, 0, 0, 0, 1)
        sleep(speed)
        fullcube(0)
        plotFill(0, 0, 0, 0, 0, 2)
        sleep(speed)
        fullcube(0)
        plotFill(0, 0, 0, 0, 0, 3)
        sleep(speed)
        fullcube(0)
        plotFill(0, 0, 0, 0, 1, 3)
        sleep(speed)
        fullcube(0)
        plotFill(0, 0, 0, 0, 2, 3)
        sleep(speed)
        fullcube(0)
        plotFill(0, 0, 0, 0, 3, 3)
        sleep(speed)
    elif name == "xbounce-ybounce":
        fullcube(0)
        plotFill(0, 0, 0, 0, 0, 3)
        plotFill(1, 1, 0, 1, 3, 3)
        sleep(speed)
        fullcube(0)
        plotFill(3, 3, 0, 3, 3, 3)
        plotFill(2, 2, 0, 2, 2, 3)
        plotFill(1, 1, 0, 1, 1, 3)
        plotFill(0, 0, 0, 0, 0, 3)
        sleep(speed)
        fullcube(0)
        plotFill(0, 0, 0, 0, 0, 3)
        plotFill(1, 1, 0, 3, 1, 3)
        sleep(speed)
        fullcube(0)
        plotFill(0, 0, 0, 3, 0, 3)
        sleep(speed)
    elif name == "ybounce-zbounce":
        fullcube(0)
        plotFill(0, 0, 0, 3, 0, 0)
        plotFill(0, 1, 1, 3, 1, 3)
        sleep(speed)
        fullcube(0)
        plotFill(0, 0, 0, 3, 0, 0)
        plotFill(0, 1, 1, 3, 1, 1)
        plotFill(0, 2, 2, 3, 2, 2)
        plotFill(0, 3, 3, 3, 3, 3)
        sleep(speed)
        fullcube(0)
        plotFill(0, 0, 0, 3, 0, 0)
        plotFill(0, 1, 1, 3, 3, 1)
        sleep(speed)
        fullcube(0)
        plotFill(0, 0, 0, 3, 3, 0)
        sleep(speed)
    elif name == "zbounce-xbounce":
        fullcube(0)
        plotFill(0, 0, 0, 0, 3, 0)
        plotFill(1, 0, 1, 3, 3, 1)
        sleep(speed)
        fullcube(0)
        plotFill(0, 0, 0, 0, 3, 0)
        plotFill(1, 0, 1, 1, 3, 1)
        plotFill(2, 0, 2, 2, 3, 2)
        plotFill(3, 0, 3, 3, 3, 3)
        sleep(speed)
        fullcube(0)
        plotFill(0, 0, 0, 0, 3, 0)
        plotFill(1, 0, 1, 1, 3, 3)
        sleep(speed)
        fullcube(0)
        plotFill(0, 0, 0, 0, 3, 3)
        sleep(speed)
    elif name == "ybounce-xbounce":
        plotFill(0, 0, 0, 0, 0, 3)
        plotFill(1, 1, 0, 1, 1, 3)
        plotFill(1, 0, 0, 1, 0, 3, 0)
        sleep(speed)
        plotFill(0, 0, 0, 0, 0, 3)
        plotFill(1, 1, 0, 1, 1, 3)
        plotFill(2, 2, 0, 2, 2, 3)
        plotFill(3, 3, 0, 3, 3, 3)
        plotFill(1, 0, 0, 1, 0, 3, 0)
        plotFill(2, 0, 0, 3, 1, 3, 0)
        plotFill(3, 2, 0, 3, 2, 3, 0)
        sleep(speed)
        plotFill(0, 0, 0, 0, 0, 3)
        plotFill(1, 1, 0, 1, 3, 3)
        plotFill(2, 0, 0, 3, 3, 3, 0)
        sleep(speed)
        fullcube(0)
        plotFill(0, 0, 0, 0, 0, 3)
        sleep(speed)
    elif name == "xbounce-yspin":   #yspin? because it's fun, that's y
        fullcube(0)
        plotFill(0, 0, 0, 0, 3, 0)
        plotFill(1, 0, 1, 1, 3, 3)
        sleep(speed)
        fullcube(0)
        plotFill(0, 0, 0, 0, 3, 0)
        plotFill(1, 0, 1, 1, 3, 1)
        plotFill(2, 0, 2, 2, 3, 2)
        plotFill(3, 0, 3, 3, 3, 3)
        sleep(speed)
        fullcube(0)
    elif name == "ybounce-xspin":
        fullcube(0)
        plotFill(0, 0, 0, 3, 0, 0)
        plotFill(0, 1, 1, 3, 1, 3)
        sleep(speed)
        fullcube(0)
        plotFill(0, 0, 0, 3, 0, 0)
        plotFill(0, 1, 1, 3, 1, 1)
        plotFill(0, 2, 2, 3, 2, 2)
        plotFill(0, 3, 3, 3, 3, 3)
        sleep(speed)
    elif name == "yspin-xbounce":
        fullcube(0)
        plotFill(0, 0, 0, 0, 3, 0)
        plotFill(1, 0, 1, 1, 3, 3)
        sleep(speed)
        fullcube(0)
        plotFill(0, 0, 0, 0, 3, 3)
        sleep(speed*2)
    elif name == "xspin-ybounce":
        fullcube(0)
        plotFill(0, 0, 0, 3, 0, 0)
        plotFill(0, 1, 1, 3, 1, 3)
        sleep(speed)
        fullcube(0)
        plotFill(0, 0, 0, 3, 0, 3)
        sleep(speed)
    elif name == "xbounce-end":
        fullcube(0)
        plotFill(0, 0, 0, 0, 3, 3)
        sleep(speed)
        fullcube(0)
        plotFill(0, 0, 0, 0, 2, 3)
        sleep(speed)
        fullcube(0)
        plotFill(0, 0, 0, 0, 1, 3)
        sleep(speed)
        fullcube(0)
        plotFill(0, 0, 0, 0, 0, 3)
        sleep(speed)
        fullcube(0)
        plotFill(0, 0, 0, 0, 0, 2)
        sleep(speed)
        fullcube(0)
        plotFill(0, 0, 0, 0, 0, 1)
        sleep(speed)
        fullcube(0)
        plot(0, 0, 0)
        sleep(speed)
        plot(0, 0, 0, 0)
    elif name == "zbounce-woopwoop":
        fullcube(0)
        plotFill(0, 0, 0, 3, 2, 0)
        sleep(speed)
        fullcube(0)
        plotFill(0, 0, 0, 3, 1, 0)
        sleep(speed)
        fullcube(0)
        plotFill(0, 0, 0, 3, 0, 0)
        sleep(speed)
        fullcube(0)
        plotFill(0, 0, 0, 2, 0, 0)
        sleep(speed)
        fullcube(0)
        plotFill(0, 0, 0, 1, 0, 0)
        sleep(speed)
        plot(0, 0, 0)
        sleep(speed)
    elif name == "woopwoop-zbounce":
        fullcube(0)
        wireframe(0, 4)
        plot(1, 1, 3)
        sleep(speed)
        plot(2, 2, 3)
        sleep(speed)
        plot(1, 2, 3)
        sleep(speed)
        plot(2, 1, 3)
        sleep(speed)
        fullcube(0)
        wireframe(0, 4)
        plotFill(0, 0, 3, 3, 3, 3, 0)
        plotFill(0, 0, 2, 3, 3, 2)
        sleep(speed)
        fullcube(0)
        wireframe(0, 4)
        plotFill(0, 0, 2, 3, 3, 3, 0)
        plotFill(0, 0, 1, 3, 3, 1)
        sleep(speed)
        fullcube(0)
        plotFill(0, 0, 0, 3, 3, 0)
        sleep(speed)
    elif name == "ybounce-rain":
        fullcube(0)
        plotFill(0, 0, 0, 3, 0, 3)
        sleep(speed)
        fullcube(0)
        plotFill(0, 1, 0, 3, 1, 3)
        sleep(speed)
        fullcube(0)
        plotFill(0, 2, 0, 3, 2, 3)
        sleep(speed)
        fullcube(0)
        plotFill(0, 3, 0, 3, 3, 3)
        sleep(speed)
    elif name == "xbounce-spiral":
        fullcube(0)
        plotFill(0, 0, 0, 0, 3, 3)
        sleep(speed)
        plotFill(1, 0, 0, 1, 3, 3)
        sleep(speed)
        plotFill(2, 0, 0, 2, 3, 3)
        sleep(speed)
        fullcube()
        sleep(speed*3)
        fullcube(0)
        plotFill(1, 2, 2, 3, 0, 0)
        sleep(speed)
        fullcube(0)
        plotFill(2, 1, 1, 3, 0, 0)
        sleep(speed)
        fullcube(0)
        plot(3, 0, 0)
        sleep(speed)
    elif name == "spiral-xbounce":
        fullcube(0)
        plot(3, 3, 0)
        sleep(speed)
        plotFill(2, 1, 1, 3, 0, 0)
        sleep(speed)
        plotFill(1, 2, 2, 3, 0, 0)
        sleep(speed)
        fullcube()
        sleep(speed*3)
        plotFill(3, 0, 0, 3, 3, 3, 0)
        sleep(speed)
        plotFill(2, 0, 0, 2, 3, 3, 0)
        sleep(speed)
        plotFill(1, 0, 0, 1, 3, 3, 0)
        sleep(speed)
    elif name == "ybounce-yname":
        fullcube(0)
        plotFill(0, 0, 0, 3, 0, 3)
        sleep(speed)
        fullcube(0)
        plotFill(0, 0, 2, 3, 0, 3)
        sleep(speed)
        fullcube(0)
        plotFill(0, 0, 3, 3, 0, 3)
        plot(0, 0, 2)
        plot(1, 0, 1)
        plot(2, 0, 2)
        sleep(speed)
    elif name == "yname-rain":
        plotFill(0, 3, 0, 3, 3, 0)
        sleep(speed)
        plotFill(0, 3, 1, 3, 3, 1)
        sleep(speed)
        plotFill(0, 3, 2, 3, 3, 2)
        sleep(speed)
    elif name == "xbounce-xname":
        fullcube(0)
        plotFill(0, 0, 0, 0, 3, 3)
        sleep(speed)
        fullcube(0)
        plotFill(1, 0, 0, 1, 3, 3)
        sleep(speed)
        fullcube(0)
        plotFill(2, 0, 0, 2, 3, 3)
        sleep(speed)
        fullcube(0)
        plotFill(3, 0, 0, 3, 3, 3)
        sleep(speed)
        plotFill(3, 0, 0, 3, 3, 0)
        sleep(speed)
    elif name == "xname-xbounce":
        plotFill(0, 0, 1, 0, 3, 3)
        sleep(speed)
        fullcube(0)
        plotFill(0, 0, 0, 0, 3, 3)
        sleep(speed)

#a firework-like effect
def LFirework(times, speed):
    for t in range(times):
        stars = []
        for n in range(4):
            fullcube(0)
            plot(0, n, 1)
            sleep(speed)
            fullcube(0)
            plot(0, n, 2)
            sleep(speed)
            fullcube(0)
            plot(1, n, 2)
            sleep(speed)
            fullcube(0)
            plot(1, n, 1)
            sleep(speed)
        fullcube(0)
        plot(0, 3, 1)
        plot(2, 3, 1)
        plot(1, 3, 0)
        plot(1, 3, 2)
        sleep(speed)
        fullcube(0)
        for n in range(randint(6, 9)):
            stars.append([randint(0, 2), randint(2, 3), randint(0, 3)])

        while stars != []:
            for s in stars:
                plot(s[0], s[1], s[2])
                if s[1] < 3:
                    plot(s[0], s[1]+1, s[2], 0)
                
                if s[1] > 0:
                    s[1] -= 1
                else:
                    stars.remove(s)
                sleep(speed/4)
                    
        

"""-----------------SEQUENCES----------------"""
#run a series of patterns a specified number of times
#if times is more than 9999 or is "infinity" then the sequence will go forever

#sequence 1 is the main function showcase
sequence1 = Sequence([voxelRand, transition, bounce, transition,
                      transition, transition, bounce, sinewave, sinewave, sinewave,
                      transition, spin, transition, transition, rain,
                      transition, bounce, transition, woopwoop, transition,
                      transition, transition, voxelSend, transition,
                      bounce, transition, spin, transition, transition])
sequence1.getParameters(["N", "start-xbounce", "x", "xbounce-xname",
                         "xname-xbounce", "xbounce-ybounce", "y", "worm",
                         "sine", "bounce", "ybounce-xspin", "x",
                         "xspin-ybounce", "ybounce-rain", "snow",
                         "ybounce-zbounce", "z", "zbounce-woopwoop", "N",
                         "woopwoop-zbounce", "zbounce-xbounce",
                         "xbounce-ybounce", "N", "ybounce-xbounce", "x",
                         "xbounce-yspin", "y", "yspin-xbounce", "xbounce-end"])
sequence1.getTimes([175, 1, 5, 1, 1, 1, 5, 5, 5, 5, 1, 10, 1, 1, 64, 1,
                    5, 1, 20, 1, 1, 1, 50, 1, 5, 1, 10, 1, 1])

#sequence 2 is a sinewave show-off
sequence2 = Sequence([transition, transition, sinewave, sinewave, sinewave,
                       voxelRand])
sequence2.getParameters(["start-xbounce", "xbounce-ybounce", "worm", "sine",
                         "bounce", "N"])
sequence2.getTimes([1, 1, 5, 5, 5, 1])

#sequence 3 is a spiral show-off
sequence3 = Sequence([transition, bounce, transition, spiral, transition,
                      bounce, transition])
sequence3.getParameters(["start-xbounce", "x", "xbounce-spiral", "N",
                         "spiral-xbounce", "x", "xbounce-end"])
sequence3.getTimes([1, 5, 1, 6, 1, 5, 1])

"""---------------MAIN FUNCTION----------------"""
try:
    #setup multiplexer and shift registers
    multiplexer = Multiplexer()
    
    #clear the shift registers
    multiplexer.register1.clear()
    multiplexer.register2.clear()

    #wait for ENTER to be pressed (the variable is never used, so I gave it a fun name!)
    print " "
    print "If it's unplugged, connect the LED cube to the Raspberry Pi now."
    whistlingPeanutsAndJugglingHippos = raw_input("Press ENTER to begin.")
    print " "
    sleep(0.25)
    
    #start multiplexing thread
    print("Starting multiplexer thread...")
    multiplexerThread=threading.Thread(target=multiplexer.multiplex,args=(15,))
    multiplexerThread.daemon=True
    multiplexerThread.start()

    #run through sequences
    print "Running..."

    sequence2.run(1, 0.075)
    sleep(2)
    sequence3.run(1, 0.075)
    sleep(2)
    sequence1.run(1, 0.075)
    
    #clear transistors and shift registers
    print "Cleaning up resources..."
    for transistor in transistors:
        GPIO.output(transistor, 0)
    multiplexer.register1.clear()
    multiplexer.register2.clear()
    print "Done."

    #multiplexer.running = False
    GPIO.cleanup()

except KeyboardInterrupt:
    #clear transistors and shift registers
    print "\nCleaning up resources..."
    for transistor in transistors:
        GPIO.output(transistor, 0)
    multiplexer.register1.clear()
    multiplexer.register2.clear()

    print "Quitting due to KeyboardInterrupt (CTRL-C)."
    #multiplexer.running = False
    
    GPIO.cleanup()

except:
    #clear transistors and shift registers
    print("Quitting due to unknown error, details are as follows:")
    for transistor in transistors:
        GPIO.output(transistor, 0)
    multiplexer.register1.clear()
    multiplexer.register2.clear()

    #multiplexer.running = False
    #another fun variable name
    flyingRhinocerousesAreAwesome = raw_input("\nPress ENTER to quit.")

    GPIO.cleanup()
