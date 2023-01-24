#!/usr/bin/env python3
import numpy as np
import matplotlib
from matplotlib import pyplot as plt
import sys
"""
cat 0.txt |grep "V="| cut -f2 -d"=" | ./stats.py
"""
arr = np.loadtxt(sys.stdin)
print("minimum:", np.round(np.min(arr), 4))
print("median:",np.round(np.median(arr),4))
print("mean:",np.round(np.mean(arr),4))
print("max:",np.round(np.max(arr),4))
print("std:",np.round(np.std(arr),4))


