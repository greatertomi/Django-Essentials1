from django.conf.urls import url
from app_two import views

urlpatterns = [
    url('present', views.present),
    url('', views.index)
]
