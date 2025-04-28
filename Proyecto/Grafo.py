# Proyecto1/Grafo.py
from Proyecto import Arista as ari
from Proyecto import Nodo as nod
import random  
import math
# import pygame
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

    def agregar_arista(self, origen, destino):
        """
        Agrega una arista entre dos nodos.
        
        Args:
            origen: Valor del nodo origen
            destino: Valor del nodo destino
        
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

    def archivo_grafo(self, valor):
        """
        Crea archivo del garfo.
        
        Args:
            valor: Valor nombre del grafo
            
        Returns:
            Archivo extencion valor.dot 
        """
        f = open(str(valor+".dot"), "w")
        f.write(str('graph '+valor+'={\n'))
        f.write(";\n".join(str(nodo.obtener_valor()) for nodo in self.obtener_nodos()))
        f.write(";\n")
        f.write(";\n".join(str(arista) for arista in self.obtener_aristas()))
        f.write(";\n}")
        f.close()

    def generar_malla(self,filas,columnas):
        """
        Genera un grafo malla con las dimensiones especificadas.
        Args:
            filas: numero de filas del grafo
            columnas: numero de columnas del grafo
        
        Returns:
            Grafo malla
        """
        
        
        # Conectar nodos horizontalmente
        for i in range(filas):
            for j in range(columnas - 1):
                origen = f"{i}_{j}"
                destino = f"{i}_{j+1}"
                self.agregar_arista(origen, destino)
        
        # Conectar nodos verticalmente
        for i in range(filas - 1):
            for j in range(columnas):
                origen = f"{i}_{j}"
                destino = f"{i+1}_{j}"
                self.agregar_arista(origen, destino)

    def grafoErdosReny(self,nodos,aristas):
        """
        Genera un grafo Erdös y Rényi con los nodos especificadas.
        Crea n nodos y elegir uniformemente al azar m distintos pares de distintos aristas
        Args:
            nodos: numero de nodos del grafo
            aristas: numero de aristas del grafo
        
        Returns:
            Grafo de Erdös y Rényi
        """
        # Crear nodos
        for i in range(nodos):
            self.agregar_nodo(i)
        
        i=0
        while(i<aristas):
            origen,destino=random.randint(0,nodos-1),random.randint(0,nodos-1)
            if self.existe_arista(origen,destino)==self.dirigido and origen != destino:
                self.agregar_arista(origen,destino)
                i+=1

    def grafoGilbert(self,nodos,pro):
        """
            Genera el grafo Gilbert con nodos especificos y probabilidad de conectarse a otro nodo 
            Crea n nodos y poner una arista entre cada par independiente y uniformemente con probabilidad pro
            Args:
                nodos: numero de nodos 
                pro: la probabilidad de conectarse
            Returns:
                Grafo Gilbert 
        """
        for i in range(nodos):
            self.agregar_nodo(i)
        
        for i in range(nodos):
            origen = f"{i}"
            for j in range(nodos):
                destino = f"{j}"
                if random.random() < pro and origen != destino and self.existe_arista(origen,destino)==self.dirigido :
                    self.agregar_arista(origen,destino)

    def grafoSimple(self,nodos,r):
        """
        Genera el Grafo geográfico simple con nodos espesificos y r
        Colocar n nodos en un rectángulo unitario con coordenadas uniformes (o normales) y colocar una arista 
        entre cada que distancia =< r 
        Args:
            nodos: n cantindad de nodos 
            r : la distacia maxima entre los nodos
        Returns:
                Grafo geográfico simple
        """
        for i in range(0,nodos):
            cor_x,cor_y=random.randint(0,nodos),random.randint(0,nodos)
            self.agregar_nodo(f"{cor_x}|{cor_y}")
        
        for origen in self.obtener_nodos():
            cord=(origen.obtener_valor().split("|"))
            corx1,cory1=int(cord[0]),int(cord[1])
            for destino in self.obtener_nodos():
                cord2=(destino.obtener_valor().split("|"))
                corx2,cory2=int(cord2[0]),int(cord2[1])
                if math.dist([corx1, cory1], [corx2, cory2]) <= r and self.existe_arista(origen,destino)==self.dirigido and cord!=cord2:
                    self.agregar_arista(origen.obtener_valor(),destino.obtener_valor())

    def GrafoDorogovtsevMendes(self,nodos):
        """
        Genera el Grafo Dorogovtsev-Mendes con nodos adidcionales
        Crear 3 nodos y 3 aristas formando un triángulo. 
        Después, para cada nodo adicional, se selecciona una arista al azar y se 
        crean aristas entre el nodo nuevo y los extremos de la arista seleccionada
        Args:
            nodos: Cantidad de nodos a generar
        Returns:
            Grafo de Dorogovtsev-Mendes
        """
        A,B,C = "0|0", "10|0", "5|10"
        self.agregar_arista(A,B)
        self.agregar_arista(B,C)
        self.agregar_arista(C,A)
        CorNodos=[]
        i=1
        while i<= nodos:
            AristaAle=random.choice(self.obtener_aristas())
            for nodo in AristaAle.obtener_nodos():
                CorNodos.append(nodo.obtener_valor())
            newNod=str(random.randint(-20,20))+'|'+str(random.randint(-20,20))
            if self.existe_arista(newNod,CorNodos[0])==self.dirigido:
                self.agregar_arista(newNod,CorNodos[0])
            if self.existe_arista(newNod,CorNodos[1])==self.dirigido:
                self.agregar_arista(newNod,CorNodos[1])
            CorNodos.pop()
            CorNodos.pop()
            i+=1

    def grafoBarabasiAlbert(self,nodos,costomax):
        """
        Genera el grafo de Barabási-Albert
        Colocar n nodos uno por uno, asignando a cada uno d aristas a vértices distintos de tal manera que la probabilidad 
        de que el vértice nuevo se conecte a un vértice existente costomax es proporcional a la cantidad de aristas
        Args:
            nodos : Cantidad de nodos del grafo
            costomax: numero maximo de aristas por nodo 
        Returns:
            Grafo de Barabási-Albert
        """
        
        for valnodo in range(1,nodos+1):
            self.agregar_nodo(valnodo)
            for exisN in self.obtener_nodos():
                if self.grado_nodo(exisN.obtener_valor())<costomax and exisN.obtener_valor()!=valnodo:
                    Pv=1-((self.grado_nodo(exisN.obtener_valor()))/costomax)
                    if random.random() < Pv:
                        self.agregar_arista(exisN.obtener_valor(),valnodo)
