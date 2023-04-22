from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

from ..forms import UserRegistrationForm, UserUpdateForm
from ..models import Note


def user_profile(request, user_pk):
    """ Get user profile for any user on the site. 
    Any user may view any other user's profile. 
    """
    user = User.objects.get(pk=user_pk)
    usernotes = Note.objects.filter(user=user.pk).order_by('-posted_date')
    return render(request, 'lmn/users/user_profile.html', {'user_profile': user, 'notes': usernotes})


@login_required
def my_user_profile(request):
    """ Get the currently logged-in user's profile """
    # TODO - editable version for logged-in user to edit their own profile
    return redirect('user_profile', user_pk=request.user.pk)


@login_required
def edit_user_account_info(request):

    if request.method == "POST":
        user = User.objects.get(pk=request.user.pk)
        form = UserUpdateForm(request.POST, instance=user)

        if form.is_valid():
            form.save()
            messages.success(request, 'Your account information has been successfully updated!')
            return redirect('user_profile', user_pk=request.user.pk)
        else:
            messages.add_message(request, messages.INFO, 'Please check the data you entered')
            # include the invalid form, which will have error messages added to it. 
            # The error messages will be displayed by the template.
            return render(request, 'lmn/users/edit_user_account_info.html', {'form': form})

    form = UserUpdateForm()
    return render(request, 'lmn/users/edit_user_account_info.html', {'form': form})
    

def register(request):
    """ Handles user registration flow

    GET request - show a user registration form.
    POST request - register a new user
    """

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user = authenticate(username=request.POST['username'], password=request.POST['password1'])
            if user:
                login(request, user)
                return redirect('user_profile', user_pk=request.user.pk)
            else:
                messages.add_message(request, messages.ERROR, 'Unable to log in new user')
        else:
            messages.add_message(request, messages.INFO, 'Please check the data you entered')
            # include the invalid form, which will have error messages added to it. 
            # The error messages will be displayed by the template.
            return render(request, 'registration/register.html', {'form': form})

    form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})
