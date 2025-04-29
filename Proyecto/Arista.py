class Arista:
    def __init__(self, origen, destino, dirigida=False):
        """
        Inicializa una arista entre dos nodos.
        
        Args:
            origen: Nodo de origen
            destino: Nodo de destino
            dirigida: Booleano que indica si la arista es dirigida (por defecto False)
        """
        self.origen = origen
        self.destino = destino
        self.dirigida = dirigida
    
    def ObtenerNodos(self):
        """
        Devuelve los nodos conectados por la arista.
        
        Returns:
            Tupla con los nodos (origen, destino)
        """
        return (self.origen, self.destino)
    
    def EsDirigida(self):
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
        direccion = "->" if self.dirigida else "--"
        return f"{self.origen.ObtenerValor()} {direccion} {self.destino.ObtenerValor()}"
    
    