from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def inicio(request):
    contexto = {"nombre": "pablo"}
    return render(request, "dispositivos/inicio.html", contexto)

def panel_dispositivos(request):
    dispositivos =[
        {"nombre": "sensor temperatura", "consumo":50},
        {"nombre": "medidor solar", "consumo":120},
        {"nombre": "sensor movimiento", "consumo":30},
        {"nombre": "calefactor", "consumo":200},
    ]

    consumo_maximo = 100

    return render(request, "dispositivos/panel.html",
    {"dispositivos": dispositivos,
    "consumo_maximo": consumo_maximo
    })