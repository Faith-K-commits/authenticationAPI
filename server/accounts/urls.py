from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('register/', views.register_user, name='register'),
    path('login/', views.login_user, name='login'),
    path('users/<uuid:user_id>/', views.get_user_record, name="get_user"),
    path('organisations/', views.get_user_organisations, name='get_user_organisations'),
    path('organisations/<uuid:org_id>/', views.get_organisation_record, name='get_organisation_record'),
    path('organisations/create/', views.create_organisation, name='create_organisation'),
    path('organisations/<uuid:org_id>/users/', views.add_user_to_organisation, name='add+user_to_organisation'),
]
