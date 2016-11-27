import random
import numpy as np

def uniform(a,b):
    if a>b:
        t = b
        b = a
        a = b
    return (random.random())*np.abs(a-b) + a

def pi_monteCarlo(N):
    in_pi = 0
    random.seed()
    x = np.zeros((N,))
    y = np.zeros((N,))
    for i in range(N):
        x[i] = uniform(-1,1)
        y[i] = uniform(-1,1)
        d = (x[i]**2 + y[i]**2)
        if np.abs(d) <= 1:
            in_pi +=1
    pi = 4*( in_pi/float(N) )
    return pi, x, y