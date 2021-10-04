from django.urls import path
from accounts import views

app_name='account'
urlpatterns = [
    path('profile/', views.profile, name="profile"),
    path('profile/update/', views.profile_update, name='profile_update'),
]
