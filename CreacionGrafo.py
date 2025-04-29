import Proyecto.Grafo as gr

grafoGusano=gr.Grafo()
grafoGusano.GrafoErdosReny(50,150)
grafoGusano.ArchivoGrafo('GrafoErdosReny0')

arbolBFSGusano = grafoGusano.BFS(inicio=1)
arbolBFSGusano.ArchivoGrafo('ArbolBFS')

arbolDfsInteGusano = grafoGusano.DfsIte(inicio=1)
arbolDfsInteGusano.ArchivoGrafo('arbolDfsInte')


arbolDfsRecGusano = grafoGusano.DfsR(inicio=1)
arbolDfsRecGusano.ArchivoGrafo('arbolDfsRec')