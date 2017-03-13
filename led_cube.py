"""--------IMPORT MODULES AND PATTERNS--------"""
import traceback

from core import *
from patterns.plot import *
from patterns.geometric import *
from patterns.plane import *
from patterns.points import *
from patterns.rainy import *
from patterns.sine import *
from patterns.transitions import *

from math import sin, sqrt
from time import sleep

"""-----------------SEQUENCES----------------"""
#run a series of patterns a specified number of times
#if the number of times is more than 9999 then the sequence will run forever

#create sequences by passing a list of sublists, where each sublist contains
#   the information for one pattern: name, parameter, and number of repetitions

#if the pattern does not require a parameter, pass "N" to not use one

#sequence 1 is the main function showcase
sequence1 = Sequence([[voxelRand,   "N",                175],
                      [transition,  "start-xbounce",    1],
                      [bounce,      "x",                5],
                      [transition,  "xbounce-xname",    1],
                      [transition,  "xname-xbounce",    1],
                      [transition,  "xbounce-ybounce",  1],
                      [bounce,      "y",                5],
                      [sinewave,    "worm",             5],
                      [sinewave,    "sine",             5],
                      [sinewave,    "bounce",           5],
                      [transition,  "ybounce-xspin",    1],
                      [spin,        "x",                10],
                      [transition,  "xspin-ybounce",    1],
                      [transition,  "ybounce-rain",     1],
                      [rain,        "snow",             64],
                      [transition,  "ybounce-zbounce",  1],
                      [bounce,      "z",                5],
                      [transition,  "zbounce-woopwoop", 1],
                      [woopwoop,    "N",                20],
                      [transition,  "woopwoop-zbounce", 1],
                      [transition,  "zbounce-xbounce",  1],
                      [transition,  "xbounce-ybounce",  1],
                      [voxelSend,   "N",                50],
                      [transition,  "ybounce-xbounce",  1],
                      [bounce,      "x",                5],
                      [transition,  "xbounce-yspin",    1],
                      [spin,        "y",                10],
                      [transition,  "yspin-xbounce",    1],
                      [transition,  "xbounce-end",      1]])

#sequence 2 is a sinewave show-off
sequence2 = Sequence([[transition,  "start-xbounce",    1],
                      [transition,  "xbounce-ybounce",  1],
                      [sinewave,    "worm",             5],
                      [sinewave,    "sine",             5],
                      [sinewave,    "bounce",           5],
                      [voxelRand,   "N",                175]])

#sequence 3 is a spiral show-off
sequence3 = Sequence([[transition,  "start-xbounce",    1],
                      [bounce,      "x",                5],
                      [transition,  "xbounce-spiral",   1],
                      [spiral,      "N",                6],
                      [transition,  "spiral-xbounce",   1],
                      [bounce,      "x",                5],
                      [transition,  "xbounce-end",      1]])

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
    #print error message and stack trace
    print("Quitting due to exception, stack trace is as follows: ")
    traceback.print_exc()

    #clear transistors and shift registers
    for transistor in transistors:
        GPIO.output(transistor, 0)
        
    multiplexer.register1.clear()
    multiplexer.register2.clear()

    #multiplexer.running = False
    raw_input("\nPress ENTER to quit.")

    GPIO.cleanup()
