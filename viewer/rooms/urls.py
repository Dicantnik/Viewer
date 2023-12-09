from django.urls import path
from rooms import views
from .views import MainView, room

app_name = 'rooms'

urlpatterns = [
   
    path('', MainView.as_view(), name='main'),
    path('room/<code>', room, name="room")
    
    # path('login/', views.login),
    # path('registration/', views.registration),
]