import Proyecto.Grafo as gr
import Proyecto.Visualicacion as vis

grafo =gr.Grafo()
grafo.GrafoErdosReny(500,800)
vis.fruchterman_reginold(grafo,fuerza=0.3)
