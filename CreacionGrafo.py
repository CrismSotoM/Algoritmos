import time
import Proyecto.Grafo as gr
import Proyecto.Visualicacion as vis

print('Creacion de grafos', time.strftime("%H:%M:%S"))
grafo =gr.Grafo()
grafo.GrafoErdosReny(100,200)
vis.spring(grafo)

print('termino de crear grafos ', time.strftime("%H:%M:%S"))