
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