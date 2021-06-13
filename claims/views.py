from django.shortcuts import render
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import admin
from django.contrib.auth.models import User


from django.views.generic import ListView, DetailView 
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from django.urls import reverse_lazy


from .models import Claim, STATUS_CHOICES 
from .forms import ClaimForm

@admin.action(description='Mark as accepted')
class ClaimList(LoginRequiredMixin, ListView): 
    model = Claim
    def get_user_profile(request, username):
        user = User.objects.get(username=username)
        return render(request, 'claims/claim_list.html', {"user":user})


class ClaimDetail(LoginRequiredMixin, DetailView): 
    model = Claim


class ClaimCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView): 
    model = Claim
    form_class = ClaimForm
    success_url = reverse_lazy('claim_list')
    success_message = "Claim successfully created!"


class ClaimUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):   
    # if field_value != 'Accepted':   
        model = Claim
        form_class = ClaimForm
        success_url = reverse_lazy('claim_list')
        success_message = "Claim successfully updated!"
        def get_user_profile(request, username):
            user = User.objects.get(username=username)
            return render(request, 'claims/claim_form.html', {"user":user})



class ClaimDelete(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Claim
    success_url = reverse_lazy('claim_list')
    success_message = "Claim successfully deleted!"


class ClaimProfile(LoginRequiredMixin, ListView): 
    model = Claim
    def get_user_profile(request, username):
        user = User.objects.get(username=username)
        return render(request, 'claims/claim_list.html', {"user":user})

def get_user_profile(request, username):
    user = User.objects.get(username=username)
    return render(request, 'claims/profile.html', {"user":user})
