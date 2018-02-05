import numpy as np
import matplotlib.pyplot as plt

def coord_aleat(N_coord):
    x_coord = 2*(np.random.rand(N_coord))-1
    y_coord = 2*(np.random.rand(N_coord))-1
    return x_coord, y_coord

def pi_calc(N,r):
    a = r #radius
    x, y = coord_aleat(N)  # llamar la función para crear coordinadas aleatorias
    pos = [(x**2 + y**2 - a**2) <= 0]  # puntos que están dentro del círculo
    pts_i = np.sum(pos) # sumar la cantidad de puntos
    PN = (pts_i/N)  # probabilidad de que los puntos estén adentro
    error = PN - (np.pi/4)  # el error de la probabilidad calculada
    return error

N_datos = np.logspace(1,6,500)  # creo una lista con la cantidad de datos que voy a tomar
PN_a = []  # arreglo vacío para guardar los datos de error
radius = 1.0  # radio del círculo

for i in N_datos:
    err = pi_calc(int(i),radius)  # llamar la función para calcular pi y guardar el valor del error
    PN_a.append(err) # agregar el error al arreglo
    
plt.semilogx(N_datos,PN_a)
plt.grid(True) 
plt.xlabel("N - número de puntos")
plt.ylabel(" $P(N) - \pi/4$ ")
