
from django.urls import path
from employee import views

urlpatterns = [
    path('Signup',views.Signup),
    path('Login',views.signin),
    path('create',views.create),
    path('index',views.index),
    path('update', views.update),
    path('delete',views.delete),
    path('dashboard',views.dashBoard),
    path('Logout',views.Logout)



]
