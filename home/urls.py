from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index.html'),
    path('login',views.loginUser, name='login.html'),
    path('logout',views.logoutUser, name='logout.html'),
    path('signup',views.signupUser, name='signup.html'),

]
