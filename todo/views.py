
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader 
from .models import Tasks
from django.urls import reverse



def index(request):
    tasks = Tasks.objects.all().values()
    template = loader.get_template('index.html')
    context = {
        'mytasks' : tasks
    }
    return HttpResponse(template.render(context, request))



def add(request):
  template = loader.get_template('add.html')
  return HttpResponse(template.render({}, request))

def addrecord(request):
  x = request.POST['Description']
  task = Tasks(description=x,)
  task.save()
  return HttpResponseRedirect(reverse('index'))


def delete(request, id):
    task = Tasks.objects.get(id=id)
    task.delete()
    return HttpResponseRedirect(reverse('index'))

def update(request, id):
    mytask = Tasks.objects.get(id=id)
    template = loader.get_template('update.html')
    context = {
    'mytask': mytask,
    }
    return HttpResponse(template.render(context, request))


def updaterecord(request, id):
    description = request.POST['description']
    task = Tasks.objects.get(id=id)
    task.description = description
    task.save()
    return HttpResponseRedirect(reverse('index'))