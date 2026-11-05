from django.shortcuts import render

def calendario(request, fecha):

    partes = fecha.split('-')

    mi_dia = partes[0]
    mi_mes = partes[1]
    mi_ano = partes[2]

    mensaje = "Esta es la fecha que has introducido."

    return render(request, 'calendario/fecha.html', {
        'dia': mi_dia,
        'mes': mi_mes,
        'ano': mi_ano,
        'mensaje': mensaje
    })