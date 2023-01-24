#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
George Gannon
greedy.py
10/6/2022

Greedily does some stuff
"""
import numpy as np
import SumofGaussians  as SG
import sys
PRINTONLYLAST = False
EPSILON = 1e-8
ITERMAX = 100_000 # Confession: I learned how to do this on tiktok
DCUBEMAX = 10
STEPSIZE = 0.01
np.set_printoptions(precision=8)
def greedy(rng,seed, dims, ncenters):
    sog = SG.SumofGaussians(dims,ncenters,rng)

    location= rng.uniform(size=(dims,))*DCUBEMAX
    for i in range(ITERMAX):
        increment =  STEPSIZE*sog.Gradient(location)
        
        location= location +increment
        
        newsoggy = sog.Evaluate(location) # soggy
        
        if not PRINTONLYLAST: print(" ".join(["{:.8f}".format(each) for each in location]), "{:.8f}".format(newsoggy))

        if np.sum(increment) <= EPSILON:
            break
    print(" ".join(["{:.8f}".format(each) for each in location]), "{:.8f}".format(newsoggy))
    
if __name__=='__main__':
    if (len(sys.argv) != 4):
        print()
        print("Usage: ./greedy.py int:seed int:dimensions int:numOfGaussians" )
        print()
        sys.exit(1)
    
    seed = int(sys.argv[1])
    dimensions = int(sys.argv[2])
    numGaussians = int(sys.argv[3])   
    rng = np.random.default_rng(seed)   
    greedy(rng,seed, dimensions, numGaussians)