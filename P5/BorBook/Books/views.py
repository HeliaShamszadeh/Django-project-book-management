from django import template
from django.template import loader
from django.http import Http404, response
from .models import Book
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Book


def index(request):
    if request.method == "GET":
        return render(request, "index.html")

def booklist(request):
        books = Book.objects.all()
        context = {'result':books}
        return render(request,'booklist.html', context)

def form(request):
    pass

def search_book(request):
    """ search function  """
    if request.method == "POST":
        query_name = request.POST.get('name', None)
        if query_name:
            results = Book.objects.filter(name__contains=query_name)
            return render(request, 'search.html', {"results":results})

    return render(request, 'search.html')

def addbook(request):
    if request.method == "GET":
        return render(request, 'addbook.html')
    elif request.method == "POST":
        data=request.POST
        obj=Book.objects.create(name=data['bname'], Author=data['Aname'], Owner=data['Oname'], city=data['city'] , email=data['contactinfo'], Description=data['description'], borrowed=False)
        obj.save()
        return render (request, 'success.html')

def changeborrow(request, id):
    results =Book.objects.get(id=id)
    if results.borrowed == True:
        results.borrowed=False
    else:
        results.borrowed= True
    results.save()
    return redirect('booklist')

def delete(request, id):
    results =Book.objects.get(id=id)
    results.delete()
    return redirect('booklist')
    
def changeborrow1(request, id):
    results =Book.objects.get(id=id)
    if results.borrowed == True:
        results.borrowed=False
    else:
        results.borrowed= True
    results.save()
    return redirect('search')

def delete1(request, id):
    results =Book.objects.get(id=id)
    results.delete()
    return redirect('search')










# Create your views here.
