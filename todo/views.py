from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader 
from .models import Tasks
def index(request):
    tasks = Tasks.objects.all().values()
    template = loader.get_template('index.html')
    context = {
        'mytasks' : tasks
    }
    return HttpResponse(template.render(context, request))
# Create your views here.
