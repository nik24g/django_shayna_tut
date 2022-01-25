import imp
import re
from django.shortcuts import redirect, render, HttpResponse
from user.models import Contact
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


# Create your views here.
def index(request):
    if request.user.is_authenticated:
        return render(request, 'index.html')
    return redirect("/login")

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST.get('email')
        phone = request.POST['phone']
        message = request.POST.get('message')

        contact = Contact(name=name, email=email, phone=phone, message=message)
        contact.save()
    return render(request, 'contact.html')

def log_in(request):
    if request.method == "POST":
        user_name = request.POST['username']
        pass_word = request.POST['password']

        user = authenticate(username=user_name, password=pass_word)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'login.html')
    return render(request, 'login.html')

def log_out(request):
    logout(request)
    return redirect("/login")

def signup(request):
    return render(request, 'signup.html')


def createuser(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        firstname = request.POST['fname']
        lastname = request.POST['lname']
        password1 = request.POST['password']
        password2 = request.POST['re_password']

        if password1 != password2:
            return HttpResponse("password not matched")

        user = User.objects.create_user(username=username, email=email, password=password1, first_name=firstname, last_name=lastname)
        # user.first_name = firstname
        # user.last_name = lastname
        user.save()
    return redirect("/login")