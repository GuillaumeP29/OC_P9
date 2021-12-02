from . import forms
from LITReview.settings import LOGIN_REDIRECT_URL
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views.generic import View
# from django.http import HttpResponse


# Create your views here.
def logout_user(request):
    logout(request)
    return redirect('login')


class LoginPage(View):
    form_class = forms.LoginForm
    template_name = "users/login.html"

    def get(self, request):
        form = self.form_class()
        message = ''
        return render(
            request,
            self.template_name,
            context={'form': form, 'message': message}
        )

    def post(self, request):
        form = forms.LoginForm(request.POST)
        message = ''
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )
            if user is not None:
                login(request, user)
                return redirect('feed')
        message = 'Identifiants invalides.'
        return render(
            request,
            self.template_name,
            context={'form': form, 'message': message}
        )


def login_page(request):
    form = forms.LoginForm()
    message = ''
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
                )
            if user is not None:
                login(request, user)
                return redirect('feed')
            else:
                message = 'Identifiants invalides.'
    return render(request, "users/login.html", context={'form': form, 'message': message})


def sign_up_page(request):
    form = forms.SignUpForm()
    if request.method == 'POST':
        form = forms.SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(LOGIN_REDIRECT_URL)
    return render(request, "users/sign_up.html", context={'form': form})
