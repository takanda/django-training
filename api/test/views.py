from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError, APIException
from api.settings import (STATUS_OK,
                          STATUS_CREATED,
                          STATUS_BAD_REQUEST,
                          STATUS_UNAUTHORIZED,
                          STATUS_METHOD_NOT_ALLOWED,
                          STATUS_TIMEOUT,
                          STATUS_CONFLICT,
                          STATUS_SERVER_ERROR,
                          STATUS_SERVER_UNAVAILABLE,
                          )

class RaiseErrorView(APIView):

    def get(self, request, code, msg):
        if code >= STATUS_BAD_REQUEST and code < STATUS_SERVER_ERROR:
            raise ValidationError(msg)
        elif code >= STATUS_SERVER_ERROR:
            raise APIException(msg)

        return Response({"message": msg, "code": status.HTTP_201_CREATED})
