from django.urls import path
from .views import hello_world, AccountCreateView

app_name = "accounts"

urlpatterns = [
    path('hello/', hello_world, name='hello_world'),
    path('create/', AccountCreateView.as_view(), name='create'),
]