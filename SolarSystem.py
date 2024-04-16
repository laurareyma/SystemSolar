import math
import numpy as np

class Planeta:

  def __init__(self, masa, posicion, velocidad):
    self.masa = masa*1000
    self.posicion = posicion*1000
    self.velocidad = velocidad*1000 #Se multiplica por mil para obtener el valor en metros y m/s respectivamente.

def fuerza(m1, m2, r1, r2):

    #Función que calcula la gravedad entre un objeto de masa m1 y posición r1 
    #ejerce sobre otro objeto de masa m2 y posición r2

    #vector de posición

    #m1 -> masa del objeto 1 [kg]
    #r1 -> posición del objeto 1 [m]
    #m2 -> masa del objeto 2 [kg]
    G = 6.67e-11 #constante de gravitación universal [N m^2 / kg^2]

    #calcular la distancia entre los dos objetos
    r2 = np.array(r1) - np.array(r2)

    d = np.linalg.norm(r2) #distancia entre los dos objetos [m]
    d = math.sqrt(r2[0]**2 + r2[1]**2 + r2[2]**2) #distancia entre los dos objetos [m]

    run21 = r2 / d #vector unitario que apunta de 1 hacia 2
    
    #calcular la fuerza

    F = run21 * G * m1 * m2 / d**2
    return F

Sol = Planeta(1.989E+30, 
              [-1.179443251112733E+06, -4.525307891739777E+05, 3.134211075848844E+04], 
              [8.641673046632211E-03, -1.197549843610353E-02, -8.333309545496825E-05])

Tierra = Planeta(5.972E+24, 
                 [-6.807583303581282E+07, 1.306386634514613E+08, 2.441434724599123E+04], 
                 [-2.700500662780606E+01, -1.367492208542078E+01, -2.819099962243499E-04])

#calcular la fuerza
F = fuerza(Sol.masa, Tierra.masa, Sol.posicion, Tierra.posicion)
print(F)
