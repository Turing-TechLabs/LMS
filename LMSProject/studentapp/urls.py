from django.urls import path, include
from studentapp.views import * 

urlpatterns = [
    path('', index, name='index'),
]
