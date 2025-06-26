from django.shortcuts import render,redirect
from .models import Room #this gets the the room mode 
from .models import Topic
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    return render(request,'home.html')


def login(request):
    return render(request,'room.html')








def createRoom(request):
   
    first_room = Room.objects.first()  # Get the first room from the database
    searching = None

    if request.method == 'POST':
        room_name = request.POST.get('room_name')
        topic_name = request.POST.get('topic')
        searchquery = request.POST.get('searchbutton')
        if searchquery:
            try:
                searching = Room.objects.get(name=searchquery)
            
            except Room.DoesNotExist:
                searching = None

        


        if room_name and topic_name:
            try:
                topic, created = Topic.objects.get_or_create(name=topic_name) #created is false if there is topic already exist


                Room.objects.create(
                    host=request.user,
                    topic=topic,
                    name=room_name
            )
            except Room.DoesNotExist:
                first_room = None

        
        

    # This runs only for GET requests
    return render(request, 'createroom.html', {'first_room': first_room,
                                               'searching': searching})







