# from django import forms
from django.shortcuts import render
from auth import forms
from django.contrib.auth import authenticate,login
from django.http import HttpResponseRedirect
from django.contrib.auth.views import LoginView,LogoutView

# Create your views here.


class Login(LoginView):
    template_name='auth/login.html'
    redirect_authenticated_user=True

class Logout(LogoutView):
    pass
    # template_name='auth/logout.html'


# def auth_login(request):
#     loginForm=forms.LoginFrom()
#     error=None
    
#     if request.method=="POST":
#         loginForm=forms.LoginFrom(request.POST)
#         if loginForm.is_valid():
#             username=loginForm.cleaned_data['username']
#             password=loginForm.cleaned_data['password']
#             user= authenticate(username=username,password=password)
#             if user:
#                 login(request,user)
#                 return HttpResponseRedirect('/')
#             else:
#                  error="invalid"
                
#     context={
#         'form':loginForm,
#         'error': error
#     }
#     return render(request,'auth/login.html',context)
    
    