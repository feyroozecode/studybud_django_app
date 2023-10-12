from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Room
from .forms import RoomForm

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

def createRoom(request):
    form = RoomForm()
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        
    context = {'form': form}
    return render(request, 'base/room_form.html', context)

def updateRoom(request, pk): 
    room = Room.objects.get(id=pk)
    form  = RoomForm(instance=room)
    
    if request.method == 'POST':                        # GET METHOD TYPE
        form = RoomForm(request.POST, instance=room)    # Get Room instance and parse there data to the form
        if form.is_valid():                             # check if form is valid
            form.save()                                 # save the form 
            return redirect('home')                     # redirect to home page

    context = {'form': form}
    return render(request, 'base/room_form.html', context)

def deleteRoom(request, pk):
    room = Room.objects.get(id=pk)
    
    if request.method == 'POST':
        room.delete()
        return redirect('home')
    
    return render(request, 'base/delete.html', {'obj': room}  )
    