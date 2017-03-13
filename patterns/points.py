#this file containes random-point patterns, e.g. voxelRand.

#import points list, time.sleep, random.randint, and fundamental plotting
#   functions
from core import points
from time import sleep
from random import randint
from plot import *

#fills the cube with random voxels
#because this uses a uniform random distribution, it has to run at a much
#   faster speed than other programs to account for the fact that many LEDs are
#   being lit multiple times
def voxelRand(times, speed):
    speed = speed / 5
    voxels = []
    
    #plot random points to fill the cube
    for t in range(times):
        vX = randint(0, 3)
        vY = randint(0, 3)
        vZ = randint(0, 3)
        plot(vX, vY, vZ, 1)
        sleep(speed)
        
    fullcube()
    sleep(speed * 2)
    
    #plot random points to empty the cube
    for t in range(times):
        vX = randint(0, 3)
        vY = randint(0, 3)
        vZ = randint(0, 3)
        plot(vX, vY, vZ, 0)
        sleep(speed)
        
    #smoothly erase any remaining points
    plotFill(0, 3, 0, 3, 3, 3, 0)
    sleep(speed * 2)
    
    plotFill(0, 2, 0, 3, 2, 3, 0)
    sleep(speed * 2)
    
    plotFill(0, 1, 0, 3, 1, 3, 0)
    sleep(speed * 2)
    fullcube(0)
    
    sleep(speed)

#makes a simple firework-like effect
def LFirework(times, speed):
    for t in range(times):
        stars = []

        #draw the firework spiraling up into the 'sky'
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

        #create random firework star 'twinkles'
        fullcube(0)
        for n in range(randint(6, 9)):
            stars.append([randint(0, 2), randint(2, 3), randint(0, 3)])

        #move stars down to the ground
        while stars != []:
            for s in stars:
                plot(s[0], s[1], s[2])
                if s[1] < 3:
                    plot(s[0], s[1]+1, s[2], 0)
                
                if s[1] > 0:
                    s[1] -= 1
                else:
                    stars.remove(s)
                sleep(speed / 4)
