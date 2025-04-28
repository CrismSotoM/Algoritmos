import Proyecto.Grafo as gr

grafoMalla = gr.Grafo()
grafoMalla.generar_malla(filas=8,columnas=8)
grafoMalla.archivo_grafo('GrafoMalla50')

grafoMalla = gr.Grafo()
grafoMalla.generar_malla(filas=15,columnas=15)
grafoMalla.archivo_grafo('GrafoMalla200')

grafoMalla = gr.Grafo()
grafoMalla.generar_malla(filas=25,columnas=25)
grafoMalla.archivo_grafo('GrafoMalla500')

grafoErdosReny= gr.Grafo()
grafoErdosReny.grafoErdosReny(nodos=50,aristas=150)
grafoErdosReny.archivo_grafo('ErdosReny50')

grafoErdosReny= gr.Grafo()
grafoErdosReny.grafoErdosReny(nodos=300,aristas=900)
grafoErdosReny.archivo_grafo('ErdosReny300')

grafoErdosReny= gr.Grafo()
grafoErdosReny.grafoErdosReny(nodos=500,aristas=1500)
grafoErdosReny.archivo_grafo('ErdosReny500')
    
grafoGilbert = gr.Grafo()
grafoGilbert.grafoGilbert(50,0.25)
grafoGilbert.archivo_grafo('grafoGilbert50')


grafoGilbert = gr.Grafo()
grafoGilbert.grafoGilbert(200,0.05)
grafoGilbert.archivo_grafo('grafoGilbert200')

grafoGilbert = gr.Grafo()
grafoGilbert.grafoGilbert(500,0.01)
grafoGilbert.archivo_grafo('grafoGilbert500')


grafoSimple=gr.Grafo()
grafoSimple.grafoSimple(nodos=50,r=10)
grafoSimple.archivo_grafo('grafoSimple50')

grafoSimple=gr.Grafo()
grafoSimple.grafoSimple(nodos=200,r=20)
grafoSimple.archivo_grafo('grafoSimple200')

grafoSimple=gr.Grafo()
grafoSimple.grafoSimple(nodos=500,r=30)
grafoSimple.archivo_grafo('grafoSimple500')

grafoDoroMendes=gr.Grafo()
grafoDoroMendes.GrafoDorogovtsevMendes(50)
grafoDoroMendes.archivo_grafo('grafoDoroMendes50')

grafoDoroMendes=gr.Grafo()
grafoDoroMendes.GrafoDorogovtsevMendes(200)
grafoDoroMendes.archivo_grafo('grafoDoroMendes200')

grafoDoroMendes=gr.Grafo()
grafoDoroMendes.GrafoDorogovtsevMendes(500)
grafoDoroMendes.archivo_grafo('grafoDoroMendes500')

grafoGusano=gr.Grafo()
grafoGusano.grafoBarabasiAlbert(50,3)
grafoGusano.archivo_grafo('Gusano50')

grafoGusano=gr.Grafo()
grafoGusano.grafoBarabasiAlbert(200,5)
grafoGusano.archivo_grafo('Gusano200')

grafoGusano=gr.Grafo()
grafoGusano.grafoBarabasiAlbert(500,7)
grafoGusano.archivo_grafo('Gusano500')