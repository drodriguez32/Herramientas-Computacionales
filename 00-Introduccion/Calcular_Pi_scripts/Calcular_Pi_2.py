import numpy as np
import matplotlib.pyplot as plt
import random as rm

# Crea una coordenada x,y al azar entre a y b donde b>a
# x = (a - b) * np.random.random_sample((1, 2)) + a

a = 1.0   #radius of the circle
m = 8     #m-1 = max exponent for number of points
PN = 0    #initialize the probability of a point being inside
pi = 0    #initial value for pi 
    
N_a = []  #initialize an array to store the number of coordinate pairs
PN_a = []  #initialize an array to store the probabilities
pi_a = []  #initialize an array to store the approximations for pi
res_a = [] #initialize an array to store the error
    
for n in range(0,m):
    N = 10**n       #number of coordinate pairs
    p_i = 0.0       #points inside
    
    for i in range(0,N-1):
        
        x = rm.uniform(-1,1)   
        y = rm.uniform(-1,1)
        
        if ((x**2)+(y**2)-(a**2)<0):   #check if the coordinate pairs are inside the circle
            p_i = p_i + 1.0   #count how many are inside
            
        PN = p_i/N   #calculate the probability of one coordinate pair being inside
        pi = PN*4    #calculate the value of pi
    
    N_a.append(N)
    PN_a.append(PN)
    pi_a.append(pi)
    res_a.append(PN-(np.pi/4))

    print(pi)

plt.semilogx(N_a,res_a, 'bo')
plt.grid(True) 
plt.xlabel("N - número de puntos")
plt.ylabel("P(N) - pi/4")
