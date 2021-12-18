from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from .models import Place, Team


def demo(request):
    obj = Place.objects.all()
    ob = Team.objects.all()

    return render(request, "index.html", {'result': obj, 'res': ob})

# def addition(request):
#   x=int(request.GET['num1'])
#  y=int(request.GET['num2'])
# sum=x+y
# return render(request,"result.html",{'result':sum})
