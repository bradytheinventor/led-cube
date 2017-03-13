# led-cube
This repository contains the code for my Raspberry Pi-based 4x4x4 LED cube. The
original version of this code was written many years ago, before I built the LED
cube featured in my Instructable.

When I wrote the original code, I did not have a very good grasp of programming
style. The code worked well, but was very messy and hard to understand. This
repository is an attempt to clear up the code and make it easier to understand.


The main file 'led_cube.py' imports core operations from 'core.py' and patterns
from the subdirectory '/patterns', and can be run by executing 'sudo python led_cube.py'.

'core.py' contains code to update the LED cube display. This code runs in a
separate thread at program start, in sort of a 'set-and-forget' manner.

'/patterns/plot.py' contains the fundamental plotting functions, which act
as the interface between the display updater and the patterns.

When making your own patterns, you can either put them inside one of the
existing module files (which group patterns according to what they do) or create
your own module file. If you add your own module file, you will have to import
it at the top of 'led_cube.py' by adding 'from patterns.<file> import *'.


The LED cube is choreographed by Sequence objects, which are built from patterns
defined in files in the '/patterns' subdirectory. Sequences require patterns to
accept three parameters: a "variation" string, the number of repetitions, and
the number of seconds to wait between 'frames' of the pattern. These three
parameters, along with the function name, are passed to the Sequence on creation
in a list.

The Sequence can be run with sequence.run(n, dt), where n is the number of
times the Sequence should run (and if n > 9999, the Sequence runs forever) and
dt is the time in seconds between frames. The Sequence class is somewhat
restrictive, so you don't have to use it if your patterns are more complicated.

At the bottom of 'led_cube.py' there is a marked section, put your patterns
and sequence runs inside that section.
