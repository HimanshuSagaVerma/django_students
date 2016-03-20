from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^my-first-page/$', views.my_first_page),
]
