from Proyecto import Arista as ari
from Proyecto import Nodo as nod
from collections import deque
import random  
import math
import pygame
class Grafo:
    def __init__(self, dirigido=False):
        """   Inicializa un grafo vacío.
        Args:
        dirigido: Booleano que indica si el grafo es dirigido (por defecto False)"""
        self.nodos = {}  # Diccionario de nodos {valor: nodo}
        self.aristas = []  # Lista de aristas
        self.dirigido = dirigido  # Indica si el grafo es dirigido o no

    def AgregarNodo(self, valor):
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

    def AgregarArista(self, origen, destino):
        """
        Agrega una arista entre dos nodos.
        
        Args:
            origen: Valor del nodo origen
            destino: Valor del nodo destino
        
        Returns:
            La arista creada
        """
        nodo_origen = self.AgregarNodo(origen)
        nodo_destino = self.AgregarNodo(destino)
        
        arista = ari.Arista(nodo_origen, nodo_destino, self.dirigido)
        self.aristas.append(arista)
        
        nodo_origen.AgregarVecino(nodo_destino)
        if not self.dirigido:
            nodo_destino.AgregarVecino(nodo_origen)
        
        return arista

    def ObtenerArista(self, origen, destino):
        """
        Obtiene una arista entre dos nodos.
        
        Args:
            origen: Valor del nodo origen
            destino: Valor del nodo destino
            
        Returns:
            La arista si existe, None si no existe
        """
        nodo_origen = self.ObtenerNodo(origen)
        nodo_destino = self.ObtenerNodo(destino)
        
        if not nodo_origen or not nodo_destino:
            return None
        
        for arista in self.aristas:
            if arista.ObtenerNodos()[0] == nodo_origen and arista.ObtenerNodos()[1] == nodo_destino:
                return arista
        return None

    def EliminarArista(self, origen, destino):
        """
        Elimina una arista entre dos nodos.
        
        Args:
            origen: Valor del nodo origen
            destino: Valor del nodo destino
            
        Returns:
            True si se eliminó la arista, False si no existía
        """
        nodo_origen = self.ObtenerNodo(origen)
        nodo_destino = self.ObtenerNodo(destino)
        
        if not nodo_origen or not nodo_destino:
            return False
        
        arista = self.ObtenerArista(origen, destino)
        
        if arista in self.aristas:
            self.aristas.remove(arista)
            nodo_origen.EliminarVecino(nodo_destino)
            if not self.dirigido:
                nodo_destino.EliminarVecino(nodo_origen)
            return True
        return False

    def ObtenerNodo(self, valor):
        """
        Obtiene un nodo por su valor.
        
        Args:
            valor: Valor del nodo a buscar
            
        Returns:
            El nodo si existe, None si no existe
        """
        return self.nodos.get(valor)

    def ObtenerAristas(self):
        """
        Devuelve todas las aristas del grafo.
        
        Returns:
            Lista de aristas
        """
        return self.aristas

    def ObtenerNodos(self):
        """
        Devuelve todos los nodos del grafo.
        
        Returns:
            Lista de nodos
        """
        return list(self.nodos.values())

    def ExisteArista(self, origen, destino):
        """
        Verifica si existe una arista entre dos nodos.
        
        Args:
            origen: Valor del nodo origen
            destino: Valor del nodo destino
            
        Returns:
            True si existe la arista, False si no
        """
        nodo_origen = self.ObtenerNodo(origen)
        nodo_destino = self.ObtenerNodo(destino)
        
        if not nodo_origen or not nodo_destino:
            return False
            
        if self.dirigido:
            return nodo_destino in nodo_origen.ObtenerVecinos()
        else:
            return (nodo_destino in nodo_origen.ObtenerVecinos() or 
                    nodo_origen in nodo_destino.ObtenerVecinos())

    def __str__(self):
        """
        Representación en string del grafo.
        
        Returns:
            String descriptivo del grafo
        """
        tipo = "Dirigido" if self.dirigido else "No dirigido"
        nodos = ", ".join(str(nodo.ObtenerValor()) for nodo in self.ObtenerNodos())
        aristas = "\n".join(str(arista) for arista in self.ObtenerAristas())
        
        return f"Grafo ({tipo})\nNodos: [{nodos}]\nAristas:\n{aristas}"

    def GradoNodo(self, valor):
        """
        Calcula el grado de un nodo (número de aristas incidentes).
        
        Args:
            valor: Valor del nodo a calcular
            
        Returns:
            El grado del nodo
        """
        nodo = self.ObtenerNodo(valor)
        if not nodo:
            return 0
        
        if self.dirigido:
            # Para grafos dirigidos, calculamos grado de entrada y salida
            grado_salida = len(nodo.ObtenerVecinos())
            grado_entrada = sum(1 for n in self.ObtenerNodos() if nodo in n.ObtenerVecinos())
            return ('Entrada='+str(grado_entrada),'Salida='+str( grado_salida))
        else:
            return len(nodo.ObtenerVecinos())

    def ArchivoGrafo(self, valor, distancias=None):
        """
        Crea archivo del garfo.
        
        Args:
            valor: Valor nombre del grafo
            
        Returns:
            Archivo extencion valor.dot 
        """
        f = open(str('C:/Users/crist/OneDrive/Documentos/practicapythn/Algoritmos/ArchivosGphi/DOT/'+valor+".dot"), "w")
        f.write(str('graph '+valor+'={\n'))
        if distancias is not None:
            for nodo in self.ObtenerNodos():
                # "1" [label="Raiz 1"];
                f.write(f"\"{nodo.ObtenerValor()}\" "+str(distancias[nodo.ObtenerValor()])+"\n")
        else:
            f.write(";\n".join(str(nodo.ObtenerValor()) for nodo in self.ObtenerNodos()))
            f.write(";\n")
        f.write(";\n".join(str(arista) for arista in self.ObtenerAristas()))
        f.write(";\n}")
        f.close()

    def Copia(self):
        """
        Crea una copia del grafo actual.
        
        Returns:
            Un nuevo objeto Grafo con los mismos nodos y aristas
        """
        nuevo_grafo = Grafo(self.dirigido)
        for nodo in self.ObtenerNodos():
            nuevo_grafo.AgregarNodo(nodo.ObtenerValor())
        for arista in self.ObtenerAristas():
            nuevo_grafo.AgregarArista(arista.ObtenerNodos()[0].ObtenerValor(),arista.ObtenerNodos()[1].ObtenerValor())
        return nuevo_grafo     

    def GrafoMalla(self,filas,columnas):
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
                origen = f"{i}|{j}"
                destino = f"{i}|{j+1}"
                self.AgregarArista(origen, destino)
        
        # Conectar nodos verticalmente
        for i in range(filas - 1):
            for j in range(columnas):
                origen = f"{i}|{j}"
                destino = f"{i+1}|{j}"
                self.AgregarArista(origen, destino)

    def GrafoErdosReny(self,nodos,aristas):
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
            self.AgregarNodo(i)
        
        i=0
        while(i<aristas):
            origen,destino=random.randint(0,nodos-1),random.randint(0,nodos-1)
            if self.ExisteArista(origen,destino)==self.dirigido and origen != destino:
                self.AgregarArista(origen,destino)
                i+=1

    def GrafoGilbert(self,nodos,pro):
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
            self.AgregarNodo(f"{i}")
        
        for i in range(nodos):
            origen = f"{i}"
            for j in range(nodos):
                destino = f"{j}"
                if random.random() < pro and origen != destino and self.ExisteArista(origen,destino)==self.dirigido :
                    self.AgregarArista(origen,destino)

    def GrafoSimple(self,nodos,r):
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
            self.AgregarNodo(f"{cor_x}|{cor_y}")
        
        for origen in self.ObtenerNodos():
            cord=(origen.ObtenerValor().split("|"))
            corx1,cory1=int(cord[0]),int(cord[1])
            for destino in self.ObtenerNodos():
                cord2=(destino.ObtenerValor().split("|"))
                corx2,cory2=int(cord2[0]),int(cord2[1])
                if math.dist([corx1, cory1], [corx2, cory2]) <= r and self.ExisteArista(origen,destino)==self.dirigido and cord!=cord2:
                    self.AgregarArista(origen.ObtenerValor(),destino.ObtenerValor())

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
        self.AgregarArista(A,B)
        self.AgregarArista(B,C)
        self.AgregarArista(C,A)
        CorNodos=[]
        i=3
        while i< nodos:
            AristaAle=random.choice(self.ObtenerAristas())
            for nodo in AristaAle.ObtenerNodos():
                CorNodos.append(nodo.ObtenerValor())
            newNod=str(random.randint(-20,20))+'|'+str(random.randint(-20,20))
            self.AgregarArista(newNod,CorNodos[0])
            self.AgregarArista(newNod,CorNodos[1])
            CorNodos.pop()
            CorNodos.pop()
            i+=1

    def GrafoBarabasiAlbert(self,nodos,costomax):
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
            self.AgregarNodo(valnodo)
            for exisN in self.ObtenerNodos():
                if self.GradoNodo(exisN.ObtenerValor())<costomax and exisN.ObtenerValor()!=valnodo:
                    Pv=1-((self.GradoNodo(exisN.ObtenerValor()))/costomax)
                    if random.random() < Pv:
                        self.AgregarArista(exisN.ObtenerValor(),valnodo)

    def BFS(self, inicio):
        """
        Busqueda a lo ancho 
        Explorar desde Inicio y hacia fuera en todas las direcciones posibles, 
        añadiendo nodos una “capa” a la vez
        
        Args:
            nodo: Nodo inicial
        """ 
        arbolBFS= Grafo()
        
        nodo_inicio = self.ObtenerNodo(inicio)
        if not nodo_inicio:
            return arbolBFS
        
        # Estructuras para BFS
        visitados = set()
        cola = deque()
        
        # Inicializar BFS
        cola.append(nodo_inicio)
        visitados.add(nodo_inicio.ObtenerValor())
        
        while cola:
            nodo_actual = cola.popleft()
            
            # Explorar vecinos
            for vecino in nodo_actual.ObtenerVecinos():
                valor_vecino = vecino.ObtenerValor()
                if valor_vecino not in visitados:
                    visitados.add(valor_vecino)
                    cola.append(vecino)
                    arbolBFS.AgregarArista(nodo_actual.ObtenerValor(),valor_vecino)
        return arbolBFS

    def DfsR(self, inicio):
        '''
        Busqueda a profundidad. Recursivamente
        Args:
            nodo: Nodo inicial
        '''
        nodo_inicio = self.ObtenerNodo(inicio)
        if not nodo_inicio:
            return Grafo()
        
        visitados = set()
        ArbolDfsR = Grafo()
        
        def Dfs(nodo):
            valor = nodo.ObtenerValor()
            visitados.add(valor)
            
            for vecino in nodo.ObtenerVecinos():
                if vecino.ObtenerValor() not in visitados:
                    ArbolDfsR.AgregarArista(valor,vecino.ObtenerValor())
                    Dfs(vecino)
        Dfs(nodo_inicio)
        return ArbolDfsR

    def DfsIte(self, inicio):
        """
        Búsqueda a profundidad iterativa que construye el árbol DFS.
        
        Args:
            grafo: Objeto de la clase Grafo
            inicio: Valor del nodo inicial

        Returns:
            Grafo que representa el árbol DFS construido
        """
        nodo_inicio = self.ObtenerNodo(inicio)
        if not nodo_inicio:
            return Grafo()

        visitados = set()
        pila = [nodo_inicio]
        ArbolDfsI = Grafo()
        ArbolDfsI.AgregarNodo(nodo_inicio.ObtenerValor())

        while pila:
            nodo_actual = pila.pop()
            valor_actual = nodo_actual.ObtenerValor()
            if valor_actual not in visitados and nodo_actual not in ArbolDfsI.ObtenerNodos():
                ArbolDfsI.AgregarNodo(valor_actual)
                visitados.add(valor_actual)
                for vecino in reversed(nodo_actual.ObtenerVecinos()):
                    valor_vecino = vecino.ObtenerValor()
                    if valor_vecino not in visitados and vecino not in pila:
                        ArbolDfsI.AgregarNodo(valor_vecino)
                        pila.append(vecino)
                        ArbolDfsI.AgregarArista(valor_actual, valor_vecino)
        return ArbolDfsI

    def Dijkstra(self, inicio):
        """
        Algoritmo de Dijkstra para encontrar el árbol de caminos más cortos desde un nodo inicial.
        
        Args:
            inicio: Valor del nodo inicial
            
        Returns:
            Un objeto de la clase Grafo que representa el árbol de caminos más cortos
        """
        nodo_inicio = self.ObtenerNodo(inicio)
        if not nodo_inicio:
            return Grafo()
        # Inicializar estructuras
        distancias = {nodo.ObtenerValor(): float('inf') for nodo in self.ObtenerNodos()}
        distancias[inicio] = 0
        visitados = set()
        cola_prioridad = [(0, nodo_inicio)]  # (distancia, nodo)
        arbol_dijkstra = Grafo()
        arbol_dijkstra.AgregarNodo(inicio)
        while cola_prioridad:
            distancia_actual, nodo_actual = cola_prioridad.pop(0)
            valor_actual = nodo_actual.ObtenerValor()
            if valor_actual in visitados:
                continue
            visitados.add(valor_actual)
            for vecino in nodo_actual.ObtenerVecinos():
                valor_vecino = vecino.ObtenerValor()
                nueva_distancia = distancia_actual + 1  # Suponiendo peso 1 para las aristas
                if nueva_distancia < distancias[valor_vecino]:
                    distancias[valor_vecino] = nueva_distancia
                    cola_prioridad.append((nueva_distancia, vecino))
                    cola_prioridad.sort(key=lambda x: x[0])  # Ordenar por distancia
                    # Agregar nodo y arista al árbol de caminos más cortos
                    arbol_dijkstra.AgregarNodo(valor_vecino)
                    arbol_dijkstra.AgregarArista(valor_actual, valor_vecino)
        # Crear un diccionario de distancias para cada nodo y su respectivo valor de distancia
        strdistancias ={}
        for nodo, distancia in distancias.items():
            strdistancias[nodo] = f"[label=\"{inicio}_({distancia})\"];"
        
        return arbol_dijkstra, strdistancias

    def Kruskal(self):
        """
        Algoritmo de Kruskal para encontrar el árbol de expansión mínima.
        
        Returns:
            Un objeto de la clase Grafo que representa el árbol de expansión mínima
        """
        arbol_kruskal = Grafo(self.dirigido)
        # Ordenar las aristas por peso (aquí asumimos peso 1 para todas las aristas)
        aristas_ordenadas = sorted(self.aristas, key=lambda x: 1)
        # Inicializar conjuntos disjuntos para cada nodo
        conjuntos = {nodo.ObtenerValor(): {nodo.ObtenerValor()} for nodo in self.ObtenerNodos()}
        for arista in aristas_ordenadas:
            origen = arista.ObtenerNodos()[0].ObtenerValor()
            destino = arista.ObtenerNodos()[1].ObtenerValor()
            # Verificar si los nodos de la arista están en conjuntos diferentes
            if conjuntos[origen] != conjuntos[destino]:
                # Unir los conjuntos
                conjunto_unido = conjuntos[origen].union(conjuntos[destino])
                for nodo in conjunto_unido:
                    conjuntos[nodo] = conjunto_unido
                # Agregar la arista al árbol de expansión mínima
                arbol_kruskal.AgregarArista(origen, destino)
        return arbol_kruskal

    def KruskalInverso(self):
        """
        Algoritmo de Kruskal inverso (Reverse-Delete) para encontrar el árbol de expansión mínima.
        Elimina aristas de mayor a menor peso, manteniendo el grafo conectado.
        Returns:
            Un objeto de la clase Grafo que representa el árbol de expansión mínima
        """
        # Copia del grafo original
        arbol = self.Copia()
        # Ordenar aristas de mayor a menor peso (peso 1, así que solo invierte)
        aristas_ordenadas = sorted(arbol.ObtenerAristas(), key=lambda x: 1,reverse=True)
        # Recorrer las aristas en orden descendente
        for arista in aristas_ordenadas:
            origen = arista.ObtenerNodos()[0].ObtenerValor()
            destino = arista.ObtenerNodos()[1].ObtenerValor()
            # Eliminar la arista
            arbol.EliminarArista(origen, destino)
            # Verificar si el grafo sigue conectado
            if not arbol.Conectado():
                # Si se desconecta, volver a agregar la arista
                arbol.AgregarArista(origen, destino)
        return arbol

    def Conectado(self):
        """
        Verifica si el grafo esta conectado con todos los nodos  usando BFS.
        Returns:
            True si esta conectado , False no estan todos los nodos.
        """
        nodos = self.ObtenerNodos()
        if not nodos:
            return "El grafo está vacío"
        arbolBfs = self.BFS(nodos[0].ObtenerValor())
        
        if len(nodos) != len(arbolBfs.ObtenerNodos()):
            return False
        else:
            return True

    def Prim(self):
        """
        Algoritmo de Prim para encontrar el árbol de expansión mínima.

        Returns:
            Un objeto de la clase Grafo que representa el árbol de expansión mínima
        """
        arbol_prim = Grafo(self.dirigido)
        nodos = self.ObtenerNodos()
        if not nodos:
            return arbol_prim
        visitados = set()
        cola_prioridad = []
        # Comenzar desde un nodo arbitrario
        nodo_inicio = nodos[0]
        visitados.add(nodo_inicio.ObtenerValor())
        arbol_prim.AgregarNodo(nodo_inicio.ObtenerValor())
        # Agregar vecinos del nodo inicial a la cola de prioridad
        for vecino in nodo_inicio.ObtenerVecinos():
            cola_prioridad.append((1, nodo_inicio, vecino))  # (peso, origen, destino)
        # Mientras haya nodos en la cola de prioridad
        while cola_prioridad:
            # Ordenar la cola por peso (aunque todos son 1, por si acaso)
            cola_prioridad.sort(key=lambda x: x[0])
            peso, origen, destino = cola_prioridad.pop(0)
            valor_destino = destino.ObtenerValor()
            if valor_destino not in visitados:
                visitados.add(valor_destino)
                arbol_prim.AgregarNodo(valor_destino)
                arbol_prim.AgregarArista(origen.ObtenerValor(), valor_destino)
                for vecino in destino.ObtenerVecinos():
                    if vecino.ObtenerValor() not in visitados:
                        cola_prioridad.append((1, destino, vecino))
        return arbol_prim