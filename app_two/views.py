from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def present(request):
    return HttpResponse("<em>My Second App</em>")


def index(request):
    values = {"developer": "Developed by me on trial"}
    return render(request, 'app_two/index.html', context=values)
