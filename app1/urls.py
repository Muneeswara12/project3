from app1.views import *
from django.urls import path
app_name='somthing'
urlpatterns=[
    path('muni/',muni,name='muni'),
    path('muni1/',muni1,name='muni1'),
]