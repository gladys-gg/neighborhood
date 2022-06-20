from django.db import models
from django.dispatch import receiver
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
import datetime as dt
from django.db.models.signals import post_save
from django.dispatch import receiver
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

# NeighbourHood Model


class NeighbourHood(models.Model):
    mtaani_name = models.CharField(max_length=50)
    description = models.TextField(max_length = 200,null = True)
    occupants_count = models.IntegerField(default=0)
    admin = models.ForeignKey(User, on_delete=models.CASCADE, null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    police_num=models.IntegerField(null=True,blank=True)
    hospital_num=models.IntegerField(null=True,blank=True)
    mtaani_pic=CloudinaryField(blank=True,)
    location = models.CharField(max_length = 50,null = True)

    def create_neigborhood(self):
        self.save()

    @classmethod
    def delete_neighbourhood(cls, id):
        cls.objects.filter(id=id).delete()

    
    @classmethod
    def search_by_name(cls, search_term):
        hood = cls.objects.filter(name__icontains=search_term)
        return hood

    # find neighbourhood by id
    @classmethod
    def find_neigborhood(cls, id):
        hood = cls.objects.get(id=id)
        return hood
    
    def __str__(self):
        return self.mtaani_name