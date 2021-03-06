from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .form import UserRegisterFrom

def register(request):

    if request.method == 'POST':
        form = UserRegisterFrom(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are new able to log in')
            return redirect('login')
    else:
        form = UserRegisterFrom()
    context = {
        'form': form,
        'title': 'Register',
    }
    return render(request, 'users/register.html', context)

@login_required()
def profile(request):
    return render(request,'users/profile.html')