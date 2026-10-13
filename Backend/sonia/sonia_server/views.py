from django.shortcuts import render


def home(request):
    """Render the sonia_server homepage."""
    return render(request, 'page/home.html')
# This view renders the homepage template stored in the page folder