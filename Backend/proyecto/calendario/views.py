from django.shortcuts import render
# to return html
from datetime import datetime
# this import is to work with dates and times


def calendario(request, fecha):
# create the function  

    try:
        
        fecha_objeto = datetime.strptime(fecha, '%d-%m-%Y')
        # convert the text  into a date
        # strp is to convert it


        mi_dia = fecha_objeto.day
        mi_mes = fecha_objeto.month
        mi_ano = fecha_objeto.year
        # separate the date into three parts

        mensaje = "La fecha introducida es correcta"

    except ValueError:
    # this part tuns when the 'try' produces an error

        mi_dia = ""
        mi_mes = ""
        mi_ano = ""
        mensaje = "El formato de fecha no es correcto. Utiliza DD-MM-AAAA"

    return render(request, 'fecha.html', {
        'dia': mi_dia,
        'mes': mi_mes,
        'ano': mi_ano,
        'mensaje': mensaje
    })