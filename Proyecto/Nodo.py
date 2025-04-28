class Nodo:
    def __init__(self, valor):
        """
        Inicializa un nodo con un valor específico.
        
        Args:
            valor: El valor que almacenará el nodo (puede ser cualquier tipo de dato).
        """
        self.valor = valor
        self.vecinos = {}  # Diccionario para almacenar nodos adyacentes (para grafos ponderados)
    
    def agregar_vecino(self, nodo):
        peso=1
        """
        Agrega un nodo vecino.
        
        Args:
            nodo: El nodo vecino a agregar.
            peso: El peso de la arista (por cada conexion se agrega 1).
        """
        self.vecinos[nodo] = peso
    
    def obtener_vecinos(self):
        """
        Devuelve los nodos vecinos.
        
        Returns:
            Un diccionario con los nodos vecinos.
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
        vecinos_str = ", ".join([f"{n.obtener_valor()}" for n in self.vecinos.items()])
        return f"Nodo({self.valor}) -> [{vecinos_str}]"