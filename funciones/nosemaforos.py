from queue import Queue
import time

cola=Queue()

def productorsinsemaforo():
    i=1
    while True:
        cola.put(i)
        cola.join()
        print("Producido: ",i)
        i+=1
        time.sleep(1)

def consumidorsinsemaforo():
    while True:
        producto=cola.get()
        print("Consumido: ",cola.get())
        cola.task_done
        time.sleep(1)