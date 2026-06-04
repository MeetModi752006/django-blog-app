from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegisterForm, ProfileUpdateForm, UserUpdateForm


def register(request):
    """
    Handles new user registration.
    On POST: validates the form, saves the user, logs them in, and redirects.
    On GET: displays the empty registration form.
    """
    if request.user.is_authenticated:
        return redirect('blog:home')  # already logged-in users go home

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # log the user in immediately after registration
            messages.success(request, f'Welcome, {user.username}! Your account has been created.')
            return redirect('blog:home')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = RegisterForm()

    return render(request, 'registration/register.html', {'form': form})


@login_required
def profile(request):
    """
    Displays and allows editing of the logged-in user's profile.
    Uses two forms simultaneously: one for User fields, one for UserProfile fields.
    """
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile has been updated!')
            return redirect('accounts:profile')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'user_form': user_form,
        'profile_form': profile_form,
    }
    return render(request, 'accounts/profile.html', context)
