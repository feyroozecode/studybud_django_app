from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse


# Create your views here.  
rooms = [
    { 'id': 1, 'name': 'Lets Learn VueJs' },
    { 'id': 2, 'name': 'Create a Tuorial' },
    { 'id': 3, 'name': 'Code my own Django Rest API' },
]

def home(request):
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)


def room(request, pk):
    room = None
    for i in rooms:
        if i['id'] == int(pk):
            room = i
    context = { 'room': room }
    
    return render(request, 'base/room.html', context)
