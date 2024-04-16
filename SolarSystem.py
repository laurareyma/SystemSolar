import math
import numpy as np

class Planeta:
  def __init__(self, peso, posX, posY, posZ, VoX, VoY, VoZ):
    self.peso = peso*1000
    self.posX = posX*1000
    self.posY = posY*1000
    self.posZ = posZ*1000
    self.VoX = VoX*1000
    self.VoY = VoY*1000
    self.VoZ = VoZ*1000

Mercurio = Planeta()
Venus = Planeta()
Tierra = Planeta()
Marte = Planeta()
Saturno = Planeta()
Urano = Planeta()
Jupiter = Planeta()
Neptuno = Planeta()


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

#definir las masas y posiciones de los objetos
m1 = 54564654654e-10 #masa del objeto 1 [kg]
r1 = [141654646116165, 51561654654121654654, 5365464651654654651] #posición del objeto 1 [m]
m2 = 54564654654e-10 #masa del objeto 2 [kg]
r2 = [546546546e-18, 546546546546e10, 5465465e-4] #posición del objeto 2 [m]

#calcular la fuerza
F = fuerza(m1, m2, r1, r2)
print(F)
