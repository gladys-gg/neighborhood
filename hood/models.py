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
    

#User Model
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = CloudinaryField('image')
    bio = models.TextField(max_length=500, blank=True, null=True)
    phone_number= models.CharField(max_length=50, blank=True, null=True)
    joined_on=models.DateTimeField(auto_now=True)
    neighbourhood = models.ForeignKey(NeighbourHood, on_delete=models.CASCADE,null=True)


    def update(self):
        self.save()

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()
    def __str__(self):
        return str(self.user)