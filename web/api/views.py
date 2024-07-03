from django.http import HttpResponse
from django.core import management
from django.shortcuts import render


def test(self):
    response = management.call_command("api")
    return HttpResponse(response)
