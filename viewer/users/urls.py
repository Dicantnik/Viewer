from django.urls import path, include
from users import views
from .views import register, login

app_name = 'users'

urlpatterns = [
    path('login/', views.auth_login, name='login'),
    path('', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register'),
    path('logout/', views.logoutus, name='logout'),
    
    # path('login/', views.login),
    # path('registration/', views.registration),
]