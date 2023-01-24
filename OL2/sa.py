#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
George Gannon
sa.py
10/6/2022

simulated annealingly optimizes a SOG(gy) function
"""
import numpy as np
import SumofGaussians  as SG
import sys

PRINTONLYLAST = False
EPSILON = 1e-8
ITERMAX = 100_000 # Confession: I learned how to do this on tiktok
DCUBEMAX = 10
STEPSIZE = 0.01
GLOBALMAX = None

def temp_schedule(option, iteration):
    if option ==0:
        return ( 1 - (iteration)/ITERMAX )
    elif option == 1: # random walk
        return ITERMAX
    elif option ==2: # greedy search
        return 0

def simulated_annealing(rng,seed, dims, ncenters):
    sog = SG.SumofGaussians(dims,ncenters,rng)
    location= rng.uniform(size=(dims,))*DCUBEMAX
    GLOBALMAX = location
    
    for i in range(ITERMAX):
        epsilon = rng.uniform(-0.05,0.05,(dims,))
        newlocation = location+epsilon
        if np.any(np.greater_equal(newlocation,10)) :
            wheregreater = np.argwhere(newlocation>10)
            for each in wheregreater:
                newlocation[each[0]]=10
        elif np.any(np.less_equal(newlocation,0)) :
            wheregreater = np.argwhere(newlocation<0)
            for each in wheregreater:
                newlocation[each[0]]=0
    
        temperature = temp_schedule(0, i)
        #temperature = temperature_schedule(1, i) # random walk
        #temperature = temperature_schedule(2, i) # greedy
                    
        if not PRINTONLYLAST: print(" ".join(["{:.8f}".format(each) for each in location]), "{:.8f}".format(sog.Evaluate(location)))   
              
        # if G(y) > G(x) where y = newlocaiton, x = location
        diff_of_locs = sog.Evaluate(newlocation) - sog.Evaluate(location)
        
        if sog.Evaluate(newlocation) > sog.Evaluate(GLOBALMAX):
            GLOBALMAX = newlocation
            
        if sog.Evaluate(newlocation) > sog.Evaluate(location):
            location = newlocation
        elif np.exp(diff_of_locs/temperature) >= rng.random(): # pretty sure np.exp is only 0 to 1, so I think I am good to do this
            location = newlocation
            

            
    # print(" ".join(["{:.8f}".format(each) for each in location]), "{:.8f}".format(sog.Evaluate(location)))   # Old way of doing it
    print(" ".join(["{:.8f}".format(each) for each in location]), "{:.8f}".format(sog.Evaluate(GLOBALMAX)))   
if __name__=='__main__':
    if (len(sys.argv) != 4):
        print()
        print("Usage: ./sa.py int:seed int:dimensions int:numOfGaussians" )
        print()
        sys.exit(1)
    
    seed = int(sys.argv[1])
    dimensions = int(sys.argv[2])
    numGaussians = int(sys.argv[3])   
    rng = np.random.default_rng(seed)   
    simulated_annealing(rng, seed, dimensions, numGaussians)
