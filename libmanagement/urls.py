from django.contrib import admin
from django.urls import path,include
from . import views


app_name = "libmanagement"

urlpatterns = [
    path('',views.index,name = "index"),
    path('signup',views.signup,name = "signup"),
    path('signin',views.signin,name = "signin"),
    path('addingbooks',views.addingbooks,name = "addingbooks"),
    path('actions',views.actions,name = "actions"),
    path('deletingbook',views.deletingbook,name = "deletingbook"),
    path('deletingbook/<int:book_id>',views.deletingbook,name = "deletingbook"),
    path('searchbook',views.searchbook,name= "searchbook"),
    path('updatebook',views.updatebook,name = "updatebook"),
    path('updateaction/<int:book_id>',views.updateaction,name = "updateaction"),
    path('updatebutton',views.updatebutton,name = "updatebutton"),
    
    
    
]
