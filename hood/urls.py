from . import views
from django.urls import path

urlpatterns=[
    path('', views.home, name='home'),
    path('search/', views.search_hood, name='search_hoods'),
    
    path('mtaani/<mtaani_id>',views.mtaani,name='mtaani'),
    path('hood/', views.add_hood, name='add_hood'),
    path('joinhood/<mtaani_id>',views.join_hood,name="joinhood"),
    path('leavehood/<mtaani_id>',views.leave_hood,name="leavehood"),
    path('addbusiness/<mtaani_id>', views.createbusiness, name='createbusiness'),
    path('post/<mtaani_id>', views.post, name='post'),
]