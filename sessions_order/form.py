from django import forms


class AddToCartForm(forms.Form):
    count = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'search_box cart_quantity_input', 'value': 1}))

    def clean_count(self):
        count = self.cleaned_data['count']
        if count <= 0:
            raise forms.ValidationError('تعداد بیشتر از 0 باشد')
        else:
            return count
