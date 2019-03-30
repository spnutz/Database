from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def index(request):
    header_str = 'Music School'
    context = {'var1': header_str}
    return render(request,'index.html', context)
