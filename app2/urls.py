from app2.views import *
from django.urls import path
app_name='nothing'
urlpatterns=[
    path('muni2/',muni2,name='muni2'),
    path('muni3/',muni3,name='muni3'),
]