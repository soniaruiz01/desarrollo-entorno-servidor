# from django.http import HttpResponse

# def homepage(request):
#     """Return the homepage response."""
#     return HttpResponse("Hello World!")

# This file defines the homepage view and returns a simple "Hello World" response when the page is accessed
from django.shortcuts import render


def homepage(request):
    """Render the homepage template."""
    return render(request, 'home.html')
# This view renders the home.html template as the homepage.