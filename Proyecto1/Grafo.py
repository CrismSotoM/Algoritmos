import Arista as ari
import Nodo as nod
class Grafo:
    def __init__(self, dirigido=False):
        """   Inicializa un grafo vacío.
        Args:
        dirigido: Booleano que indica si el grafo es dirigido (por defecto False)"""
        self.nodos = {}  # Diccionario de nodos {valor: nodo}
        self.aristas = []  # Lista de aristas
        self.dirigido = dirigido
        
    def agregar_nodo(self, valor):
        """
        Agrega un nuevo nodo al grafo.
        
        Args:
            valor: Valor del nodo a agregar
            
        Returns:
            El nodo creado o existente
        """
        if valor not in self.nodos:
            self.nodos[valor] = nod.Nodo(valor)
        return self.nodos[valor]
    
    def agregar_arista(self, origen, destino, peso=1):
        """
        Agrega una arista entre dos nodos.
        
        Args:
            origen: Valor del nodo origen
            destino: Valor del nodo destino
            peso: Peso de la arista (solo para grafos ponderados)
            
        Returns:
            La arista creada
        """
        nodo_origen = self.agregar_nodo(origen)
        nodo_destino = self.agregar_nodo(destino)
        
        arista = ari.Arista(nodo_origen, nodo_destino, self.dirigido)
        self.aristas.append(arista)
        
        nodo_origen.agregar_vecino(nodo_destino)
        if not self.dirigido:
            nodo_destino.agregar_vecino(nodo_origen)
        
        return arista
    
    def obtener_nodo(self, valor):
        """
        Obtiene un nodo por su valor.
        
        Args:
            valor: Valor del nodo a buscar
            
        Returns:
            El nodo si existe, None si no existe
        """
        return self.nodos.get(valor)
    
    def obtener_aristas(self):
        """
        Devuelve todas las aristas del grafo.
        
        Returns:
            Lista de aristas
        """
        return self.aristas
    
    def obtener_nodos(self):
        """
        Devuelve todos los nodos del grafo.
        
        Returns:
            Lista de nodos
        """
        return list(self.nodos.values())
    
    def existe_arista(self, origen, destino):
        """
        Verifica si existe una arista entre dos nodos.
        
        Args:
            origen: Valor del nodo origen
            destino: Valor del nodo destino
            
        Returns:
            True si existe la arista, False si no
        """
        nodo_origen = self.obtener_nodo(origen)
        nodo_destino = self.obtener_nodo(destino)
        
        if not nodo_origen or not nodo_destino:
            return False
            
        if self.dirigido:
            return nodo_destino in nodo_origen.obtener_vecinos()
        else:
            return (nodo_destino in nodo_origen.obtener_vecinos() or 
                    nodo_origen in nodo_destino.obtener_vecinos())
    
    def __str__(self):
        """
        Representación en string del grafo.
        
        Returns:
            String descriptivo del grafo
        """
        tipo = "Dirigido" if self.dirigido else "No dirigido"
        nodos = ", ".join(str(nodo.obtener_valor()) for nodo in self.obtener_nodos())
        aristas = "\n".join(str(arista) for arista in self.obtener_aristas())
        
        return f"Grafo ({tipo})\nNodos: [{nodos}]\nAristas:\n{aristas}"
    
    def grado_nodo(self, valor):
        """
        Calcula el grado de un nodo (número de aristas incidentes).
        
        Args:
            valor: Valor del nodo a calcular
            
        Returns:
            El grado del nodo
        """
        nodo = self.obtener_nodo(valor)
        if not nodo:
            return 0
        
        if self.dirigido:
            # Para grafos dirigidos, calculamos grado de entrada y salida
            grado_salida = len(nodo.obtener_vecinos())
            grado_entrada = sum(1 for n in self.obtener_nodos() if nodo in n.obtener_vecinos())
            return ('Entrada='+str(grado_entrada),'Salida='+str( grado_salida))
        else:
            return len(nodo.obtener_vecinos())