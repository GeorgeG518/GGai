#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
George Gannon
datastructures.py
THis is all of the data structures contained in one file so that way I can keep everything consolidated.
All of them are from heapq_test.py and also set_test.py.

OG Comments:
Created on Wed Sep 11 20:26:15 2019

@author: Joshua L. Phillips
Department of Computer Science
Middle Tennessee State University
Illustration of heapq and operator overloading

Portions based on Python code provided by
Scott P. Morton
Center for Computational Science
Middle Tennessee State University
"""
import copy
import heapq
import numpy as np
from numpy.linalg import norm
GOAL = np.array([[0,1,2],[3,4,5],[6,7,8]])
# The Frontier
class PriorityQueue():
    def __init__(self):
        self.thisQueue = []
    def push(self, thisNode):
        heapq.heappush(self.thisQueue, (thisNode.totalcost, -thisNode.id, thisNode))
    def pop(self):
        return heapq.heappop(self.thisQueue)[2]
    def isEmpty(self):
        return len(self.thisQueue) == 0
    def notEmpty(self):
        return len(self.thisQueue) > 0
    def length(self):
        return len(self.thisQueue)
    
# The Closed List
class Set():
    def __init__(self):
        self.thisSet = set()
    def add(self,entry):
        if entry is not None:
            self.thisSet.add(entry.__hash__())
    def length(self):
        return len(self.thisSet)
    def isMember(self,query):
        return query.__hash__() in self.thisSet
    
HEURISTIC = 0
nodeid = 0
MAXN = 0
class node():
    def __init__(self,val,parent):
        global nodeid
        self.id = nodeid
        nodeid += 1
        self.state = val # changed it to say state :)
        self.parent = parent
        self.hcost = 0
        self.totalcost = None
        
        if parent != None:
            self.depth = parent.depth+1
        else:
            self.depth=0
            
        if HEURISTIC == 0:
            self.totalcost = self.depth
        elif HEURISTIC == 1:
            self.hcost = self.displaced()
        elif HEURISTIC==2:
            self.hcost = self.manhattan()
        elif HEURISTIC ==3:
            self.hcost = self.myheuristic()
            
        self.totalcost = self.depth+self.hcost
        
    def manhattan(self):
        # start with a zero sum
        sumofmanhattan = 0
        
        for i,eachrow in enumerate(self.state.tiles):
            for j,num in enumerate(eachrow):
                goalindex = np.argwhere(GOAL==num)[0] # give me the index in the goal array that contains the current number
                stateindex = np.array([i, j])
                # l1 norm of the indexes: https://github.com/GeorgeG518/MTSU-CSCI-4600-Summer-2022/blob/main/Module3/linalgnotebook.ipynb
                sumofmanhattan+=norm(stateindex-goalindex,1) 
        return sumofmanhattan
    
    
    def myheuristic(self):
        """
        GOAL state:
        0 1 2
        3 4 5
        6 7 8
        
        My heuristic operates like a checksum of sorts. We take each column and row and add them up for the
        goal state. Then we do the same for the current state and take the absolute difference between the two. 
        this number should tend towards zero as the state is closer.
        
        Example:
        10-9 |11-12| |15-15|
        1 0 2  3-3
        3 4 5 12-12
        6 7 8 21 -21
        
        = 1
        
        Functionally it is similar to heuristic one, but the more wrong the puzzle is, the higher it should go:
        8 7 6
        5 4 3
        2 1 0
        
        = 6 + 0 + 6 + 18 + 0  + 18 
        = 48
        """
        
        colsums = np.sum(self.state.tiles, 0)
        rowsums = np.sum(self.state.tiles, 1)
        c1 = np.abs(colsums[0]-9)
        c2 = np.abs(colsums[1]-12)
        c3 = np.abs(colsums[2]-15)
        r1 = np.abs(rowsums[0]-3)
        r2 = np.abs(rowsums[1]-12)
        r3 = np.abs(rowsums[2]-21)

        #print(c1 + c2 +c3 + r1 + r2+ r3) # for debugging
        return (c1 + c2 +c3 + r1 + r2+ r3)

    def displaced(self):
        totaldisplaced = len(np.argwhere(self.state.tiles!=GOAL))
        return totaldisplaced
    
    def __str__(self):
        return 'Node: id=%d val=%d'%(self.id,self.val)

class state():
    def __init__(self, curr_tiles):
        self.tiles = curr_tiles
        self.xpos, self.ypos = self.find_zero(curr_tiles)
        
    def find_zero(self, tiles):
        zeros= np.argwhere(tiles==0)
        return zeros[0][0] ,  zeros[0][1]
        
    def left(self):
        if (self.ypos == 0):
            return None
        s = self.copy()
        s.tiles[s.xpos][s.ypos] = s.tiles[s.xpos][s.ypos-1]
        s.ypos -= 1
        s.tiles[s.xpos][s.ypos] = 0
        return s
    def right(self):
        if (self.ypos == 2):
            return None
        s = self.copy()
        s.tiles[s.xpos][s.ypos] = s.tiles[s.xpos][s.ypos+1]
        s.ypos += 1
        s.tiles[s.xpos][s.ypos] = 0
        return s
    def up(self):
        if (self.xpos == 0):
            return None
        s = self.copy()
        s.tiles[s.xpos][s.ypos] = s.tiles[s.xpos-1][s.ypos]
        s.xpos -= 1
        s.tiles[s.xpos][s.ypos] = 0
        return s
    def down(self):
        if (self.xpos == 2):
            return None
        s = self.copy()
        s.tiles[s.xpos][s.ypos] = s.tiles[s.xpos+1][s.ypos]
        s.xpos += 1
        s.tiles[s.xpos][s.ypos] = 0
        return s
    def __hash__(self):
        return (tuple(self.tiles[0]),tuple(self.tiles[1]),tuple(self.tiles[2]))
    def __str__(self):
        return '%d %d %d\n%d %d %d\n%d %d %d\n'%(
                self.tiles[0][0],self.tiles[0][1],self.tiles[0][2],
                self.tiles[1][0],self.tiles[1][1],self.tiles[1][2],
                self.tiles[2][0],self.tiles[2][1],self.tiles[2][2])
    def copy(self):
        s = copy.deepcopy(self)
        return s
