#!/usr/bin/env python3
"""
george gannon
9/14/2022 10:50 PM

a-star.py
Takes in a board from standard input as well as one command line arg:  the heuristic
"""
import datastructures as ds # my python file with all of the datastructures.
import numpy as np
import sys
STACKDEBUG = True
GOAL = np.array([[0,1,2],[3,4,5],[6,7,8]])
# Only support 0 heuristic atm
def a_star(cl, frontier):
    
    found = False
    while frontier.notEmpty():
        currexpansion = frontier.pop()
        if ds.MAXN < cl.length() +  frontier.length():
            ds.MAXN=cl.length() +  frontier.length()
        # First we do da goalcheck
        if np.array_equal(currexpansion.state.tiles,GOAL):
            goal_found(currexpansion, cl, frontier)
            return currexpansion
        else:

            generate_children(currexpansion,frontier, cl)
            cl.add(currexpansion.state)
            
def goal_found(lastnode, CL, frontier):
    V = CL.length() # we only visited the ones in the closed list
    N = V + frontier.length() # Nodes visited are in memory, and so are the ones in the frontier
    d = lastnode.depth
    print("V=", V)
    print("N=", ds.MAXN)
    print("d=", d)
    # https://math.stackexchange.com/questions/3409419/calculate-base-of-exponent-from-result
    # N = b**d -> N ** 1/d
    b = ds.MAXN ** (1.0/d)
    print("b=", b)
    print()
    
    currnode = lastnode
    stack = [currnode]
    while currnode.parent != None:
        stack.append(currnode.parent)
        currnode = currnode.parent
    if STACKDEBUG:
        while len(stack) >0:
            print(stack.pop().state)

def generate_children(currnode, frontier, CL):
    currleft =currnode.state.left()
    if currleft != None and CL.isMember(currleft) == False:
        frontier.push(ds.node(currleft, currnode))
        
    currright = currnode.state.right()
    if currright != None and CL.isMember(currright) == False:
        frontier.push(ds.node(currright,currnode))
        
    currup = currnode.state.up()
    if currup != None and CL.isMember(currup) == False:
        frontier.push(ds.node(currup,currnode))

    currdown = currnode.state.down()
    if currdown != None and CL.isMember(currdown) == False:
        frontier.push(ds.node(currdown,currnode))
    
    pass




if __name__=='__main__':
    if (len(sys.argv) != 2):
        print()
        print("Usage: ./a-star.py heuristic[0 for None]" )
        print()
        sys.exit(1)

    initialtiles=np.loadtxt(sys.stdin) # reed da input 
    ds.HEURISTIC = int(sys.argv[1])
    
    openlist = ds.PriorityQueue()
    closedlist = ds.Set()
    
    initialstate = ds.state(initialtiles)
    
    rootnode = ds.node(initialstate, None)
    openlist.push(rootnode)
    
    a_star(closedlist, openlist)
