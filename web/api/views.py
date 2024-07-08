from django.shortcuts import render
import subprocess


def test(request):
    subprocess.Popen(["python", "manage.py", "api", "1", "2", "3", "4"])
    return render(request, "api/test.html")
