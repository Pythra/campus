from django.forms import Textarea, TextInput, NumberInput, FileInput
from .models import Product, Shop, Service, Review, Request, User, House
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class HouseForm(forms.ModelForm):
    class Meta:
        model = House
        fields = ('address', 'price', 'typ', 'pic1', 'pic2', 'pic3', 'pic4')

        widgets = {
            'address': TextInput(attrs={'class': 'form-control'}),
            'typ': TextInput(attrs={'class': 'form-control'}),
            'school': TextInput(attrs={'class': 'form-control'}),
            'price': NumberInput(attrs={'class': 'form-control'}), 
        }



class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'price', 'description', 'condition', 'pic1', 'pic2', 'pic3', 'pic4', )

        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),
            'price': NumberInput(attrs={'class': 'form-control'}), 
            'description': TextInput(attrs={'class': 'form-control', 'placeholder': 'describe the product'}),
        }


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ('name', 'charge', 'description', 'picture', 'pic1', 'pic2', 'pic3', 'pic4')

        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),
            'charge': NumberInput(attrs={'class': 'form-control',}), 
            'description': TextInput(attrs={'class': 'form-control', 'placeholder': 'describe the product'}),
        }


class ShopForm(forms.ModelForm):

    class Meta:
        model = Shop
        fields = ('name', 'school', 'logo')
        widgets = {
            'name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Name of your buisness'}),
            'logo': FileInput(),
        }


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('title', 'content', 'photo', 'photo1', 'photo2', 'photo3', 'photo4',)
        widgets = {
            'title': TextInput(attrs={'class': 'form-control'}),
            'content': Textarea(attrs={'class': 'form-control'}),
            'photo1': FileInput(),
            'photo2': FileInput(),
            'photo3': FileInput(),
            'photo4': FileInput(),
                   }


class RequestForm(forms.ModelForm):

    class Meta:
        model = Request
        fields = ('title', 'description', 'ref_pic', 'min_price', 'max_price')
        widgets = {
            'title': TextInput(attrs={'class': 'form-control', 'placeholder': 'What do you need?'}),
            'description': TextInput(attrs={'class': 'form-control', 'placeholder': "Describe what you're looking for"}),
            'min_price': NumberInput(attrs={'class': 'form-control'}),
            'max_price': NumberInput(attrs={'class': 'form-control'}),
            'ref_pic': FileInput(),
        }



class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

