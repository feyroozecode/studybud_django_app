from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Room

# Create your views here.  
static_rooms = [
    { 'id': 1, 'name': 'Lets Learn VueJs' },
    { 'id': 2, 'name': 'Create a Tuorial' },
    { 'id': 3, 'name': 'Code my own Django Rest API' },
]


def home(request):
    # get all rooms Object
    rooms = Room.objects.all()
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)


def room(request, pk):
    # get all rooms Object
    room = Room.objects.get(id=pk)
    context = { 'room': room }
    
    return render(request, 'base/room.html', context)
