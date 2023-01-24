#!/usr/bin/env python3
"""
George Gannon
kmeans.py

kmeansly does some stuff
"""
import sys
import os
import numpy as np
from numpy.linalg import norm
VERBOSE = False
#from numba import jit
class KMeans:
    def __init__(self, num_clusters, intrain_data, inval_data):
        self.NUM_CLUSTERS = num_clusters
        self.training_data = intrain_data
        self.validation_data = inval_data
        self.cluster_values = np.empty([ self.training_data.shape[0]]) # will be a numpy array of integers representing training_data[i]'s self.clusters index.
        self.centroids = np.zeros( (self.NUM_CLUSTERS, self.training_data.shape[-1]-1))
        self.cluster_category = np.empty([self.NUM_CLUSTERS])
        
    def initialize_centroids(self):
        for i in range(self.NUM_CLUSTERS):
            self.centroids[i] = self.training_data[i][:-1] # don't include category
                  
    def calculate_new_centroids(self):
        for i in range(self.NUM_CLUSTERS):
            cluster_indices = np.where(self.cluster_values==i)
            if VERBOSE: print("test", self.training_data[cluster_indices][:,:-1])
            if self.training_data[cluster_indices][:,:-1].size!=0: 
                newpt = np.mean(self.training_data[cluster_indices][:,:-1], axis=0) # [:,:-1] & -1 for not adding the category
                self.centroids[i] = newpt
    
    def majority_vote(self):
        for i in range(self.NUM_CLUSTERS):
            cluster_indices = np.where(self.cluster_values==i)
            try:
                vals, cts=np.unique(self.training_data[cluster_indices][:,-1], return_counts=True)

                if VERBOSE:print("category ",vals[np.argmax(cts)])
                self.cluster_category[i]=vals[np.argmax(cts)]
            except ValueError:
                continue

    
#@jit                    
def calculate_cluster_ownership(training_data, centroids, cluster_values):
    # A few parts stolen from my github: https://github.com/GeorgeG518/MTSU-CSCI-4600-Summer-2022/blob/6c6cefe2028584a4a5e94f5027fb5efe62d75b2b/Module2/pythontiming.ipynb
    for i,each in enumerate(training_data):
        MIN_DIST = 1.7976931348623157e+308 # kinda big
        for j, cent in enumerate(centroids):  
            distance = norm(each-cent, 2)
            if MIN_DIST > distance: # our distance is smaller
                MIN_DIST = distance
                cluster_values[i]=j
                
def test(kmeans):
    TOTALCORRECT= 0
    for each in kmeans.validation_data:
        MIN_DIST = 1.7976931348623157e+308 # kinda big
        CHOSEN_CLUSTER = None
        
        for i, cent in enumerate(kmeans.centroids): 
            dist = norm(each[:-1]-cent, 2)
            if MIN_DIST > dist: # our distance is smaller
                MIN_DIST = dist
                CHOSEN_CLUSTER=i
        if each[-1] == kmeans.cluster_category[CHOSEN_CLUSTER]:
            TOTALCORRECT+=1
    print(TOTALCORRECT)
    
            

if __name__=='__main__':
    if (len(sys.argv) != 4):
        print()
        print("Usage: ./kmeans.py int: num of clusters string:input training data string:input validation data filename" )
        print()
        sys.exit(1)
    
    num_clusters = int(sys.argv[1])
    intrain_name = str(sys.argv[2])
    inval_name = str(sys.argv[3])
    
    intrain_data = np.loadtxt(intrain_name)
    inval_data = np.loadtxt(inval_name)
    if VERBOSE:print(intrain_data.shape)
    kmeans = KMeans(num_clusters, intrain_data, inval_data)
    kmeans.initialize_centroids()
    converged = False
    
    while not converged:
        prev_iter = np.copy(kmeans.cluster_values)
        calculate_cluster_ownership(kmeans.training_data[:,:-1], kmeans.centroids, kmeans.cluster_values)
        curr_iter_cluster_membership = kmeans.cluster_values
        kmeans.calculate_new_centroids()
        
        if prev_iter.all() == curr_iter_cluster_membership.all():
            converged=True
            
    kmeans.majority_vote()
    for i in range(kmeans.NUM_CLUSTERS):
        cluster_indices = np.where(kmeans.cluster_values==i)
        if VERBOSE:print(kmeans.training_data[cluster_indices])
    if VERBOSE:print(kmeans.cluster_values)
    test(kmeans)
        
    
    
    


    
