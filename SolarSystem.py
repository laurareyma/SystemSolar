import math
import numpy as np
from scipy.spatial.distance import norm

class Planet:

  def __init__(self, mass, position, speed):
    self.mass = np.array(mass)*1000
    self.position = np.array(position)*1000
    self.speed = np.array(speed)*1000 #Se multiplica por mil para obtener el valor en metros y m/s respectivamente.

def force(m1, r1, m2, r2):

    #Función que calcula la gravedad entre un objeto de masa m1 y posición r1 
    #ejerce sobre otro objeto de masa m2 y posición r2

    #vector de posición

    #m1 -> masa del objeto 1 [kg]
    #r1 -> posición del objeto 1 [m]
    #m2 -> masa del objeto 2 [kg]
    G = 6.67e-11 #constante de gravitación universal [N m^2 / kg^2]

    #calcular la distancia entre los dos objetos
    r21 = r1 - r2
    d = norm(r21) #distancia entre los dos objetos [m]
    run21 = r2 / d #vector unitario que apunta de 1 hacia 2
    #calcular la fuerza

    F = run21 * G * m1 * m2 / d**2
    return F

def accelerationCalc(planet1Mass, planet1Position):
    temp = 0
    for planet in Planets:
      if planet1Mass == planet.mass:
         pass
      else:
        temp = temp + (force(planet.mass, planet.position, planet1Mass, planet1Position))
    accl = temp/planet1Mass
    return accl

Sol = Planet(1.989E+30, 
              [-1.179443251112733E+06, -4.525307891739777E+05, 3.134211075848844E+04], 
              [8.641673046632211E-03, -1.197549843610353E-02, -8.333309545496825E-05])

Mercurio = Planet(3.285E+23, 
                  [-5.604542055485767E+07, -3.485180684223912E+07, 2.252726524219494E+06], 
                  [1.587699012959109E+01, 3.914167832796291E+01, -4.653314021586240E+00])

Venus = Planet(4.867E+24, 
                [-9.124062992562428E+07, -6.007396006977719E+07, 4.409138578373339E+0], 
                [1.909604199335837E+01, -2.937858610658142E+01, -1.504747093789415E+00])

Tierra = Planet(5.972E+24, 
                 [-6.807583303581282E+07, 1.306386634514613E+08, 2.441434724599123E+04], 
                 [-2.700500662780606E+01, -1.367492208542078E+01, -2.819099962243499E-04])

Marte = Planet(6.39E+23, 
                 [-8.418911224084277E+06, -2.186228318767418E+08, -4.363309315665454E+06], 
                 [2.513774699083788E+01, 1.264412795570113E+00, -5.897251116445148E-01])

Jupiter = Planet(1.898E+27, 
                 [5.072890561816115E+08, 5.455564093701284E+08, -1.361280331447470E+07],
                 [9.712016793883137E+00, 9.516945889247435E+00, 1.778637018081355E-01])

Saturno = Planet(5.683E+26, 
                 [1.349171392640714E+09, -5.432565025518103E+08, -4.427101531561103E+07], 
                 [3.069954912732006E+00, 8.940857757866405E+00, -2.774778319351245E-01])

Urano = Planet(8.681E+25, 
                [1.826634011533559E+09, 2.294233899646317E+09, -1.514356969771659E+07],
                [-5.377708713288905E+00, 3.924460766621745E+00, 8.429516133480419E-02])

Neptuno = Planet(1.024E+26, 
                  [4.463673410614180E+09, -2.603336928890301E+08, -9.750858120032202E+07],
                  [2.803376699079932E-01, 5.458300376201279E+00, -1.186959253968582E-01])

Planets = []
Planets.append(Sol)
Planets.append(Mercurio)
Planets.append(Venus)
Planets.append(Tierra)
Planets.append(Marte)
Planets.append(Jupiter)
Planets.append(Saturno)
Planets.append(Urano)
Planets.append(Neptuno)

h = 3600
Nsteps = 3*24*365

def RK(planet):
  planetPosFinal = 0
  for time in range(0,Nsteps):
    print(planet.position)
    k1 = accelerationCalc(planet.mass, planet.position)
    k2 = accelerationCalc(planet.mass, planet.position+planet.speed*h/2+(k1*(h**2)/8))
    k3 = accelerationCalc(planet.mass, planet.position+planet.speed*h/2+(k2*(h**2)/8))
    k4 = accelerationCalc(planet.mass, planet.position+planet.speed*h+(k3*(h**2/2)))
    planet.speed = planet.speed + h*(k1+2*k2+3*k3+k4)/6  # Actualiza la velocidad
    planet.position = planet.position + planet.speed*h + h**2*(k1+k2+k3)/6  # Actualiza la posición
    time = time*h  # Almacena el tiempo actual
  planetPosFinal = planet.position 
  return planetPosFinal/10000

pato =  RK(Sol)
print(pato)