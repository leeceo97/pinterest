from django.urls import path
from .views import hello_world

app_name = "accounts"

urlpatterns = [
    path('hello/', hello_world, name='hello_world')
]