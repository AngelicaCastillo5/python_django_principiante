from typing import ContextManager
from django.http import HttpResponse
import datetime
from django.template import Template, Context

def saludo(request): #primera vista
    doc_externo=open("D:/aprendizaje extra/python_django_principiante/Python_Django/pildorasinformaticas/Proyecto1/Proyecto1/template/index.html")
    plt=Template(doc_externo.read())
    doc_externo.close()
    ctx=Context() #contexto
    #renderizar documento
    documento=plt.render(ctx)
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