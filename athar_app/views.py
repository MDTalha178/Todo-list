from django.shortcuts import render, redirect
from django.http import HttpResponse
from athar_app.models import Loosers
from athar_app.forms import TaskForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def athar(request):
    if request.method == "POST":
        form = TaskForm(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.manage = request.user
            instance = form.save()
        messages.success(request,("New Task Added!"))
        return redirect('athar')
    else:
        all_task = Loosers.objects.filter(manage= request.user)
        paginator = Paginator(all_task,10)
        page = request.GET.get('pg')
        all_task = paginator.get_page(page)

        return render(request, 'athar.html', {'all_task': all_task})


@login_required
def delete_loosers(request, loosers_id):
    task = Loosers.objects.get(pk=loosers_id)
    if task.manage == request.user:
        task.delete()
    else:
       messages.error(request,("Access Restricted, You Are Not Allowed."))

    return redirect('athar')

def edit_loosers(request, loosers_id):
      if request.method == "POST":
          task = Loosers.objects.get(pk=loosers_id)
          form = TaskForm(request.POST or None, instance = task)
          if form.is_valid():
              form.save
       
          messages.success(request,("Task Edited!"))
          return redirect('athar')
      else:
           task_obj = Loosers.objects.get(pk=loosers_id)
           return render(request,'edit.html', {'task_obj': task_obj})

@login_required
def complete_loosers(request, loosers_id):
    task = Loosers.objects.get(pk=loosers_id)
    if task.manage == request.user:
       task.done = True
       task.save()
    else:
        messages.error(request,("Access Redirected, You are not Allow"))

    return redirect('athar')

@login_required
def pending_loosers(request, loosers_id):
    task = Loosers.objects.get(pk=loosers_id)
    task.done = False
    task.save()

    return redirect('athar')

def index(request):
    context = {
        'index_text':"Welcome to index us page.",
    }
    return render(request, 'index.html', context)


def contact(request):
    context = {
        'contact_text':"Welcome to Contact Page.",
        }
    return render(request, 'Contact us.html', context)

def about(request):
    context = {
        'about_text':"Welcome to about us page.",
    }
    return render(request, 'about us.html', context)
