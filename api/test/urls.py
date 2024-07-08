from django.urls import path
from .views import RaiseErrorView


urlpatterns = [
    path("api/<int:code>/<str:msg>", RaiseErrorView.as_view()),
]