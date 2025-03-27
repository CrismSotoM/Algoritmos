class Arista:
    def __init__(self, origen, destino, dirigida=False):
        """
        Inicializa una arista entre dos nodos.
        
        Args:
            origen: Nodo de origen
            destino: Nodo de destino
            peso: Peso de la arista (por defecto 1 para grafos no ponderados)
            dirigida: Booleano que indica si la arista es dirigida (por defecto False)
        """
        self.origen = origen
        self.destino = destino
        self.dirigida = dirigida
    
    def obtener_nodos(self):
        """
        Devuelve los nodos conectados por la arista.
        
        Returns:
            Tupla con los nodos (origen, destino)
        """
        return (self.origen, self.destino)
    
    def es_dirigida(self):
        """
        Indica si la arista es dirigida.
        
        Returns:
            True si es dirigida, False si no lo es
        """
        return self.dirigida
    
    def __str__(self):
        """
        Representación en string de la arista.
        
        Returns:
            String descriptivo de la arista
        """
        direccion = "->" if self.dirigida else "<->"
        return f"{self.origen.obtener_valor()} {direccion} {self.destino.obtener_valor()}"
    
    def __eq__(self, otra):
        """
        Compara si dos aristas son iguales. 
        Args:
            otra: Otra arista a comparar
        Returns:
            True si conectan los mismos nodos (en el mismo orden si es dirigida)
        """
        if self.dirigida:
            return (self.origen == otra.origen and 
                    self.destino == otra.destino)
        else:
            return ((self.origen == otra.origen and 
                    self.destino == otra.destino) or
                    (self.origen == otra.destino and 
                    self.destino == otra.origen))