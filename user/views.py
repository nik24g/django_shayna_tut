from django.shortcuts import redirect, render, HttpResponse
from user.models import Contact
from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.models import User
from user.models import Student, User
from django.contrib import messages


# Create your views here.
def index(request):
    if request.user.is_authenticated:
        students = Student.objects.all()
        context = {"students": students}
        return render(request, 'index.html', context)
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

def create_student(request):
    if request.method == "POST":
        name = request.POST['name']
        age = request.POST['age']
        branch = request.POST['branch']
        address = request.POST['address']
        image = request.FILES.get('image')

        # Student 
        student = Student(name=name, age=age, branch=branch, address=address, image=image)
        student.save()
        messages.success(request, 'Student Added Successfully')
    return render(request, 'create_student.html')

def change_password(request):
    if request.method == "POST":
        oldPassword = request.POST.get("oldpassword")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        email = request.user.email
        user = authenticate(username=email, password=oldPassword)
        if user:
            if password1 == password2:
                user.set_password(password1)
                user.save()
                messages.success(request, "Password Changed")
            else:
                messages.warning(request, "Password not matched")
        else:
            messages.warning(request, "Old password is wrong")
    return render(request, "change-password.html")


def others(request):
    if request.method == "POST":
        name = request.POST['name']
        users = User.objects.filter(first_name__icontains = name)
        print(users)
        payload = {"queryusers": users}
        return render(request, "others.html", payload)

    return render(request, "others.html")