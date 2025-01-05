from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path(r"^$", views.index, name="index"),
    path("song/", views.songs, name="songs"),  # Changed from empty string to "song/"
    path("photos/", views.photos, name="photos"),  # Updated this line to include "photos/"
    path("signup/", views.signup, name="signup"),  # Updated this line to include "signup/"
    path("login/", views.login_view, name="login"),  # Updated login URL
    path("logout/", views.logout_view, name="logout"),  # Updated logout URL
    path("concert/", views.concerts, name="concerts"),  # Updated to "concert/" instead of empty string
    path("concert-detail/<int:id>", views.concert_detail, name="concert_detail"),
    path("concert_attendee/", views.concert_attendee, name="concert_attendee"),
]

