from django.shortcuts import render

def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')

def about(request):
    """ A view to return the about page """

    return render(request, 'home/about.html')


def bad_request_400(request, exception):
    """ A view to return Custom 400 Error Page """
    
    return render(request, "error/400.html")


def forbidden_403(request, exception):
    """ A view to return Custom 403 Error Page """
    
    return render(request, "error/403.html")

        
def page_not_found_404(request, exception):
    """ A view to return Custom 404 Error Page """
    
    data = {}
    return render(request, "error/404.html", data)


def internal_server_500(request):
    """ A view to return Custom 500 Error Page """
    
    return render(request, "error/500.html")
