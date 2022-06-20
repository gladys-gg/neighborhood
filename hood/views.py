from django.shortcuts import render
from django.shortcuts import get_object_or_404, render,redirect
from .models import Business, NeighbourHood, Post, Profile
from django.contrib.auth.decorators import login_required
from .forms import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login


# Create your views here.
def index(request):
    mtaani = NeighbourHood.objects.all()
    return render(request, 'index.html',{'mtaani':mtaani})

def profile(request):
#Get the profile
    current_user=request.user
    profile = Profile.objects.filter(id=current_user.id).first()
    if request.method == 'POST':
        profileform = UpdateProfileForm(request.POST,request.FILES,instance=profile)
        if  profileform.is_valid:
            profileform.save(commit=False)
            profileform.user=request.user
            profileform.save()
            return redirect('profile')
    else:
        form=UpdateProfileForm()
    return render(request,'profile.html',{'form':form})

@login_required
def mtaani(request, mtaani_id):
    mtaani = NeighbourHood.objects.get(id=mtaani_id)
    postform = PostForm()
    businessform = BusinessForm()
    current_user = request.user
    business = Business.objects.filter(neighbourhood_id=mtaani)
    users = Profile.objects.filter(neighbourhood=mtaani)
    posts = Post.objects.filter(neighbourhood=mtaani)
    return render(request, 'mtaani.html', {'postform':postform, 'businessform': businessform, 'users':users,'current_user':current_user, 'mtaani':mtaani,'business':business,'posts':posts})

@login_required
def add_hood(request):
    if request.method == 'POST':
        hoodform = HoodForm(request.POST, request.FILES)
        if hoodform.is_valid():
            upload = hoodform.save(commit=False)
            upload.profile = request.user.profile
            upload.save()
            return redirect('home')
    else:
        hoodform = HoodForm()
    return render(request,'addhood.html',locals())


def createbusiness(request,mtaani_id):
    mtaani = NeighbourHood.objects.get(id=mtaani_id)
    if request.method == 'POST':
        businessform = BusinessForm(request.POST, request.FILES)
        if businessform.is_valid():
            business = businessform.save(commit=False)
            business.neighbourhood = mtaani
            business.user = request.user
            business.save()
        return redirect('neighbourhood', mtaani_id=mtaani.id)
    else:
        businessform = BusinessForm()
    return render(request,'business.html',locals())
