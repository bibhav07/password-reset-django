from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import CreateUserForm


@login_required(login_url='/login')
def mainpg(request):
    return render(request, 'main.html')


def loginpg(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Username or password incorrect')
    return render(request, 'login.html')


def logoutUser(request):
    logout(request)
    return redirect('/login/')


def signuppg(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)

        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            messages.success(request, "Accounted was created for " + username)
            return redirect('/login/')

    context = {'form': form}
    return render(request, 'signup.html', context)
