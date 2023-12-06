from django.urls import path
from . import views

urlpatterns =[
    path("", views.index, name="index.html"),
    path("segunda", views.index, name="index2"),
]