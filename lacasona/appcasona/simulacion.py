""" 

INTEGRANTES-------------------------------
Rafael Leon
Pablo Lopez
Laboratorio 5 
Este ejercicio hace una simulacion con el modulo simpy
"""


import simpy
import random


# clase de simulacion
class Simulacion(object):

    # constructor de la clase 
    def __init__(self,env, simTime, name, ram, memory, ins, velocidad):
        self.env = env # ambiente de simulacion simpy
        self.simTime = simTime # tiempo de simulacion
        self.name = name # nombre del proceso PID (process ID)
        self.ram = ram # memoria ram disponible
        self.memory = memory # cantidad de memoria
        self.ins = ins # instucciones de un proceso
        self.velocidad = velocidad

        # iniciar la simulacion
        self.action = env.process(self.proceso(env, simTime, name, ram, memory, ins, velocidad))

    # simulacion 
    def proceso(self,env, simTime, name, ram, memory, ins, velocidad):
        global tiempoTotal
        global tiempoDes

        yield env.timeout(simTime)
        print"%s necesita %d de memoria RAM - tiempo actual: %f"%(name, memory, env.now)

        tiempoLlegada = env.now 
        yield RAM.get(memory)

        print "%s ha obtenido %d de memoria - tiempo actual: %f"%(name, memory, env.now)
        insC = 0 # instrucciones disponibles por CPU
        

        # luego de obtener la memoria RAM necesaria, se hace cola para pedir realizar instrucciones al CPU
        while insC < ins:
            with CPU.request() as reqCPU:
                yield reqCPU

                if (ins-insC)>=velocidad:
                    rend = velocidad # efectividad de procesamiento

                else:
                    rend=(ins-insC)

                print"%s el CPU ejecutara %d instrucciones - tiempo actual: %f"%(name, rend, env.now)
                yield env.timeout(rend/velocidad)   

                insC += rend

                print"%s CPU ejecutando (%d/%d) completado - tiempo actual: %f"%(name, insC, ins, env.now)

            waiting = random.randint(1,2)

            if ((waiting == 1) and (insC<ins)):

                with WAIT.request() as requestIO:
                    yield requestIO
                    yield env.timeout(1)                
                    print "%s esperando para realizar operaciones (I/O) - tiempo actual: %f"%(name, env.now)

        yield RAM.put(memory)
        print "%s completado: retornando %d de memoria RAM - tiempo actual: %f"%(name, memory, env.now)
        tiempoTotal += (env.now - tiempoLlegada)
        tiempoDes.append(env.now - tiempoLlegada) 


"""VARIABLES QUE SE ESTAN UTILIZANDO """
velocidad = 3.0 # instrucciones que realiza el CPU por unidad de tiempo
memoriaTotal = 100 # Memoria de RAM disponible
procesos = 25 # cantidad de procesos a realizar
tiempoTotal = 0 # tiempo total en la simulacion
tiempoDes = [] # desviacion estandar del tiempo


# ambiente de simulacion, CPU y WAIT como resources y RAM como contenedor
environment = simpy.Environment() 
CPU = simpy.Resource (environment, capacity=2) 
RAM = simpy.Container(environment, init=memoriaTotal, capacity=memoriaTotal)
WAIT = simpy.Resource (environment, capacity=2)  
 
semilla = 42 # semilla para crear numeros aleatorios
intervalo = 1 # intervalo en que se crean los procesos 
random.seed(semilla)


# creacion de los procesos
for i in range(procesos):
    simTime = random.expovariate(1.0 / intervalo)
    instrucciones = random.randint(1,10)
    memory = random.randint(1,10)
    c = Simulacion(environment, simTime, 'PID %d' % i, RAM, memory, instrucciones, velocidad)
environment.run()

print"------SIMULACION TERMINADA, DATOS OBTENIDOS-----------"

promedio = (tiempoTotal/procesos)
print"La media del tiempo es: %f" % (promedio)

suma = 0

for j in tiempoDes:
    suma +=(j-promedio)**2

desviacion = (suma/(procesos-1))**0.5
print"La desviacion estandar es: %f"%(desviacion)