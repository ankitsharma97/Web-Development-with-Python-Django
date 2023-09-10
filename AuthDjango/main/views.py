from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# from main 
# Create your views here.
login_required(login_url='/auth/login') 
def index(request):
    return render(request,'main/index.html')


def sshh(request):
    return HttpResponse("authenticated view")