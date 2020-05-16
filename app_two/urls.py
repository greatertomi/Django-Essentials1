from django.conf.urls import url
from app_two import views

urlpatterns = [
    url('present', views.present),
    url('other', views.index),
    url('signup', views.signup),
    url('', views.getUsers)
]
