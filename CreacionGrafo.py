import time
import Proyecto.Grafo as gr
import random

print('Creacion de grafos', time.strftime("%H:%M:%S"))

grafo=gr.Grafo()
grafo.GrafoMalla(5,5)
grafo.ArchivoGrafo('grafoMalla25')

nodo=random.choice(grafo.ObtenerNodos())
Kruskal=grafo.Kruskal()
Kruskal.ArchivoGrafo('Kruskal25Malla')

KruskalInver=grafo.KruskalInverso()
KruskalInver.ArchivoGrafo('KruskalInverMalla')

arbolprim=grafo.Prim()
arbolprim.ArchivoGrafo('ArbolPrimMalla')


print('termino de crear grafos ', time.strftime("%H:%M:%S"))