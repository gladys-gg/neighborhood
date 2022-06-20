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

def EditProfile(request):
    user = request.user.id
    profile = Profile.objects.get(user_id=user)

    if request.method == "POST":
        form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            profile.profile_pic = form.cleaned_data.get('profile_pic')
            profile.fullname = form.cleaned_data.get('fullname')
            profile.location = form.cleaned_data.get('location')
            profile.url = form.cleaned_data.get('url')
            profile.bio = form.cleaned_data.get('bio')
            profile.save()
            return redirect('profile', profile.user.id)
    else:
        form = UpdateProfileForm(instance=request.user.profile)

    context = {
        'form':form,
    }
    return render(request, 'editprofile.html', context)


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
            return redirect('index')
    else:
        hoodform = HoodForm()
    return render(request,'addhood.html',locals())

@login_required
def join_hood(request, mtaani_id):
    mtaani = get_object_or_404(NeighbourHood, id=mtaani_id)
    request.user.profile.neighbourhood = mtaani
    request.user.profile.save()
    return redirect('mtaani', mtaani_id = mtaani.id)

@login_required
def leave_hood(request, mtaani_id):
    mtaani = get_object_or_404(NeighbourHood, id=mtaani_id)
    request.user.profile.neighbourhood = None
    request.user.profile.save()
    return redirect('index')


def createbusiness(request,mtaani_id):
    mtaani = NeighbourHood.objects.get(id=mtaani_id)
    if request.method == 'POST':
        businessform = BusinessForm(request.POST, request.FILES)
        if businessform.is_valid():
            business = businessform.save(commit=False)
            business.neighbourhood = mtaani
            business.user = request.user
            business.save()
        return redirect('mtaani', mtaani_id=mtaani.id)
    else:
        businessform = BusinessForm()
    return render(request,'business.html',locals())

def post(request,mtaani_id):
    mtaani = NeighbourHood.objects.get(id=mtaani_id)
    if request.method == 'POST':
        postform = PostForm(request.POST, request.FILES)
        if postform.is_valid(): 
            post = postform.save(commit=False)
            post.neighbourhood = mtaani
            post.user = request.user
            post.save()
        return redirect('mtaani', mtaani_id=mtaani.id)
    else:
        postform = PostForm()
    return render(request,'post.html',locals())


def search_hood(request):

    if 'name' in request.GET and request.GET["name"]:
        search_term = request.GET.get("name")
        searched_hoods = NeighbourHood.search_by_name(search_term)
        print(searched_hoods)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"hoods": searched_hoods})
    
def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()

            # Profile.get_or_create(user=request.user)
            
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            user = authenticate(username=username, password=password)
            login(request,user)
            messages.success(request, f'Account created for { username }!!')
            return redirect('index')

    else:
        form = UserRegisterForm()
    context = {
        'form': form,
    }
    return render(request, 'registration/sign-up.html', context)

def signout(request): 
    return redirect('index')
