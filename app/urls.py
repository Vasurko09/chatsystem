from django.urls import path
from . import views

urlpatterns = [
    path("", views.home),
    path("vasu/",views.client1,name="vasu")
]