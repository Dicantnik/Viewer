from django.urls import path
from rooms import views
from .views import MainView, room, profileview

app_name = 'rooms'

urlpatterns = [
   
    path('', MainView.as_view(), name='main'),
    path('room/<code>', room, name="room"),
    path('profile', profileview, name='profile')
    # path('login/', views.login),
    # path('registration/', views.registration),
]