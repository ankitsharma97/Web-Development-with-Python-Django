from django.urls import path
from check import views

urlpatterns = [
    path('login/',views.Login.as_view(),name='check_login'),
    path('logout/',views.Logout.as_view(),name='check_logout'),
]