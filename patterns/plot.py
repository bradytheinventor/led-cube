#this file contains the fundamental plotting functions; all other patterns
#   should use these to write to the 'points' list

#import points list
from core import points

#sets a specific LED high or low
def plot(x, y, z, n=1):
    points[y][x][z] = n

#fills from (x1,y1,z1) to (x2,y2,z2) with n
def plotFill(x1, y1, z1, x2, y2, z2, n=1):
    #if point1 > point2, swap them
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

    #fill in points
    for y in range(y1, y2+1):
        for x in range(x1, x2+1):
            for z in range(z1, z2+1):
                plot(x, y, z, n)

#a quick and easy way to use plotRect to light the whole cube
def fullcube(n=1):
    plotFill(0, 0, 0, 3, 3, 3, n)

#and an overloaded version for those who like consistent camelCase
def fullCube(n=1):
    fullcube(n)

#and a quick way to clear the whole cube
def clear(n=0):
    plotFill(0, 0, 0, 3, 3, 3, n)
    
