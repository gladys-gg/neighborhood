"""mtaani URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views
from hood import views
from django.contrib.auth import views as auth_views
from hood.views import profile

urlpatterns = [
    path('', include('hood.urls')),
    path('admin/', admin.site.urls),
            # User Authentication

    path('sign-up/',views.register,name='sign-up'),
    path('login/',auth_views.LoginView.as_view(template_name = 'registration/sign-in.html'),name='sign-in'),
    path('sign-out/', views.signout, name='sign-out'),
    path('user/', profile, name='profile'),
    # path('<username>/', UserProfile, name='profile'),
]