from funciones.nosemaforos import *
from funciones.semaforos import *
from threading import Thread
import time

def main():
    print("A continuacion se ejecutara el programa con semaforos")
    print("----------------------------------------------------")
    time.sleep(1)
    h1=Thread(target=productor)
    h2=Thread(target=consumidor)
    h1.start()
    h2.start()

    print("A continuacion se ejecutara el programa sin semaforos")
    print("----------------------------------------------------")
    time.sleep(1)
    h3=Thread(target=productorsinsemaforo)
    h4=Thread(target=consumidorsinsemaforo)
    h3.start()
    h4.start()