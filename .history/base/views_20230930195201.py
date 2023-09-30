from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.  
rooms = [
    { 'id': 1, 'name': 'Lets Learn VueJs' },
    { 'id': 2, 'name': 'Create a Tuorial' },
    { 'id': 3, 'name': 'Code my own Django Rest API' },
]

def home(request):
    return render(request, 'home.html', {'rooms': rooms})


def room(request):
    return render(request, 'room.html')
