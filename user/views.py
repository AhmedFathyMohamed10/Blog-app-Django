from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import render, redirect


from django.contrib.auth.models import User

try:
    from blog import views
except ImportError:
    pass

def index(request):
    return redirect(views.index)

def register(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        firstname = request.POST.get('first_name')
        lastname = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('confirm')

        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username Taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email Taken")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password, first_name=firstname, last_name=lastname)
                user.save()
                return redirect('index')
        else:
            messages.info(request, "Password not matching")
            return redirect('register')
    else:
        return render(request, "logging_up/register.html")
    
    
def login_user(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
    
        user = authenticate(request, username=username, password=password)
    
        if user is not None: # if user exists
            login(request, user) # log in user
            return redirect('index')
        else:
            messages.info(request, "Username or Password is incorrect")
            return redirect('login')
    else:
        return render(request, "logging_up/login.html")


def logout_user(request):
    logout(request)
    return redirect('login')