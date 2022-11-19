from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import login, authenticate
from .forms import UserRegisterationForm, UserLoginForm
from django.contrib import messages

# Create your views here.


class UserRegisterView(View):
    def get(self, request):
        form = UserRegisterationForm()
        return render(request, 'account/register.html', {'form': form})

    def post(self, request):
        form = UserRegisterationForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            User.objects.create_user(cd['username'], cd['email'], cd['password1'])
            messages.success(request, 'You registered successfully', 'success')
            return redirect('home:home')
        return render(request, 'account/register.html', {'form': form})


class UserLoginView(View):
    form_class = UserLoginForm
    template_name = 'account/login.html'

    def get(self, request):
        form = self.form_class
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user is not None:
                login(request, user)
                messages.success(request, 'You have logged in successfully')
                return redirect('home:home')
            messages.error(request, 'Username or password are not correct', 'danger')
            return render(request, self.template_name, {'form': form})