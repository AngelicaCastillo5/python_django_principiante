from django.http import HttpResponse
import datetime

def saludo(request): #primera vista
    documento="""<html>
    <body>
    <h1>
    Hola alumnos, esta es nuestra primera vista con Django
    </h1>
    </body>
    </html>
    """
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