

from django import forms

class inputform1(forms.Form):
    n1 = forms.IntegerField(
        min_value=1,
        max_value=10,
        label="Enter a number ",
        widget=forms.NumberInput(attrs={
            'style': 'width: 300px; height: 40px; font-size: 20px;',
            'placeholder': 'Enter a number'
        })
    )

