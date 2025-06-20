from django.shortcuts import render
from .models import Room #this gets the the room mode 

# Create your views here.
def home(request):
    return render(request,'home.html')


def room(request):
    return render(request,'room.html')

def createRoom(request):
    context = {}
    first_room = Room.objects.first()  # Get the first room from the database
    return render(request,'createroom.html',{'first_room': first_room})

