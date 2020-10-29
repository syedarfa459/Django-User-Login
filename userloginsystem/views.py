from django.contrib.auth import authenticate
from django.contrib import messages
from django.shortcuts import render

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# Create your views here.

def user_login(request):
    form = AuthenticationForm(request=request, data=request.POST)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password )
        if user is not None:
            messages.info(request, f"You are now logged in as {username}")
            return render(request, 'success.html')
        # else:
        #     messages.error(request, "Invalid username/ password")
        #     return render('index.html')
    else:
        pass
        # messages.error(request, "Invalid username/ password")

    form= AuthenticationForm()

    return render(request=request, template_name='user_login.html', context={'form': form})


def index(request):
    return render(request, 'index.html')
