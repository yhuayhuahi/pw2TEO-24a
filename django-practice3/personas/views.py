from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def myHomeView(request, *args, **kargs):
    mycontext = {
        'mytext': 'Esto es sobre nosotros :|',
        'mynumber': 123,
        'mylist': [33, 44, 55]
    }
    return render(request, 'home.html', mycontext)
