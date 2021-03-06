# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 14:33:53 2021

@author: c_ken
"""

import numpy as np
from pylab import *

#call = input('The number of terms of the Fibonacci Sequence: ')
#No = int(call)


# Creating our function for the Fibonacci Sequence
def fib(N): 
    a = 0
    b = 1

    if N == 1 : 
        seq = np.array([a, b])
        
    elif N == 0 : 
        seq = np.array([a])
        
    else: 
        seq = np.array([a, b])
        
        # to create the sequence, I will create a for loop that repeats N times 
        for i in range(1, N):
            c = a + b 
            seq = np.append(seq, c)
            a = b 
            b = c
               
    print(seq)
    #print(len(seq))
    
    #Now to Approximate the Golden Ratio Rn = Fn / Fn-1
    #becuase of my if and elif statments, the c value is called with i + 1
    R = [(seq[i+1]/seq[i]) for i in range(1, len(seq) - 1)]
    plot(R)
    xlabel('Number of Terms (N)')
    ylabel("Golden Ratio")
    print(R)
    
#Using the plot and printed values of the array, it converges when N = 13 to the value of 1.6180

fib(13)
    
    
   


    
