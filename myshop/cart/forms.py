from django import forms
from django.utils.translation import gettext_lazy as _

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]

class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(
        label=_('Quantity'),
        choices=PRODUCT_QUANTITY_CHOICES,
        coerce=int)

    update = forms.BooleanField(
        label=_('Update'),
        required=False,
        initial=False,
        widget=forms.HiddenInput)
