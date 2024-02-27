from django import forms
from product.models import Date, HalfCarcasses, ByProduct


class FormStileMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class DateForm(forms.ModelForm, FormStileMixin):
    class Meta:
        model = Date
        fields = "__all__"


class HalfCarcassesForm(FormStileMixin, forms.ModelForm):
    class Meta:
        model = HalfCarcasses
        fields = "__all__"


class ByProductForm(FormStileMixin, forms.ModelForm):
    class Meta:
        model = ByProduct
        fields = '__all__'
