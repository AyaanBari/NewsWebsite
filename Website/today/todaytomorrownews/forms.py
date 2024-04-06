
from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from . models import CustomUser

class SignupForm(UserCreationForm):
    username = forms.CharField(
        label=('Username'),
        widget=forms.TextInput(attrs={'placeholder': 'Enter Username', 'class': 'form-control border-primary'}))
    first_name = forms.CharField(
        label=('First Name'),
        widget=forms.TextInput(attrs={'placeholder': 'Enter First Name', 'class': 'form-control border-primary'}))
    last_name = forms.CharField(
        label=('Last Name'),
        widget=forms.TextInput(attrs={'placeholder': 'Enter Last Name', 'class': 'form-control border-primary'}))
    email = forms.EmailField(
        label=('Email'),
        widget=forms.EmailInput(attrs={'placeholder': 'Enter Email', 'class': 'form-control border-primary'}))
    mobile = forms.CharField(
        label=('Mobile Number'),
        widget=forms.TextInput(attrs={'placeholder': 'Enter Mobile Number', 'class': 'form-control border-primary'}))
    password1 = forms.CharField(
        label=('Password'),
        widget=forms.PasswordInput(attrs={'placeholder': 'Enter Password', 'class': 'form-control border-primary'}))
    password2 = forms.CharField(
        label=('Confirm Password'),
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password', 'class': 'form-control border-primary'}))
    class Meta:
         model = CustomUser
         fields = ('username','first_name','last_name', 'email','mobile')



class SigninForm(AuthenticationForm):
    username = forms.CharField(max_length=255, label='Username', widget=forms.TextInput(attrs={'placeholder': 'Enter Username', 'class': 'form-control border-primary'}))
    password = forms.CharField(max_length=128, label='Password', widget=forms.PasswordInput(attrs={'placeholder': 'Enter Password', 'class': 'form-control border-primary'}))
    

class PostNewsForm(forms.Form):
    title = forms.CharField(
        label=('Title'),
        widget=forms.TextInput(attrs={'placeholder': 'Enter Title', 'class': 'form-control border-primary'}))
    description = forms.CharField(
        label=('Description'),
        widget=forms.Textarea(attrs={'placeholder': 'Enter Description', 'class': 'form-control border-primary'}))
    image = forms.ImageField(
        label=('Image'),
        widget=forms.FileInput(attrs={'placeholder': 'Choose Image', 'class': 'form-control border-primary', 'accept': 'image/*', 'capture': 'camera'}))
