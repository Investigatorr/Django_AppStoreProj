from django import forms


PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 26)] # 사용자가 선택가능한 숫자


class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int)
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)