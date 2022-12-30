from django.urls import path
from app1.views import *
app1_name='something1'

urlpatterns=[
    path('file1/',file1,name='file1'),
]
