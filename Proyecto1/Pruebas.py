import Grafo as gr

# Crear grafo
grafo1 = gr.Grafo(dirigido=True)
grafo1.generar_malla(filas=20,columnas=20)
grafo1.archivo_grafo('GrafoMalla')
print(grafo1)
