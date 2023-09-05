from django.urls import path

from helloWorld import views

urlpatterns = [
     path('',views.index),
     path('hi/',views.hello)
]
