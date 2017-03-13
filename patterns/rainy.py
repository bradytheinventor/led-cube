#this file contains "rainy" patterns, e.g. rain and voxelSend

#import points list, time.sleep, random.randint, and fundamental plotting
#   functions
from core import points
from time import sleep
from random import randint
from plot import *

#sends random voxels down the y axis, like a rain shower
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
    #fill the top and bottom layers
    plotFill(0, 0, 0, 3, 0, 3)
    plotFill(0, 3, 0, 3, 3, 3)
    sleep(speed)
    
    for t in range(times):
        #select a new point
        vX = randint(0, 3)
        vY = randint(0, 1) * 3
        vZ = randint(0, 3)

        #send it up or down the cube, depending on its starting y-position
        for n in range(0, 4):
            if vY == 0:
                if n > 0:
                    plot(vX, n-1, vZ, 0)
                plot(vX, n, vZ)
                
            elif vY == 3:
                if n > 0:
                    plot(vX, (3-n)+1, vZ, 0)
                plot(vX, (3-n), vZ)
            
            sleep(speed)
