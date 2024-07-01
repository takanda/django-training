from django.urls import path
from .views import TestAPI


urlpatterns = [
    path("api", TestAPI.as_view()),
]