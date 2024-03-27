from django.urls import path
from .views import HomePageView

urlpatterns = [
    path("about/", HomePageView.as_view(), name="about"),
    path("", HomePageView.as_view(), name="home"),
]