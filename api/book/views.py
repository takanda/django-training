from rest_framework import generics
from .models import Auther
from .serializers import AutherSerializer

class AutherListView(generics.ListAPIView):
    queryset = Auther.objects.all()
    serializer_class = AutherSerializer
