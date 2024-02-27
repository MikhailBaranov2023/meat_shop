from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect
from django.views.generic import CreateView, UpdateView
from users.models import User, CompanyCard
from users.forms import UserRegisterForm, UserProfileForm, CompanyCardForm
from django.urls import reverse_lazy
from django.forms import inlineformset_factory
from django.contrib.auth.mixins import LoginRequiredMixin


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:login')
    template_name = 'users/register.html'


class ProfileView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        CompanyCardFormset = inlineformset_factory(User, CompanyCard, form=CompanyCardForm, extra=1)
        if self.request.method == 'POST':
            formset = CompanyCardFormset(self.request.POST, instance=self.object)
        else:
            formset = CompanyCardFormset(instance=self.object)

        context_data['formset'] = formset
        return context_data
