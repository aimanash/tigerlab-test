from django.contrib import messages
from django.shortcuts import redirect, render

from .forms import RegisterForm


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile details updated.')
            return redirect("login")
        else:
            messages.success(request, 'There was an error...')
            return render(request, "register/register.html", {"form": form})
    else:
        form = RegisterForm()
        return render(request, "register/register.html", {"form": form})
