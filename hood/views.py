from django.shortcuts import render
from django.shortcuts import get_object_or_404, render,redirect
from .models import Business, NeighbourHood, Post, Profile
from django.contrib.auth.decorators import login_required
from .forms import UpdateProfileForm,NeighbourhoodForm,PostForm,BusinessForm, UserRegisterForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login


# Create your views here.
def index(request):
    mtaani = NeighbourHood.objects.all()
    return render(request, 'index.html',{'mtaani':mtaani})
