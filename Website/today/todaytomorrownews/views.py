#from imaplib import _Authenticator
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import SigninForm, SignupForm
import requests
API_KEY='9102aa4297e644dea116668aedc4419e'



# Create your views here.
def index(request):
    category=request.GET.get('category')
    if category is None:
        category='general'
    url=f'https://newsapi.org/v2/top-headlines?country=in&category={category}&pageSize=10&apiKey={API_KEY}'
    response = requests.get(url)
    data=response.json()
    articles = data['articles']
    context={
        'articles': articles
    }
    return render(request, 'today/index.html',context)

def techcategory01(request):
    return render(request, 'today/tech-category-01.html')
def techcategory02(request):
    return render(request, 'today/tech-category-02.html')
def techcategory03(request):
    return render(request, 'today/tech-category-03.html')
def techcontact(request):  
    return render(request, 'today/tech-contact.html')
def techsingle(request):
    return render(request, 'today/tech-single.html')
def signup(request):
    if request.POST:
        form = SignupForm(request.POST)
        
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'Account created successfully.')
            except Exception as e :
                messages.error(request, e)
    else:
        form = SignupForm()

    return render(request, 'today/sign-up.html', {'form': form})



def signin(request):

    
    if request.POST:
        form = SigninForm(request=request, data=request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']  # Correctly access the 'password' field
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('/')
           

    
    else:
        form = SigninForm()

    return render(request, 'today/sign-in.html', {'form': form})

def signout(request):
    logout(request)
    return redirect('index')
