from django.urls import path

from profiles.views import ProfileCreateView, ProfileUpdateView

app_name = 'profiles'

urlpatterns = [
    path('update/<int:pk>', ProfileUpdateView.as_view(), name='update'),
    path('create/', ProfileCreateView.as_view(), name='create'),
]