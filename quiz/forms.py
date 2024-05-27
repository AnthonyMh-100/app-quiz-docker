from django.contrib.auth.models import User
from django import forms
from .models import Product


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','password']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm',
                'placeholder': 'Username'
            }),
            'password': forms.PasswordInput(attrs={
                'class': 'block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm',
                'placeholder': 'Password'
            }),
        }
        help_texts = {
            'username': None,  
        }

class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','email','password']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm',
                'placeholder': 'Username'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm',
                'placeholder': 'Password'
            }),
            'password': forms.PasswordInput(attrs={
                'class': 'block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm',
                'placeholder': 'Password'
            }),
        }
        help_texts = {
            'username': None,  
        }
        
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name','imagen','description','price','stock']
        
        