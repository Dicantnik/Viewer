from django.urls import path
from rooms import views
from .views import main

app_name = 'rooms'

urlpatterns = [
   
    path('', views.main, name='main'),
    
    # path('login/', views.login),
    # path('registration/', views.registration),
]