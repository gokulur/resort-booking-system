from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def accomodation(request):
    return render(request, 'accomodation.html')

def gallery(request):
    return render(request, 'gallery.html')