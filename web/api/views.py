from django.shortcuts import render
import subprocess


def test(request):
    subprocess.Popen(["python", "manage.py", "api"])
    return render(request, "api/test.html")
