from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='home'),
    path('members/', views.members, name='members'),
    path('members/member_details/<int:id>', views.member_details, name='details'),
    path('testing/', views.testing, name='testing'),
]