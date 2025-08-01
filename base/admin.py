from django.contrib import admin

# Register your models here
from .models import partic
from .models import visitor

admin.site.register(partic)
admin.site.register(visitor)
