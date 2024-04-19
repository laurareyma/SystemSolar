import math
import numpy as np
from scipy.spatial.distance import norm

class Planet:
  def __init__(self, nombre, mass, position, speed):
    self.nombre = nombre
    self.mass = np.array(mass)
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

Planets = []

Sol = Planet("Sol", 1.989E+30, 
              [-1.179443251112733E+06, -4.525307891739777E+05, 3.134211075848844E+04], 
              [8.641673046632211E-03, -1.197549843610353E-02, -8.333309545496825E-05])

Mercurio = Planet("Mercurio", 3.285E+23, 
                  [-5.604542055485767E+07, -3.485180684223912E+07, 2.252726524219494E+06], 
                  [1.587699012959109E+01, 3.914167832796291E+01, -4.653314021586240E+00])

Venus = Planet("Venus", 4.867E+24, 
                [-9.124062992562428E+07, -6.007396006977719E+07, 4.409138578373339E+0], 
                [1.909604199335837E+01, -2.937858610658142E+01, -1.504747093789415E+00])

Tierra = Planet("Tierra", 5.972E+24, 
                 [-6.807583303581282E+07, 1.306386634514613E+08, 2.441434724599123E+04], 
                 [-2.700500662780606E+01, -1.367492208542078E+01, -2.819099962243499E-04])

Marte = Planet("Marte", 6.39E+23, 
                 [-8.418911224084277E+06, -2.186228318767418E+08, -4.363309315665454E+06], 
                 [2.513774699083788E+01, 1.264412795570113E+00, -5.897251116445148E-01])

Jupiter = Planet("Jupiter", 1.898E+27, 
                 [5.072890561816115E+08, 5.455564093701284E+08, -1.361280331447470E+07],
                 [9.712016793883137E+00, 9.516945889247435E+00, 1.778637018081355E-01])

Saturno = Planet("Saturno", 5.683E+26, 
                 [1.349171392640714E+09, -5.432565025518103E+08, -4.427101531561103E+07], 
                 [3.069954912732006E+00, 8.940857757866405E+00, -2.774778319351245E-01])

Urano = Planet("Urano", 8.681E+25, 
                [1.826634011533559E+09, 2.294233899646317E+09, -1.514356969771659E+07],
                [-5.377708713288905E+00, 3.924460766621745E+00, 8.429516133480419E-02])

Neptuno = Planet("Neptuno", 1.024E+26, 
                  [4.463673410614180E+09, -2.603336928890301E+08, -9.750858120032202E+07],
                  [2.803376699079932E-01, 5.458300376201279E+00, -1.186959253968582E-01])

Ganímedes_Luna_Jupiter = Planet("Ganímedes (JIII)", 1.482E+23,
                                [5.079070599985498E+08, 5.464283675677761E+08, -1.357086017775604E+07],
                                [-1.858346269200461E+01, 1.582973414762908E+01, 2.937100137013733E-01])

Luna_Tierra = Planet("Luna", 7.3E+22,
                    [-6.773677209009242E+07, 1.307964854608734E+08, 2.769446864134818E+04],
                    [-2.740275578400834E+01, -1.271092519226561E+01, 9.149857821719465E-02])

Titan_Luna_Jupiter = Planet("Titan (SVI)", 1.345E+23,
                            [1.349704800759490E+09, -5.423110088905436E+08, -4.481177099723300E+07],
                            [-1.876954276198388E+00, 1.146819868966134E+01, -1.088036948437308E+00])

Calisto_Luna_Jupiter = Planet("Calisto (JIV)", 1.075938E+23,
                              [5.054390744241988E+08, 5.459686638832101E+08,-1.362459464487553E+07],
                              [-1.150432589728793E+01, 1.571931395124353E+00, -9.506025312649641E-02])

Io_Luna_Jupiter = Planet("Io (JI)", 8.94E+22,
                        [5.070754211480966E+08, 5.459198781194668E+08, -1.360316329383263E+07],
                        [-2.469595330228651E+01, 8.077287633431147E-01,-3.481497790305407E-01])




#Añadir los planetas a la lista de planetas
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
Planets.append(Titan_Luna_Jupiter)
Planets.append(Luna_Tierra)
Planets.append(Io_Luna_Jupiter)
Planets.append(Calisto_Luna_Jupiter)
Planets.append(Ganímedes_Luna_Jupiter)

h = 1200
Nsteps = 3*24*365

def RK(planet):
  planetPosFinal = 0
  for time in range(0,Nsteps):
    k1 = accelerationCalc(planet.mass, planet.position)
    k2 = accelerationCalc(planet.mass, planet.position+planet.speed*h/2+(k1*(h**2)/8))
    k3 = accelerationCalc(planet.mass, planet.position+planet.speed*h/2+(k2*(h**2)/8))
    k4 = accelerationCalc(planet.mass, planet.position+planet.speed*h+(k3*(h**2/2)))
    planet.speed = planet.speed + h*(k1+2*k2+3*k3+k4)/6  # Actualiza la velocidad
    planet.position = planet.position + planet.speed*h + h**2*(k1+k2+k3)/6  # Actualiza la posición
    time = time*h  # Almacena el tiempo actual
  planetPosFinal = planet.position 
  return planetPosFinal/1000

print("Aproximación de la posicion de los planetas en 1 año")

for i in range(len(Planets)):
   print(f"{str(Planets[i].nombre)}: {RK(Planets[i])}")

