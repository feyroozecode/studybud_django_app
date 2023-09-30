from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render()

def room(request):
    return HttpResponse('Room Route')
