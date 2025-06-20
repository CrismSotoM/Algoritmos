import Proyecto.Grafo as gr
import Proyecto.Visualicacion as vis

grafo =gr.Grafo()
grafo.GrafoMalla(23, 23)
vis.fruchterman_reginold(grafo,fuerza=1)
