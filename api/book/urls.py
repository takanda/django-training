from django.urls import path
from .views import AutherListView

urlpatterns = [
    path('authers/', AutherListView.as_view(), name='auther-list'),
]
