from django.urls import path
from app2.views import *
app_name='something2'

urlpatterns=[
    path('file2/',file2,name='file2'),
]

