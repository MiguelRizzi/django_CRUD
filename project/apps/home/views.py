from django.shortcuts import render, redirect

# Login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login
from .forms import CustomUserCreationForm


# Create your views here.

#def index(request):
#    return render(request, "home/index.html")

# Login basado en funciones
def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request.POST, data=request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get("username")
            contraseña = form.cleaned_data.get("password")
            user = authenticate(username=usuario, password=contraseña)
            if user is not None:
                login(request, user)
                return redirect("home:index")
    else:
        form = AuthenticationForm()
    return render(request, "home/login.html", {"form": form})

# Registro basado en funciones
def register(request):
    if request.method == "POST":
        #form = UserCreationForm(request.POST)
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username") 
            form.save()
            return render(request, "home/index.html", {"mensaje": "Usuario creado"})
    else:
        #form = UserCreationForm()
        form = CustomUserCreationForm()
    return render(request, "home/register.html", {"form": form})