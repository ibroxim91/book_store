from django.shortcuts import render
from .models import Book,Category
# Create your views here.


def home(request):
    books = Book.objects.all()
    categories = Category.objects.all()
    data = {"books":books ,"categories":categories}
    return render(request=request, template_name="index.html",context= data )

def category_books(request,pk):
    category = Category.objects.get(id=pk)
    books = Book.objects.filter(category=category)
    categories = Category.objects.all()
    data = {"books":books ,"categories":categories,"category":category}
    return render(request=request, template_name="index.html",context= data )


def book_detail(request,pk):
    book = Book.objects.get(id=pk)
    data = {"book":book }
    return render(request=request, template_name="book_detail.html",context= data )


def search(request):
    query = request.GET.get("query")

    books = Book.objects.filter(name__icontains=query)
    categories = Category.objects.all()
    data = {"books":books ,"categories":categories}
    return render(request=request, template_name="index.html",context= data )
