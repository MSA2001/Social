from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View
from .forms import UserRegisterationForm
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