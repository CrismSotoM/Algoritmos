import time
import Proyecto.Grafo as gr
import random

print('Creacion de grafos', time.strftime("%H:%M:%S"))

grafo=gr.Grafo()
grafo.GrafoBarabasiAlbert(30,3)
grafo.ArchivoGrafo('grafoOriginal')

nodo=random.choice(grafo.ObtenerNodos())

kstra=grafo.Dijkstra(inicio=nodo.valor)
kstra.ArchivoGrafo('dijkstra')

print('termino de crear grafos ', time.strftime("%H:%M:%S"))