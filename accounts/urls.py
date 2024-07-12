from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('auth/register/', views.register_user, name='register'),
    path('auth/login/', views.login_user, name='login'),
]
