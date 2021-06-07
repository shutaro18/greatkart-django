from django.shortcuts import render
from .forms import RegistraionForm


def register(request):
    form = RegistraionForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/register.html', context)


def login(request):
    return render(request, 'accounts/login.html')


def logout(request):
    return 