from django.shortcuts import render
from django.http import HttpResponse
from app_two.models import User
# Create your views here.


def present(request):
    return HttpResponse("<em>My Second App</em>")


def index(request):
    values = {"developer": "Developed by me on trial"}
    return render(request, 'app_two/index.html', context=values)


def webindex(request):
    return HttpResponse("Welcome to my page. Go to /users to see the list of users")


def getUsers(request):
    users = User.objects.order_by('firstName')
    user_dict = {'records': users}
    return render(request, 'app_two/index.html', context=user_dict)
