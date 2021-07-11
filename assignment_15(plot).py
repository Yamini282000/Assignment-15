# -*- coding: utf-8 -*-
"""Assignment-15.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1B_t3GZ6M1TwUwxpoLmkkqLTLIkAFty-c
"""

import numpy as np
import matplotlib.pyplot as plt


O = np.array(([0,0]))

def ellipse_gen(a,b):
	len = 50
	theta = np.linspace(0,2*np.pi,len)
	x_ellipse = np.zeros((2,len))
	x_ellipse[0,:] = a*np.cos(theta)
	x_ellipse[1,:] = b*np.sin(theta)
	x_ellipse = (x_ellipse.T + O).T
	return x_ellipse

#Generate line points
def line_gen(A,B):
  len =10
  x_AB = np.zeros((2,len))
  lam_1 = np.linspace(0,1,len)
  for i in range(len):
    temp1 = A + lam_1[i]*(B-A)
    x_AB[:,i]= temp1.T
  return x_AB

#Standard Ellipse
a = 3
b = 4
x = ellipse_gen(a,b)

#Vertices
A1 = np.array([a,0])
A2 = -A1
B1 = np.array([0,b])
B2 = -B1
# Plotting points
A = np.array([0,4]) 
B = np.array([-2.598,-2])
C = np.array([2.598,-2])
D = np.array([0,-2])
#Plotting the ellipse
plt.plot(x[0,:],x[1,:],'b' ,label='ellipse')

#Generating lines
x_AB = line_gen(A,B)
x_BC = line_gen(B,C)
x_CA = line_gen(C,A)

# Axes
l = np.array([0,5]) 
m = np.array([0,-5]) 
p = np.array([-5,0]) 
q = np.array([5,0]) 
x_lm = line_gen(l,m)
x_pq = line_gen(p,q)
plt.plot(x_lm[0,:],x_lm[1,:])
plt.plot(x_pq[0,:],x_pq[1,:])


#Plotting all lines
plt.plot(x_AB[0,:],x_AB[1,:],label='$AB$')
plt.plot(x_BC[0,:],x_BC[1,:],label='$BC$')
plt.plot(x_CA[0,:],x_CA[1,:],label='$CA$')

#Labelling points
plt.plot(0,0, 'o')
plt.text(-0.7 ,-0.3,'O')
plt.plot(0,4, 'o')
plt.text(0.4 ,4.2,'A')
plt.plot(-2.598,-2, 'o')
plt.text(-3.2 ,-1.7,'B')
plt.plot(2.596,-2,'o')
plt.text(2.9,-2.1,'C')
plt.plot(0,-2,'o')
plt.text(0.3,-2.5,'D')

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')

plt.show()