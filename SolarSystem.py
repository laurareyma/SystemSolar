import math
import numpy as np

class Planet:

  def __init__(self, mass, position, speed, acceleration):
    self.mass = mass*1000
    self.position = position*1000
    self.speed = speed*1000 #Se multiplica por mil para obtener el valor en metros y m/s respectivamente.
    self.acceleration = None

def force(m1, m2, r1, r2):

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

def accelerationCalc(planet1:Planet):
    #Función que calcula la aceleración de un planeta, sumando las fuerzas ejercidas por los demás planetas
    temp = 0 #Variable temporal para almacenar la suma de las fuerzas
    planetIndex = 0 #Variable para almacenar el índice del planeta en la lista de planetas
    for planet in Planets: 
      if planet == planet1: #Si el planeta es el mismo que el que se está calculando, se pasa al siguiente planeta
         planetIndex = Planets.index(planet)
         pass
      else:
        temp = temp + planet1.mass*(force(planet.mass, planet.position , planet1.mass, planet1.position))
    accl = 1/temp
    Planets[planetIndex].acceleration = accl
    return accl

def AproRK(self, time, mass, ):
   pass

Planets = []

Sol = Planet(1.989E+30, 
              [-1.179443251112733E+06, -4.525307891739777E+05, 3.134211075848844E+04], 
              [8.641673046632211E-03, -1.197549843610353E-02, -8.333309545496825E-05],
              None)

Mercurio = Planet(3.285E+23, 
                  [-5.604542055485767E+07, -3.485180684223912E+07, 2.252726524219494E+06], 
                  [1.587699012959109E+01, 3.914167832796291E+01, -4.653314021586240E+00],
                  None)

Venus = Planet(4.867E+24, 
                [-9.124062992562428E+07, -6.007396006977719E+07, 4.409138578373339E+0], 
                [1.909604199335837E+01, -2.937858610658142E+01, -1.504747093789415E+00],
                None)

Tierra = Planet(5.972E+24, 
                 [-6.807583303581282E+07, 1.306386634514613E+08, 2.441434724599123E+04], 
                 [-2.700500662780606E+01, -1.367492208542078E+01, -2.819099962243499E-04],
                 None)

Marte = Planet(6.39E+23, 
                 [-8.418911224084277E+06, -2.186228318767418E+08, -4.363309315665454E+06], 
                 [2.513774699083788E+01, 1.264412795570113E+00, -5.897251116445148E-01],
                 None)

Jupiter = Planet(1.898E+27, 
                 [5.072890561816115E+08, 5.455564093701284E+08, -1.361280331447470E+07],
                 [9.712016793883137E+00, 9.516945889247435E+00, 1.778637018081355E-01],
                 None)

Saturno = Planet(5.683E+26, 
                 [1.349171392640714E+09, -5.432565025518103E+08, -4.427101531561103E+07], 
                 [3.069954912732006E+00, 8.940857757866405E+00, -2.774778319351245E-01],
                 None)

Urano = Planet(8.681E+25, 
                [1.826634011533559E+09, 2.294233899646317E+09, -1.514356969771659E+07],
                [-5.377708713288905E+00, 3.924460766621745E+00, 8.429516133480419E-02],
                None)

Neptuno = Planet(1.024E+26, 
                  [4.463673410614180E+09, -2.603336928890301E+08, -9.750858120032202E+07],
                  [2.803376699079932E-01, 5.458300376201279E+00, -1.186959253968582E-01],
                  None)

#Añadir los planetas a la lista de planetas
Planets.append(Sol)
Planets.append(Mercurio)
Planets.append(Venus)
Planets.append(Tierra)
Planets.append(Marte)
Planets.append(Jupiter)
Planets.append(Saturno)
Planets.append(Urano)
Planets.append(Neptuno)
 
#Acceleration calculus for each planet using accelrationCalc() function
for planet in Planets:
   accelerationCalc(planet)

