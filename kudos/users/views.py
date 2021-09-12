from django.contrib.auth import authenticate,login, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ExtendedUserCreationForm, UserProfileForm
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib import messages


@csrf_exempt
def register(request):
    if request.method == "POST":
        form = ExtendedUserCreationForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        if form.is_valid() and profile_form.is_valid():
            user = form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.organization_name = profile_form.cleaned_data.get("organization_name").lower()
            profile.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            username = User.objects.get(username=form.cleaned_data.get("username"))
            messages.success(request, 'Account created for username %s' % username)
            #return  redirect('users/register.html')

    else:
        form = ExtendedUserCreationForm()
        profile_form = UserProfileForm()

    context = {'form': form, 'profile_form': profile_form}
    return render(request, 'users/register.html', context)


@csrf_exempt
def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = User.objects.get(username=form.cleaned_data.get("username"))
            user = form.get_user()
            login(request, user)
            messages.success(request, "Hello {}, you are logged in!".format(username))
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password')
            return redirect('login')
    else:
        form = AuthenticationForm()

    context = {'form': form}
    return render(request, 'users/login.html', context)


def user_logout(request):
    logout(request)
    messages.success(request, "You have been logged out")
    return redirect('home')