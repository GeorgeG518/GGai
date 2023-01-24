#!/usr/bin/env python3
"""
george gannon
9/14/2022 10:50 PM

random_board.py
Takes in a board from standard input as well as two command line args: seed and number of moves.
At the end it outputs the board configuration.
"""

import datastructures as ds # my python file with all of the datastructures.
import numpy as np
import sys, random

if (len(sys.argv) != 3):
    print()
    print("Usage: ./random_board.py int[Seed] int[Number of Moves]" )
    print()
    sys.exit(1)

random.seed(int(sys.argv[1])) # seed da random generatin
moves = int(sys.argv[2])


inputs = []
inputs=np.loadtxt(sys.stdin) # reed da input 

randomstate = ds.state(inputs)
for i in range(moves): # shuffle da boar
    randmove=random.randrange(4) 
    newstate=None
    if randmove==0:
        newstate=randomstate.up()
    elif randmove==1:
        newstate=randomstate.down()
    elif randmove==2:
        newstate=randomstate.left()
    elif randmove==3:
        newstate=randomstate.right()        
    if newstate!=None: # ignore the moves.
        randomstate=newstate
        
print(randomstate)