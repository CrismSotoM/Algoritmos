class Nodo:
    def __init__(self, valor):
        """
        Inicializa un nodo con un valor específico.
        
        Args:
            valor: El valor que almacenará el nodo (puede ser cualquier tipo de dato).
        """
        self.valor = valor
        self.vecinos = {}  # Diccionario para almacenar nodos adyacentes y pesos (para grafos ponderados)
    
    def agregar_vecino(self, nodo, peso=1):
        """
        Agrega un nodo vecino con un peso opcional.
        
        Args:
            nodo: El nodo vecino a agregar.
            peso: El peso de la arista (por defecto 1 para grafos no ponderados).
        """
        self.vecinos[nodo] = peso
    
    def obtener_vecinos(self):
        """
        Devuelve los nodos vecinos.
        
        Returns:
            Un diccionario con los nodos vecinos y sus pesos.
        """
        return self.vecinos
    
    def obtener_valor(self):
        """
        Devuelve el valor almacenado en el nodo.
        
        Returns:
            El valor del nodo.
        """
        return self.valor
    
    def __str__(self):
        """
        Representación en string del nodo.
        
        Returns:
            String que muestra el valor del nodo y sus vecinos.
        """
        vecinos_str = ", ".join([f"{n.obtener_valor()}({peso})" for n, peso in self.vecinos.items()])
        return f"Nodo({self.valor}) -> [{vecinos_str}]"