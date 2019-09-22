from django.urls import path, include
from .views import index, logout, login, register, profile

urlpatterns = [
    path('accounts/register/', register, name='register'),
    path('accounts/profile/', profile, name='profile'),
    path('accounts/logout/', logout, name='logout'),
    path('accounts/login/', login, name='login'),
    path('accounts/', include('django.contrib.auth.urls')),
]