from django.urls import path, include
from . import views

app_name = "vapp"

urlpatterns = [
    path("", views.index, name="index")
]
