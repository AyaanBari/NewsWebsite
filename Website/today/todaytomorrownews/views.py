from imaplib import _Authenticator
import json
import pickle
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from . models import News
from .forms import SigninForm, SignupForm , PostNewsForm
import requests
from rest_framework import viewsets
from rest_framework.decorators import api_view
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt
import pickle
import datetime
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

def postnews(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PostNewsForm(request.POST, request.FILES)
            if form.is_valid():
                # Process form data for saving news post
                title = form.cleaned_data['title']
                description = form.cleaned_data['description']
                image = form.cleaned_data['image']

                try:
                    with open('news_pickle.pickle', 'rb') as f:
                        nb1 = pickle.load(f)
                        vectorizer = pickle.load(f)

                    # Transform the submitted title text using the vectorizer
                    X_new_transformed = vectorizer.transform([title])

                    # Make prediction using the loaded nb1 model
                    predicted_category = nb1.predict(X_new_transformed)[0]  # Get predicted category based on highest probability
                    if predicted_category == 0:
                        category = 'Business'
                    elif predicted_category == 1:
                        category = 'Entertainment'
                    elif predicted_category == 2:
                        category = 'Health'
                    elif predicted_category == 3:
                        category = 'Politics'
                    else:
                        category = 'Sports'

                except Exception as e:
                    messages.error(request, f'Error making prediction: {e}')
                    return render(request, 'today/postnews.html', {'form': form})

                # Create the news post with the predicted category
                post = News(title=title, description=description, image=image,
                            author=request.user.get_full_name(), date=datetime.date.today(),
                            time=datetime.datetime.now().time(), category=category ,catid=predicted_category+1)
                post.save()

                messages.success(request, 'Post created successfully.')
                return redirect('usernews/0')  # Redirect after successful POST
            else:
                messages.error(request, form.errors)  # Display form errors on the template
                return render(request, 'today/postnews.html', {'form': form})
        else:
            # Render the form for GET requests
            return render(request, 'today/postnews.html', {'form': PostNewsForm()})
    else:
        return redirect('signin')


def usernews(request, catid=None): 
    if request.method == 'GET':
        if catid == 0:  # Check if 'catid' is 0
            cat='All'
        elif catid == 1:
            cat='Business'
        elif catid == 2:
            cat='Entertainment'
        elif catid == 3:
            cat='Health'
        elif catid == 4:
            cat='Politics'
        elif catid == 5:
            cat='Sports'
        else:
            messages.error(request, 'Invalid category selected.')
            return redirect('index')
        try:
            # Filter news based on catid (assuming 'catid' field exists)
            if catid != 0:  # Check if 'catid' is provided
                news = News.objects.filter(catid=catid)
            else:
                news = News.objects.all()  # Show all news if no category selected

            context = {'news': news, 'cat': cat}  # No need for 'category_list' since you're not displaying categories separately
            if not news:
                messages.info(request, 'No news posts found in this category.')
            return render(request, 'today/usernews.html', context)
        except Exception as e:
            messages.error(request, f'An error occurred: {e}')
            return redirect('index')
    else:
        messages.error(request, 'Invalid request method.')
        return redirect('index')

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

#here we will create a function to get the news from the API and display it on the index page and also analyze the news category using the headline which we will pass to the NLP model we created earlier.

