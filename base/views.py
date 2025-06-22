from django.shortcuts import render,redirect
from .models import Room #this gets the the room mode 
from .models import Topic
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    return render(request,'home.html')


def room(request):
    return render(request,'room.html')







def createRoom(request):
    context = {}
    first_room = Room.objects.first()  # Get the first room from the database

    if request.method == 'POST':
        room_name = request.POST.get('room_name')
        topic_name = request.POST.get('topic')

        topic, created = Topic.objects.get_or_create(name=topic_name)


        Room.objects.create(
                host=request.user,
                topic=topic,
                name=room_name
            )
        return redirect('home')  

    # This runs only for GET requests
    return render(request, 'createroom.html', {'first_room': first_room})




