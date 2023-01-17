from django.shortcuts import render,redirect
from django.contrib import messages
from users.forms import registerform
from django.contrib.auth.decorators import login_required
# Create your views here.


def register(request):
    if request.method == 'POST':
        form = registerform(request.POST)
        if form.is_valid():
            form.save()
            username =form.cleaned_data.get('username')
            messages.success(request,f"welcome {username}, Your account is created")
            return redirect("login")
    else:
        form = registerform()
    return render(request,'register.html',{'form':form})

@login_required
def profilepage(request):
    return render(request,'profile.html')