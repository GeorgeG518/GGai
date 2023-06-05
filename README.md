# GSAIT: George's Simple Artificial Intelligence Toolkit

First thing is first, I am a covert narcissist so of course I have to have my
name in the acronym. I will come up with a better name eventually.


Mainly doing this as a side project to learn more AI stuff but also work on my
python skills. I anticipate that each module will have its own challenges
and software design patterns. Sure, plenty of this stuff is already implemented
and tools like this exist, but where is the fun in that? Very lame to not do a project
for that reason.

Goals:
	No building required
	Run with basic Anaconda install
	Simple interfaces

## Modules
### *SOS*: simple optimization suite
Long term plan: multiple optimization codes that can leverage an input file format
to optimize a user defined objective function. Users define their control variables, 
limits, optimization method, etc and the code will just do its thing.

This module will be heavily inspired by DAKOTA, but I wanted it to be a bit more lightweight.

General concept will be that the users create a python class that defines an optional Pre Process and post process step (in case it's coupled with other codes). The user
can also define a custom gradient function. A required objective function calculation function that is called after the post process step will need to be defined as the code has
no real way of knowing what to optimize.

The report I wrote for AI will be used as the ground truth of performance for the generalized codes i.e. whatever I get from my new method of reading in an objective function should be the same
as the report.

### *SCS*: Simple Clustering Suite
Similar setup to above. User provides data, code clusterly clusterizes some stuff.

### *SSS*: Simple supervised-learning suite
Was going to be called Simple Categorization suite but SCS was already taken. Made more sense to SSLS anyway.

### *SUS*: Simple Unsupervised-Learning Suite
Simple unsupervised learning suite will be a lot of neural network work or whatever else I want to do.
lol sus amogus

It's probably pretty clear which one I planned the most
