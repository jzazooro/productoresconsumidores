from funciones.nosemaforos import *
from funciones.semaforos import *
from threading import Thread
import time

def main():

    apartado=int(input("Introduzca 1 si lo quiere con semaforos, o introduzca 2 si lo quiere sin semaforos: "))

    if apartado ==1:
        print("A continuacion se ejecutara el programa con semaforos")
        print("----------------------------------------------------")
        time.sleep(1)
        h1=Thread(target=productor)
        h2=Thread(target=consumidor)
        h1.start()
        h2.start()

    if apartado ==2:
        print("A continuacion se ejecutara el programa sin semaforos")
        print("----------------------------------------------------")
        time.sleep(1)
        h1=Thread(target=productorsinsemaforo)
        h2=Thread(target=consumidorsinsemaforo)
        h1.start()
        h2.start()