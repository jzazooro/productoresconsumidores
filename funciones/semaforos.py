from queue import Queue
import time 
from threading import Thread
from threading import Semaphore

cola=Queue()
semaforo=Semaphore(0)

def productor():
    i=1
    while True:
        print("Producido: ",i)
        cola.put(i)
        i+=1
        time.sleep(1)
        semaforo.release()

def consumidor():
    while True:
        semaforo.acquire()
        print("Consumido: ",cola.get())
        cola.task_done
        time.sleep(1)