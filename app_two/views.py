from django.shortcuts import render
from django.http import HttpResponse
from app_two.models import User
from app_two.forms import NewUserForm
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
    return render(request, 'app_two/users.html', context=user_dict)


def signup(request):
    form = NewUserForm()
    if request.method == "POST":
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print("Error Form invalid")
    return render(request, 'app_two/signup.html', {'form': form})
