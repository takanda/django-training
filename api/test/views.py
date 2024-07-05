from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError


class TestAPI(APIView):

    def get(self, request):
        raise ValidationError("Invalid request.")



