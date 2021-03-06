from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from .views import hello_world, AccountCreateView, AccountDetailView, AccountUpdateView, AccountDeleteView

app_name = "accounts"

urlpatterns = [
    path('hello/', hello_world, name='hello_world'),

    path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('detail/<int:pk>', AccountDetailView.as_view(), name='detail'),
    path('update/<int:pk>', AccountUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', AccountDeleteView.as_view(), name='delete'),
    path('create/', AccountCreateView.as_view(), name='create'),
]