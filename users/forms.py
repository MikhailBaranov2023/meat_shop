from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from users.models import User, CompanyCard
from django import forms
from django.forms import ModelForm


class FormStileMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class UserRegisterForm(FormStileMixin, UserCreationForm):
    class Meta:
        model = User
        fields = ('phone', 'password1', 'password2')


class UserProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'phone', 'city')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['password'].widget = forms.HiddenInput()


class CompanyCardForm(ModelForm, FormStileMixin):
    class Meta:
        model = CompanyCard
        exclude = ('user',)
