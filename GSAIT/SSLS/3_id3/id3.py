#!/usr/bin/env python3
"""
George Gannon
id3.py

id threely does some stuff

cat iris-data.txt | ./split.bash 10 python id3.py >> temp-10.txt
"""
import sys
import os
import numpy as np
VERBOSE = False # Controls debugging output. swap to true to have an absolutely massive amount of output

class ID3Node:
    def __init__(self, terminal = False):
        self.training_data = None
        self.validation_data = None
        self.attribute = None # index/category to split
        self.left = None
        self.right = None
        self.indices = None
        self.training_entropy = None
        self.splitpt = None # value to split by
        self.terminal = terminal
        self.category = None # THis will only be something if the terminal value is true
    
class ID3Tree:
    def __init__(self, intrain_data, inval_data):
        self.root = ID3Node()
        if len(intrain_data.shape) < 2:
            self.root.training_data = np.array([intrain_data])
        else:
            self.root.training_data = intrain_data
         
        if len(inval_data.shape) < 2:
            self.root.validation_data = np.array([inval_data])
        else:
            self.root.validation_data = inval_data
        self.MAXGAIN = -1
        self.root.indices = np.argsort(self.root.training_data,axis=0)
        self.train(self.root)

        
    def test(self, vector):
        got_right = 0
        category = None
        node = self.root

        while(node.terminal == False):
            if vector[node.attribute] < node.splitpt:
                node = node.left
                if VERBOSE: print('left')
            else:
                node = node.right
                if VERBOSE: print('right')    
                
        category= node.category

        if category == vector[-1]:
            got_right+=1
        else:
            if VERBOSE: print("wrong",category, vector)
        return got_right
    
        
    def traverse(self, node, LorR):
        if(node.terminal == True):
            if VERBOSE:print("terminal", LorR, node.category)
            return node.category
        if VERBOSE:print(LorR, node.attribute, node.splitpt)        
        self.traverse(node.left, "L")
        self.traverse(node.right, "R")
        
    def cant_split(self,data):
        sortedcatvec = data[:, -1]
        entr =self.entropy_calc(sortedcatvec)
        if(entr< 1e-8):
            return True
        if(len(np.unique(data[:,-1]))>1):
            return False
        return True
    
    
    def train(self, node):
        self.MAXGAIN = -1
        left=None
        right=None
        
        sortedbycat=np.array(node.training_data[node.indices[:,-1]])
                
        sortedcatvec = sortedbycat[:, -1]
        node.training_entropy = self.entropy_calc(sortedcatvec)       
        if(self.cant_split(sortedbycat)):
            node.terminal = True
            if VERBOSE:print('sorted',sortedcatvec)
            vals, counts = np.unique(sortedcatvec, return_counts = True)
            index = np.argmax(counts)
            node.category = sortedcatvec[index]
            return
        
        elif node.training_entropy <1e-8: # ik i'm checking in the cant split function, but i haven't tested if i can remove this
            node.terminal = True
            node.category = sortedcatvec[0]
            # TODO: determine what to do if it is a terminal node.
            return            


        if VERBOSE:
            print("whole data",node.training_entropy) # entropy calc is correct

        for i in range(node.indices.shape[1]-1):
            sortedwhole=np.array(node.training_data[node.indices[:,i]])
            sortedvec = sortedwhole[:, i]
            seps = np.where(np.roll(sortedvec,1)!=sortedvec)[0]
            for j,each in enumerate(seps):
                if each==0: continue  # dont split with first element.  
                else:
                    
                    seperator = (sortedvec[each]+sortedvec[each-1]) / 2    
                    left = np.where(sortedwhole[:,i] < seperator)[0] # can't remember why I need to index the first element, but it's in my code
                    right =np.where(sortedwhole[:,i] >= seperator)[0]
                    
                    L_entropy = self.entropy_calc(sortedwhole[left, -1])
                    R_entropy = self.entropy_calc(sortedwhole[right, -1])

                    
                    slide27_L=(len(left)/sortedwhole.shape[0])*L_entropy
                    slide27_R=(len(right)/sortedwhole.shape[0])*R_entropy
                    
                    minEXA=slide27_L+slide27_R # slide 25
                    if  node.training_entropy- minEXA > self.MAXGAIN:
                        self.MAXGAIN =  node.training_entropy- minEXA
                        node.attribute = i
                        node.splitpt = seperator # I think?
                        
                    if VERBOSE:
                        if self.MAXGAIN==node.training_entropy- minEXA:
                            print("checking", seperator, "left", L_entropy, "right",
                                  R_entropy, "Gain",node.training_entropy- minEXA, "(MAX)")
                        else:
                            print("checking", seperator, "left", L_entropy, "right", 
                                  R_entropy, "Gain",node.training_entropy- minEXA)
        


        
        
        left_node = ID3Node()
        left_node.training_data = node.training_data[np.where(node.training_data[:,node.attribute] < node.splitpt)]
        node.left = left_node
        left_node.indices = np.argsort(left_node.training_data,axis=0) # might be better in constructor

        
        right_node = ID3Node()
        right_node.training_data = node.training_data[np.where(node.training_data[:,node.attribute] >= node.splitpt)]
        node.right = right_node
        right_node.indices = np.argsort(right_node.training_data,axis=0) # might be better in constructor
        
        
        if VERBOSE:
            print("SPLIT NODE", node.attribute, node.splitpt)
            print("left", left_node.training_data,left_node.training_data.shape)
            print('attr', node.attribute,'\nLess than', node.splitpt)
            print("right",right_node.training_data, right_node.training_data.shape)
        # RECURSION
        self.train(left_node)
        self.train(right_node)
        
        # TODO: see if there is an iris id3 result somwhere and work it out by hand
        # use that to determine split points, make a new text file and run the program
        
    def entropy_calc(self,arr):
        nums, counts = np.unique(arr,return_counts=True)
        # slide 27, supervised learning
        totalsamples = np.sum(counts)
        
        sumofentropy = 0
        for i,each in enumerate(counts):
            sumofentropy-=(each/totalsamples)*np.log2(each/totalsamples)
                                      
        return sumofentropy
        

    
if __name__=='__main__':
    if (len(sys.argv) != 3):
        print()
        print("Usage: ./id3.py string:input training data string:input validation data filename" )
        print()
        sys.exit(1)

    intrain_name = str(sys.argv[1])
    inval_name = str(sys.argv[2])
    
    intrain_data = np.loadtxt(intrain_name)
    inval_data = np.loadtxt(inval_name)
    da_id_tree = ID3Tree(intrain_data, inval_data)
    da_id_tree.traverse(da_id_tree.root, "Root")
    correct = 0
    for each in da_id_tree.root.validation_data:
        correct+=da_id_tree.test(each)
    print(correct)
    
    
