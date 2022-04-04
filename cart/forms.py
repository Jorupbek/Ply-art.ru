from django import forms


class CartAddProductForm(forms.Form):
    quantity = forms.IntegerField(label='', min_value=1, widget=forms.NumberInput(attrs={'value': 1, 'class': 'cart-plus-minus-box'}))
    override = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
    select = forms.CharField(label='')

    class Meta:
        fields = ['quantity', 'override', 'select']
