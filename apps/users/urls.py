from django.urls import path
from .views import RegisterUsers

urlpatterns = [

    # url for Lunch
    path('register/', RegisterUsers.as_view(), name='register'),
]