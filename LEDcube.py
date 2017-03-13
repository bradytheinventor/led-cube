#import core functions
from LEDcubeCore import *
from patterns.plot import *
from patterns.plane import *
from patterns.geometric import *
from patterns.rainy import *
from patterns.sine import *
from patterns.points import *
from math import sin, sqrt

"""----DECLARE VARIABLE----"""
threadRunning = True

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
