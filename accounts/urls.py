from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('auth/register/', views.register_user, name='register'),
    path('auth/login/', views.login_user, name='login'),
    path('api/users/<str:user_id>/', views.get_user, name="get_user"),
]
