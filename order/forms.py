from django import forms
from order.models import Order


class FormStileMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class OrderForm(FormStileMixin, forms.ModelForm):
    class Meta:
        model = Order
        exclude = ('user', 'status',)
