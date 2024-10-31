from django.urls import path
from .views import HomePageView
from .views import AboutPageView


urlpatterns = [
    path("", HomePageView.as_View(), name="home"),
    path("About/", AboutPageView.as_view(), name ="about"),
]

