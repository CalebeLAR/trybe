# events/urls.py
from django.urls import path
from events.views import about, index


urlpatterns = [
    path("", index, name="home-page"),
    path("about", about, name="about-page"),
]
