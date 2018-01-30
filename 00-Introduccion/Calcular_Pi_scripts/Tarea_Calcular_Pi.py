import numpy as np
import matplotlib.pyplot as plt

# Crea una coordenada x,y al azar entre a y b donde b>a
# x = (a - b) * np.random.random_sample((1, 2)) + a

a = 1.0   #radius of the circle
m = 8     #m-1 = max exponent for number of points
PN = 0    #initialize the probability of a point being inside
pi = 0    #initial value for pi 
    
N_a = np.zeros([1,m])   #initialize an array to store the number of coordinate pairs
PN_a = np.zeros([1,m])  #initialize an array to store the probabilities
pi_a = np.zeros([1,m])  #initialize an array to store the approximations for pi
    
for n in range(0,m):
    N = 10**n       #number of coordinate pairs

    p_i = 0.0       #points inside
    
    pts = (1+1) * np.random.random_sample((N, 2)) - 1   #generate an array with N number of random coordinate pairs for which 

    for i in range(0,N-1):
        if (((np.linalg.norm(pts[i])**2)-(a**2))<0):   #check if the coordinate pairs are inside the circle
            p_i = p_i + 1.0   #count how many are inside
            
        PN = p_i/N   #calculate the probability of one coordinate pair being inside
        pi = PN*4    #calculate the value of pi
    
    N_a[0,n] = N
    PN_a[0,n] = PN-(np.pi/4)
    pi_a[0,n] = pi
    
    print(pi)

plt.semilogx(N_a,PN_a, 'bo')
plt.grid(True) 
plt.xlabel("N - número de puntos")
plt.ylabel("P(N) - pi/4")
