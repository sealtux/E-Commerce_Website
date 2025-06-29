from django.db import models
from django.contrib.auth.models import User

# Create your models here.



    


class partic(models.Model):
    #host = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    #topic = models.ForeignKey(Topic,on_delete=models.SET_NULL,null = True)
    name = models.CharField(max_length= 200)
    password = models.TextField(max_length = 125)

    updated = models.DateTimeField(auto_now=True)
    created  = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.name
    




     