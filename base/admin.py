<<<<<<< HEAD
from django.contrib import admin

# Register your models here
from .models import Room

admin.site.register(Room)
=======
from django.contrib import admin

# Register your models here
from .models import Room,Topic,Message

admin.site.register(Room)
admin.site.register(Message)
admin.site.register(Topic)
>>>>>>> 7dc7f0b (Added a new admin feature)
