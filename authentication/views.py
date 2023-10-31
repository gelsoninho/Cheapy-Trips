from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
# Create your views here.
def home(request):
    return render(request, "base.html")

def login_view(request):
    login(request)
    return redirect("/")

def logout_view(request):
    logout(request)
    return redirect("/")

