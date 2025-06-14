import time
import Proyecto.Grafo as gr
import Proyecto.Visualicacion as vis

grafo =gr.Grafo()
grafo.GrafoErdosReny(500, 700)
vis.spring(grafo)
