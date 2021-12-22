from typing import ContextManager
from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.template import loader 
class persona(object):
    def __init__(self,nombre,apellido):
        self.nombre=nombre
        self.apellido=apellido


def saludo(request): #primera vista
    p1=persona("Profesor Juan","Diaz")
    nombre="Juan"
    apellido="Diaz"
    temas=["Plantillas","Modelos","Formularios","Vistas","Despliegue"] #contexto
    tema2=[]
    #renderizar documento
    ahora=datetime.datetime.now()
    #doc_externo=open("D:/aprendizaje extra/python_django_principiante/Python_Django/pildorasinformaticas/Proyecto1/Proyecto1/templates/index.html")
    #plt=Template(doc_externo.read())
    #doc_externo.close()
    doc_externo=loader.get_template('index.html')
    #ctx=Context({"nombre_persona":p1.nombre,"apellido_persona":p1.apellido,"fecha":ahora,"temas":temas})
    #documento=plt.render(ctx)
    diccionario={"nombre_persona":p1.nombre,"apellido_persona":p1.apellido,"fecha":ahora,"temas":temas}
    documento=doc_externo.render(diccionario)
    return HttpResponse(documento)

def despedida(request):
    return HttpResponse("Hasta luego alumnos de django")

def dameFecha(request):
    fecha_actual=datetime.datetime.now()
    documento="""<html>
    <body>
    <h1>
    Fecha y hora actuales %s
    </h1>
    </body>
    </html>
    """% fecha_actual
    return HttpResponse(documento)

def calculaEdad(request, edad,agno):
    #edadActual=18
    periodo=agno-2021
    #edadfutura=edadActual+periodo
    edadFutura=edad+periodo
    documento="<html><body><h2> En el año %s tendras %s años"%(agno,edadFutura)  #marcadores de posicion %s
    return HttpResponse(documento)