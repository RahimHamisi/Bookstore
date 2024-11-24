from django.urls import path

from BookService import views


urlpatterns=[
    path("home/",views.index)
]