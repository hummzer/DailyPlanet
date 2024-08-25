# main/urls.py 
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("post/<int:pk>/", views.detail, name="detail"),
    path("category/<category>/", views.category, name="category"),
]
