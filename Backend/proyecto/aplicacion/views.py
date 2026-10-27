from django.shortcuts import render
def aplicacion(request):
 return render(request, 'aplicacion/home.html')
