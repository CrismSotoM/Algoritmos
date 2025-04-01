import Grafo as gr

# Crear grafo
grafo1 = gr.Grafo(dirigido=False)
grafo1.generar_malla(filas=50,columnas=20)
grafo1.archivo_grafo('GrafoMalla')

grafoErdosReny= gr.Grafo(dirigido=False)
grafoErdosReny.grafoErdosReny(nodos=500,aristas=1500)
grafoErdosReny.archivo_grafo('ErdosReny')
