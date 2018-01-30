import numpy as np
import matplotlib.pyplot as plt

def coord_aleat(N_coord):
    x_coord = 2*(np.random.rand(N_coord))-1
    y_coord = 2*(np.random.rand(N_coord))-1
    return x_coord, y_coord

def pi_calc(N,r):
    a = r #radius
    x, y = coord_aleat(N)
    pos = [(x**2 + y**2 - a**2) <= 0]
    pts_i = np.sum(pos)
    PN = (pts_i/N)
    error = PN - (np.pi/4)
    return error

N_datos = np.logspace(1,7,500)
PN_a = []
radius = 1.0

for i in N_datos:
    err = pi_calc(int(i),radius)
    PN_a.append(err)
    
plt.semilogx(N_datos,PN_a)
plt.grid(True) 
plt.xlabel("N - número de puntos")
plt.ylabel("P(N) - pi/4")
