# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 14:33:53 2021

@author: c_ken
"""


import numpy as np
from pylab import *

# Creating our function for the Fibonacci Sequence
def fib(N): 
    a = 0
    b = 1
    
    if N == 1: 
        seq = np.array([a])
        print(seq)
    else: 
        seq = np.array([a, b])
        # to create the sequence, I will create a for loop that repeats N times 
        for i in range(1, N):
            c = a + b 
            new = np.array([c])
            a = b 
            b = c
            additions = np.append(new, [c])
            

    final = np.append(seq, additions)       
    print(final)
        

        
fib(6)

# to create the sequence, I will create a for loop that repeats N times 