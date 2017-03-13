#import core functions
import traceback

from LEDcubeCore import *
from patterns.plot import *
from patterns.geometric import *
from patterns.plane import *
from patterns.points import *
from patterns.rainy import *
from patterns.sine import *
from patterns.transitions import *

from math import sin, sqrt
from time import sleep

"""----DECLARE VARIABLE----"""
threadRunning = True

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

    #wait for ENTER to be pressed
    print " "
    print "Connect the LED cube to the Raspberry Pi now."
    raw_input("When you are ready, press ENTER to begin.")
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
    print("Quitting due to exception, stack trace is as follows: ")
    traceback.print_exc()
    
    for transistor in transistors:
        GPIO.output(transistor, 0)
    multiplexer.register1.clear()
    multiplexer.register2.clear()

    #multiplexer.running = False
    raw_input("\nPress ENTER to quit.")

    GPIO.cleanup()
