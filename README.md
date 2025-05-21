# Algoritmos

Este proyecto contiene la implementación de diversos algoritmos relacionados con grafos. Incluye la generación de grafos, algoritmos de búsqueda y caminos más cortos, entre otros.

## Contenido del Proyecto

### Funcionalidades principales:
1. **Generación de grafos**:
   - Grafo Malla
   - Grafo de Erdös-Rényi
   - Grafo de Gilbert
   - Grafo Geográfico Simple
   - Grafo de Dorogovtsev-Mendes
   - Grafo de Barabási-Albert

2. **Algoritmos de búsqueda**:
   - Búsqueda en Anchura (BFS)
   - Búsqueda en Profundidad Recursiva (DFS Recursivo)
   - Búsqueda en Profundidad Iterativa (DFS Iterativo)

3. **Algoritmos de caminos más cortos**:
   - Algoritmo de Dijkstra

### Archivos principales:
- `Grafo.py`: Contiene la clase `Grafo` y la implementación de los algoritmos.
- `CreacionGrafo.py`: Script para generar grafos y ejecutar algoritmos sobre ellos.
- `README.md`: Documentación del proyecto.

## Requisitos

- Python 3.8 o superior
- Librerías estándar:
  - `random`
  - `math`
  - `time`
  - `collections` (para `deque`)

## Uso

1. **Generar un grafo**:
   Puedes generar un grafo utilizando cualquiera de los métodos de la clase `Grafo`. Por ejemplo:
   ```python
   grafo = Grafo()
   grafo.GrafoBarabasiAlbert(30, 3)
   grafo.ArchivoGrafo('grafoOriginal')