from django.urls import path
from . import views

urlpatterns = [
    path('uploadData/', views.upload_csv, name='upload_csv'),
]