from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('auth/register', views.register_user, name='register'),
    path('auth/login', views.login_user, name='login'),
    path('api/users/<uuid:user_id>', views.get_user_record, name="get_user"),
    path('api/organisations', views.get_user_organisations, name='get_user_organisations'),
]
