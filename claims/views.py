from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .forms import ClaimForm
from .models import Claim


class ClaimList(LoginRequiredMixin, ListView):
    model = Claim

    # to ensure current user only able to view their details
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = context['object_list'].filter(user=self.request.user)
        return context


class ClaimDetail(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Claim

    # prohibit user from viewing other user's profile
    def test_func(self):
        current_user = self.request.user
        claim_user = get_object_or_404(Claim, pk=self.kwargs['pk']).user
        return current_user == claim_user


class ClaimCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Claim
    form_class = ClaimForm
    context_object_name = 'object'
    success_url = reverse_lazy('claim_list')
    success_message = "Claim successfully created!"

    # to make sure the uploaded details are current user details
    def form_valid(self, form: ClaimForm):
        form.instance.user = self.request.user
        return super(ClaimCreate, self).form_valid(form)

    # pre-fill user details that have been recorded during registration
    def get_initial(self, *args, **kwargs):
        user_id = self.request.user.pk
        initial = super().get_initial(**kwargs)
        initial['name'] = get_object_or_404(
                          User, pk=user_id).first_name + ' ' + get_object_or_404(
                          User, pk=user_id).last_name
        initial['email'] = get_object_or_404(User, pk=user_id).email
        return initial


class ClaimUpdate(LoginRequiredMixin, UserPassesTestMixin,
                  SuccessMessageMixin, UpdateView):
    model = Claim
    form_class = ClaimForm
    success_url = reverse_lazy('claim_list')
    success_message = "Claim successfully updated!"

    # prohibit user from updating other user's profile
    # user with status 'Accepted' not able to edit their profile
    def test_func(self):
        current_user = self.request.user
        claim_user = get_object_or_404(Claim, pk=self.kwargs['pk']).user
        status_user = get_object_or_404(Claim, pk=self.kwargs['pk']).status
        return current_user == claim_user and status_user != 'Accepted'


class ClaimDelete(LoginRequiredMixin, UserPassesTestMixin,
                  SuccessMessageMixin, DeleteView):
    model = Claim
    success_url = reverse_lazy('claim_list')
    success_message = "Claim successfully deleted!"

    # prohibit user from deleting other user's profile
    # user with status 'Accepted' not able to delete their details
    def test_func(self):
        current_user = self.request.user
        claim_user = get_object_or_404(Claim, pk=self.kwargs['pk']).user
        status_user = get_object_or_404(Claim, pk=self.kwargs['pk']).status
        return current_user == claim_user and status_user != 'Accepted'
