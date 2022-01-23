from django.shortcuts import redirect, render
from user.models import Contact
from django.contrib.auth import authenticate, login, logout


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