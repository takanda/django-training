from django.shortcuts import render
import subprocess


def test_get_api(request):
    subprocess.Popen(["python", "manage.py", "get_api", "1", "2", "3", "4"])
    return render(request, "api/test.html")

def test_post_api(request):
    subprocess.Popen(["python", "manage.py", "post_api", "1", "2", "3", "4"])
    return render(request, "api/test.html")
