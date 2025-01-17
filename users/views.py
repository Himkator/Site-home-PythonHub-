from django.contrib import auth, messages
from django.http import HttpResponseRedirect
from django.http.response import HttpResponseBase
from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from users.forms import *

# Create your views here.
def login(request):
    if request.method=='POST':
        form=UserLoginForm(data=request.POST)
        if form.is_valid():
            username=request.POST['username']
            password=request.POST['password']
            user=auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                messages.success(request, f"{username}, Вы успешно вошли")
                redirect_page=request.POST.get('next', None)
                if redirect_page and redirect_page!=reverse('user:logout'):
                    return HttpResponseRedirect(request.POST.get('next'))
                return HttpResponseRedirect(reverse('main:main'))
    else:
        form=UserLoginForm()
    context={
        'title':'Home-Авторизация',
        'form':form,
    }
    return render(request, 'users/login.html', context)


def registration(request):
    if request.method=='POST':
        form=UserRegistrationForm(data=request.POST)
        if form.is_valid():
            user=form.save()
            auth.login(request, user)
            messages.success(request, f"{user.username}, Вы успешно вошли")
            return HttpResponseRedirect(reverse('main:main'))
    else:
        form=UserRegistrationForm()


    context={
        'title':'Home-Региятрация',
        'form':form,
    }
    return render(request, 'users/registration.html', context)

@login_required
def profile(request):
    if request.method=='POST':
        form=ProfileForm(data=request.POST, instance=request.user, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Профайл успешно изменен")
            return HttpResponseRedirect(reverse('user:profile'))
    else:
        form=ProfileForm(instance=request.user)

    context={
        'title':'Home-Кабинет',
        'form':form,
    }
    return render(request, 'users/profile.html', context)

@login_required
def logout(request):
    auth.logout(request)
    messages.success(request, f"{request.user.username}, Вы успешно вышли")
    return redirect(reverse('main:main'))

@login_required
def user_cart(request):
    context={
        'title':'Home-Корзина',
    }
    return render(request, 'users/user_cart.html', context)