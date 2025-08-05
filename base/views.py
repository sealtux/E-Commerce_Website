import time
from django.shortcuts import render,redirect
from .models import partic #this gets the the room mode 
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import check_password
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import visitor
from django.http import JsonResponse
hello = {}
# Create your views here.
def home(request):
    
    return render(request,'home.html')



def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        return x_forwarded_for.split(',')[0]
    return request.META.get('REMOTE_ADDR')

def shop(request):
    if request.method == 'POST':
        action = request.POST.get('action')
        ip = get_client_ip(request)

        if action == 'movetofree':
            return redirect('free') 
        
        elif action == 'movetotrack':
            return redirect('track') 
        
        elif action == 'movetohelp':
            return redirect('help')
        
        elif action == 'movetogroup':
            return redirect('group')

        # Handle visit tracking
        lisitor, created = visitor.objects.get_or_create(ip_address=ip)
        lisitor.visit_count += 1
        lisitor.save()

        return JsonResponse({'status': 'success', 'visits': lisitor.visit_count})

    # GET request — load the page normally
    return render(request, 'Shop.html')



def freeitems(request):

    return render(request,'free.html')


def track(request):
    return render (request, "track.html")


def help(request):
    return render (request, "help.html")

def group(request):
    return render (request, "groups.html")


def login_views(request):
    
    if request.method =="POST":
        username = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user = partic.objects.get(name=username)

            if user.password == password and user.name == username:
                return redirect('shop') 
            
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

