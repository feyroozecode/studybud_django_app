from django.shortcuts import render

# Create your views here.
def home(request):
    return HttpResponse('Salam Aleykoum Hi')

def room(request):
    return HttpResponse('Room Route')
