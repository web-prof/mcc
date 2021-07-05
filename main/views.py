from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages


def main(request):
    return render(request, 'main.html', {})


def log_in(request):
    if request.method == 'POST':
        u = request.POST['username']
        p = request.POST['password']
        re = auth.authenticate(username=u, password=p)

        if re is not None:
            auth.login(request, re)
            return redirect('acc:safety_user')
        else:
            messages.warning(request, 'من فضلك تاكد من اسم المستخدم و الرقم السري')
            return redirect('main:log_in')
    return render(request, 'login.html', {})

def log_out(request):
    auth.logout(request)
    return redirect('main:log_in')