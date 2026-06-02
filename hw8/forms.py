from django import forms
from .models import Client, Seller, Product, Sale

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'

class SellerForm(forms.ModelForm):
    class Meta:
        model = Seller
        fields = '__all__'

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

class SaleForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = '__all__'
        widgets = {
            'sale_date': forms.DateInput(attrs={'type': 'date'}),
        }
