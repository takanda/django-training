from django.urls import path
from .views import test_get_api, test_post_api


urlpatterns = [
    path("test-get-api/", test_get_api),
    path("test-post-api/", test_post_api),
]