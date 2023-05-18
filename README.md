# productoresconsumidores

El enlace al repositorio de GitHub de este proyecto es el siguiente: [GitHub](https://github.com/jzazooro/productoresconsumidores.git)

Hemos resuelto el problema de productores y consumidores con semaforos y sin semaforos

### main

```
from lanzador import main

if __name__ == '__main__':
    main()
```

### lanzador

```
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
```

### funcione(no semaforos)

```
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
```

### funciones (semaforos)

```
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
```
