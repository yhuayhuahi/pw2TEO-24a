from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def myHomeView(request, *args, **kargs):
    mycontext = {
        'mytext': 'Esto es sobre nosotros :|',
        'mynumber': 123,
        'mylist': [1, 2, 3, 4, 5, 6, 7]
    }
    return render(request, 'home.html', mycontext)
