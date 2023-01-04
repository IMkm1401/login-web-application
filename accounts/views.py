from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login
def Loginv(request):
    if request.method == "POST":
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            userinf = form.get_user()
            login(request,userinf)
            return redirect("/")
    form = AuthenticationForm()
    return render(request,"login.html",{"formu":form})
