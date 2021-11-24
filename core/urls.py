from django.urls import path 
from . import views

urlpatterns = [
    path("base", views.base, name="base"),
    path("", views.index, name="index"),
    path("tomahora", views.tomahora, name="tomahora"),
    path("contact", views.contact, name="contact"),
    path("passr", views.passr, name="passr"),
    path("register", views.register, name="register"),
]
