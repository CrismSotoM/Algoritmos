import time
import Proyecto.Grafo as gr
import Proyecto.Visualicacion as vis

grafo =gr.Grafo()
grafo.GrafoMalla(10, 10)
vis.fruchterman_reginold(grafo)
