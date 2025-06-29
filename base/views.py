from django.shortcuts import render,redirect
from .models import partic #this gets the the room mode 
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import check_password
from django.contrib.auth.decorators import login_required



# Create your views here.
def home(request):
    return render(request,'home.html')


def login_views(request):
    if request.method =="POST":
        username = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user = partic.objects.get(name=username)

            if user.password == password and user.name == username:
                return redirect('/') 
            
            else:
                return render(request, "room.html",{"error":"invalid password"})
        
        except partic.DoesNotExist:
        
            return render(request, "room.html", {"error": "User not found"})
    
    return render(request,"room.html")
        





def forgot(request):
    return render(request,'forgot.html')










'''

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





'''

