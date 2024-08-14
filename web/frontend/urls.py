from django.urls import path
from .views import Index, IndexCopy

app_name = "frontend"

urlpatterns = [
    path('', Index, name="index"),
    path('copy', IndexCopy, name="index_copy"),
]
