#!/usr/bin/env python3
import numpy as np
from matplotlib import pyplot as plt

#properties of the load
M = 10  #mass
l = 10  #Length
b = 2/2 #Height

#acceleration gravity
g = 9.8

#X coordinate of center robot
l1 = 3

#height of right robot
# h  = 0

#change height
dh = -0.01
fh = -5 

#number of step
steps = int(np.abs(fh)/np.abs(dh))

#data
x  = np.zeros(steps)
R0 = np.zeros(steps)
R1 = np.zeros(steps)
R2 = np.zeros(steps)


#Reaction Force
R0[0] = M*g*(l1*l1+3*l*l1-l*l)/(8*l*l1)
R1[0] = M*g*(l1*l1*l1-2*l*l1*l1+l*l*l)/(8*l1*(l-l1)*(l-l1))
R2[0] = M*g*(l1*l1-5*l*l1+3*l*l)/(8*l*(l-l1))

def ReactionForce(step):
    global R0,R1,R2,M,g,dh,l,l1
    h = step*dh
    x[step] = h

    if(h>0):
        R0[step] = M*g*(1/2 + b*h/(l*np.sqrt(l*l-h*h)))
        R1[step] = 0
        R2[step] = M*g*(1/2 - b*h/(l*np.sqrt(l*l-h*h)))
    if(h<0):
        if(l/2<l1):
            R0[step] = M*g*(1-l/(2*l1))
            R1[step] = M*g*(l/(2*l1))
            R2[step] = 0
        if(l/2>l1):
            R0[step] = 0
            R1[step] = M*g*(1/(l-l1))*(l/2+b*h/(np.sqrt((l-l1)*(l-l1)-h*h)))
            R2[step] = M*g*(1/(l-l1))*(l/2-l1-b*h/(np.sqrt((l-l1)*(l-l1)-h*h)))
        if(l1 == l/2):
            R0[step] = 0
            R1[step] = M*g
            R2[step] = 0
    if(h==0):
        R0[step] = R0[0]
        R1[step] = R1[0]
        R2[step] = R2[0]
    



STEP = 0
for i in range(0,steps):
    ReactionForce(STEP) 
    STEP +=1
    

plt.plot(-x,R0,label = "$R_0$")
plt.plot(-x,R1,label = "$R_1$")
plt.plot(-x,R2,label = "$R_2$")
plt.legend()
plt.show()