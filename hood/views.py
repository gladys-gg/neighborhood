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

