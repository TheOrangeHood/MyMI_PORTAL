from django.contrib import admin
from django.urls import path,include
from home import views
urlpatterns = [
    path('',views.index, name="home"),
    path('login',views.loginUser, name="login"),
    path('logout',views.logoutUser, name="logout"),
    path('add',views.addTask, name="add"),
    path('delete/<int:pk>',views.deleteTask, name="deleteTask"),
    path('complete/<int:pk>',views.completeTask, name="completeTask"),
    path('assigned',views.assignedTask, name="assigned"),
    path('assigned_coordie',views.assignedTask_coordie, name="assigned_coordie"),

    # path('save',views.saveTask, name="save"),

]