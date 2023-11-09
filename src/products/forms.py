from django import forms

from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]

class RawProductForm(forms.Form):
    title = forms.CharField()                
    description = forms.CharField(required=True, widget=forms.Textarea(attrs={
        "class":"text", "id":"desc", "rows":20, "cols":20,
    }))  
    price = forms.CharField()
    checkbox = forms.BooleanField()