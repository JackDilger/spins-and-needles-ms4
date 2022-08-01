from django.shortcuts import render


# A view to return the index page
def index(request):
    return render(request, 'home/index.html')

