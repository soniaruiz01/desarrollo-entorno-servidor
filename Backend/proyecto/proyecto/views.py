from django.shortcuts import render
# render allows HTML to be displayed in google
def homepage(request):
    return render(request, 'home.html')
# return the request of google
    
