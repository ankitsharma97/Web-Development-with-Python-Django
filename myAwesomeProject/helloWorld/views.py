from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    developedBy="ankit sharma"
    mentors=[
        "hariom",
        "aqib",
        "rishabh",
    ]
    context={
        "developer":developedBy,
        "mentors":mentors
        
    }
    
    response = render(request,'helloWorld/index.html',context)
    # response=HttpResponse("hello word")
    return response

def hello(request):
    return render(request,'helloWorld/hi.html')