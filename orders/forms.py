from django import forms
from .models import Order, OrderCountry


class OrderCreateForm(forms.ModelForm):
    first_name = forms.CharField(label="Имя", widget=forms.TextInput(
                                   attrs={'class': 'billing-info', 'placeholder': 'Ваше имя'}))
    phone_number = forms.CharField(label="Номер телефона", widget=forms.TextInput(
                                   attrs={'class': 'billing-info', 'placeholder': 'Ваше номер'}))
    country = forms.ModelChoiceField(label="Страна", queryset=OrderCountry.objects.all(),
                                     widget=forms.Select(attrs={'class': 'billing-info'}))
    email = forms.EmailField(label="Email", required=False, widget=forms.EmailInput(
                                   attrs={'class': 'billing-info', 'placeholder': 'Ваше email'}))
    address = forms.CharField(label="Адрес", widget=forms.TextInput(
        attrs={'class': 'billing-info', 'placeholder': 'Ваше адрес'}))
    note = forms.CharField(label="Комментарий", widget=forms.Textarea(
        attrs={'class': 'form-control', 'placeholder': 'Оставьте комментарий'}))

    class Meta:
        model = Order
        fields = ['first_name', 'phone_number', 'email', 'country', 'address', 'note']
