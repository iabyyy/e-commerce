from django import forms
from django.contrib.auth.forms import UserCreationForm

from new_app.models import Customer, Login, Seller, Products, CartItem, Payment, Details


class LoginForm(UserCreationForm):
    username = forms.CharField()
    password1 = forms.CharField(label="password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="confirmpassword", widget=forms.PasswordInput)

    class Meta:
        model = Login
        fields = ('username', 'password1', 'password2')

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        exclude = ('User',)

class SellerForm(forms.ModelForm):
    class Meta:
        model = Seller
        exclude = ('User',)

class ProductForm(forms.ModelForm):
    class Meta:
        model = Products
        exclude= ('seller',)

class CartItemForm(forms.ModelForm):
    class Meta:
        model = CartItem
        exclude = ('User','product','date','pay',)


class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        exclude = ('cart','details','item',)


class DetailsForm(forms.ModelForm):
    class Meta:
        model = Details
        exclude = ('cart','customer','status',)
