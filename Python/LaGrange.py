# Implementación del interpolador de Lagrange y algunos casos de salida.

from math import *


def LagrangePol(datos):

    def L(k, x): # pol Lk(x) = Q i 6= k x−xi xk−xi

        out = 1.0
        for i, p in enumerate(datos):
            if i != k:
                out *= (x-p[0])/(datos[k][0]-p[0])
        return out

    def P(x): # polinomio P(x) = P k f(xk)Lk(x)
        lag = 0.0
        for k, p in enumerate(datos):
            lag += p[1]*L(k, x)
        return lag

    return P

# datos para f(x) = 1 x con x0 = 2, x1 = 2.75 y x2 = 4
datosf = [(2.0, 1.0/2.0), (11.0/4.0, 4.0/11.0), (4.0, 1.0/4.0)]
Pf = LagrangePol(datosf)
print (" \n" +r" -- Polinomio de Lagrange en x=3: " +" \n")
print (Pf(3))

# datos g(x) = sin(3x), x0 = 1, x1 = 1.3, x2 = 1.6, x3 = 1.9 y x4 = 2.2
datosg = [(1.0, 0.1411), (1.3, -0.6878), (1.6, -0.9962),
          (1.9, -0.5507), (2.2, 0.3115)]
Pg = LagrangePol(datosg)
print (" \n" +r" -- Polinomio de Lagrange en x=1.5: " +" \n")
print (Pg(1.5))