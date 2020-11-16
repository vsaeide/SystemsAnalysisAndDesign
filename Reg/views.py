from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from Reg.forms import SignUpForm



@login_required
def home(request):
    return render(request, 'home.html')


def signup(request):
    print("hello saeede1")

    if request.method == 'POST':

        print("hello saeede2")
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            temp =form.cleaned_data.get('type')

            if temp=="vip":
                user.profile.type=temp
            else:
                user.profile.type=temp

            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()

    return render(request, 'signup.html', {'form': form})
