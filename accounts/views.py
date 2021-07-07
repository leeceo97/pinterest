from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def hello_world(request):
    if request.method == "POST":
        return render(request, 'accounts/helloworld.html', context={'text':'POST METHOD!'})
    else:
        return render(request, 'accounts/helloworld.html', context={'text':'get METHOD!'})