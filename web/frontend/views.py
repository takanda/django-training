from django.shortcuts import render

def Index(request):
    return render(request, "frontend/index.html")

def IndexCopy(request):
    return render(request, "frontend/index_copy.html")

    