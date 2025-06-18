<<<<<<< HEAD
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')


def room(request):
=======
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')


def room(request):
>>>>>>> 7dc7f0b (Added a new admin feature)
    return render(request,'room.html')