import Grafo as gr

# Crear grafo
grafo1 = gr.Grafo(dirigido=True)
grafo1.agregar_nodo('A')
grafo1.agregar_nodo('B')
grafo1.agregar_nodo('C')

grafo1.agregar_arista('A', 'B')
grafo1.agregar_arista('A', 'C')
grafo1.agregar_arista('B', 'A')
grafo1.agregar_arista('B', 'C')
grafo1.agregar_arista('C', 'A')

print(grafo1)
print("Grado de A:", grafo1.grado_nodo('A'))
