import Grafo as gr

# Crear grafo no dirigido y no ponderado
grafo1 = gr.Grafo(dirigido=False)
grafo1.agregar_nodo('A')
grafo1.agregar_nodo('B')
grafo1.agregar_nodo('C')

grafo1.agregar_arista('A', 'B')
grafo1.agregar_arista('B', 'C')
grafo1.agregar_arista('C', 'A')

print(grafo1)
print("Grado de A:", grafo1.grado_nodo('A'))

