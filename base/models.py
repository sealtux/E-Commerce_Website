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
    


class visitor(models.Model):
    ip_address = models.GenericIPAddressField(unique=True)
    visit_count = models.PositiveIntegerField(default=0)
    visited_at = models.DateTimeField(auto_now=True)
    item_ids = models.TextField(blank=True, null=True)  # Add this if not already

    def __str__(self):
        return f"{self.ip_address} ({self.visit_count} clicks)"

    def add_item(self, item_id):
        current = self.item_ids.split(',') if self.item_ids else []
        current.append(item_id)
        self.item_ids = ','.join(current)
     