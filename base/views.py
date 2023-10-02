from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Room

# Create your views here.  


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
