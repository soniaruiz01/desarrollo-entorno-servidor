from django.shortcuts import render
# render allows HTML to be displayed in google
def aplicacion(request):
 
 return render(request, 'aplicacion/home.html')  
# return the request in google

