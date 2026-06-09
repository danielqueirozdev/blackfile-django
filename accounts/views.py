from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import Http404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .forms.login_form import LoginForm
from .forms.register_form import RegisterForm


def register_view(request):
    register_form_data = request.session.get('register_form_data', None)
    form_errors = request.session.pop('form_errors', None)

    form = RegisterForm(register_form_data)

    if form_errors:
        form._errors = form_errors

    return render(request, 'accounts/pages/register.html', {
        'form': form,
    })


def register_create_view(request):
    if request.method != 'POST':
        raise Http404()

    form = RegisterForm(request.POST)

    if form.is_valid():
        user = form.save(commit=False)
        user.set_password(user.password)
        user.save()

        request.session.pop('register_form_data', None)

        messages.success(request, 'Account created successfully. Please log in.')
        return redirect(reverse('accounts:login'))

    request.session['register_form_data'] = request.POST
    request.session['form_errors'] = form.errors

    return redirect('accounts:register')


def login_view(request):
    # If user is already logged in, send to notes
    if request.user.is_authenticated:
        return redirect('notes:home')

    form = LoginForm()
    return render(request, 'accounts/pages/login.html', {
        'form': form,
        'form_action': reverse('accounts:login_create'),
    })


def login_create_view(request):
    if request.method != 'POST':
        raise Http404()

    form = LoginForm(request.POST)
    login_url = reverse('accounts:login')

    if form.is_valid():
        authenticated_user = authenticate(
            username=form.cleaned_data.get('username', ''),
            password=form.cleaned_data.get('password', ''),
        )

        if authenticated_user is not None:
            login(request, authenticated_user)
            messages.success(request, 'Welcome back.')
            return redirect('notes:home')

        messages.error(request, 'Invalid username or password.')
        return redirect(login_url)

    messages.error(request, 'Invalid username or password.')
    return redirect(login_url)


@login_required(login_url='accounts:login')
def logout_view(request):
    if request.method != 'POST':
        return redirect('accounts:login')

    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('accounts:login')
