import time
import Proyecto.Grafo as gr


print('Creacion de grafos Gilbert', time.strftime("%H:%M:%S"))
grafoGilbert30=gr.Grafo()
grafoGilbert30.GrafoGilbert(nodos=30,pro=0.3)
grafoGilbert30.ArchivoGrafo('GrafoGilbert30')

arbolBFSGilbert30 = grafoGilbert30.BFS(inicio=1)
arbolBFSGilbert30.ArchivoGrafo('ArbolBfsGilbert30')

arbolDfsInteGilbert30 = grafoGilbert30.DfsIte(inicio=1)
arbolDfsInteGilbert30.ArchivoGrafo('arbolDfsInteGilbert30')

arbolDfsRecGilbert30 = grafoGilbert30.DfsR(inicio=1)
arbolDfsRecGilbert30.ArchivoGrafo('arbolDfsRecGilbert30')


grafoGilbert100=gr.Grafo()
grafoGilbert100.GrafoGilbert(nodos=100,pro=0.3)
grafoGilbert100.ArchivoGrafo('GrafoGilbert100')

arbolBFSGilbert100 = grafoGilbert100.BFS(inicio=1)
arbolBFSGilbert100.ArchivoGrafo('ArbolBfsGilbert100')

arbolDfsInteGilbert100 = grafoGilbert100.DfsIte(inicio=1)
arbolDfsInteGilbert100.ArchivoGrafo('arbolDfsInteGilbert100')

arbolDfsRecGilbert100 = grafoGilbert100.DfsR(inicio=1)
arbolDfsRecGilbert100.ArchivoGrafo('arbolDfsRecGilbert100')

grafoGilbert500=gr.Grafo()
grafoGilbert500.GrafoGilbert(nodos=30,pro=0.3)
grafoGilbert500.ArchivoGrafo('GrafoGilbert500')

arbolBFSGilbert500 = grafoGilbert500.BFS(inicio=1)
arbolBFSGilbert500.ArchivoGrafo('ArbolBfsGilbert500')

arbolDfsInteGilbert500 = grafoGilbert500.DfsIte(inicio=1)
arbolDfsInteGilbert500.ArchivoGrafo('arbolDfsInteGilbert500')

arbolDfsRecGilbert500 = grafoGilbert500.DfsR(inicio=1)
arbolDfsRecGilbert500.ArchivoGrafo('arbolDfsRecGilbert500')

print('termino de crear grafos Gilbert', time.strftime("%H:%M:%S"))