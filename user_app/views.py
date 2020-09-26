from django.shortcuts import render, redirect
from.forms import CustomRegistraionForm
from django.contrib import messages

def register(request):
    if request.method=="POST":
         register_form = CustomRegistraionForm(request.POST)
         if register_form.is_valid():
             register_form.save()
             messages.success(request,("NEW USER ACCOUNT CREATED, LOGON TO GET SATARTED!"))
             return redirect('register')

    else:
        register_form = CustomRegistraionForm()
    return render(request, 'register.html', {'register_form':register_form})
