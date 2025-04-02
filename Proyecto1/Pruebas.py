import Grafo as gr

grafoMalla = gr.Grafo()
grafoMalla.generar_malla(filas=30,columnas=30)
grafoMalla.archivo_grafo('GrafoMalla')

grafoErdosReny= gr.Grafo()
grafoErdosReny.grafoErdosReny(nodos=500,aristas=1500)
grafoErdosReny.archivo_grafo('ErdosReny')
    
grafoGilbert = gr.Grafo()
grafoGilbert.grafoGilbert(50,0.25)
grafoGilbert.archivo_grafo('grafoGilbert')

grafoSimple=gr.Grafo()
grafoSimple.grafoSimple(nodos=50,r=10)
grafoSimple.archivo_grafo('grafoSimple')

grafoDoroMendes=gr.Grafo()
grafoDoroMendes.GrafoDorogovtsevMendes(50)
grafoDoroMendes.archivo_grafo('grafoDoroMendes')

grafoGusano=gr.Grafo()
grafoGusano.grafoBarabasiAlbert(50,3)
grafoGusano.archivo_grafo('Gusano')
