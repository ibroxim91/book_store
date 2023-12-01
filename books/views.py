from typing import Any
from django.shortcuts import render
from .models import Book,Category,TgAdmin
import datetime
from django.core.mail import send_mail
import telebot
bot = telebot.TeleBot(token="6587656270:AAGEV4MFsrvoypdstkZoEFwjw7fgXBv6S9w")

from django.views import View
from django.views.generic import TemplateView,ListView ,CreateView
from django.views.generic.detail import DetailView



def send():
    send_mail("Registratsiya", "Registratsiya bajarildi",
               "navbaxor2016@mail.ru",["ulugbek.husain@gmail.com"])

class HomeView(ListView):
    template_name = "new.html"
    model = Book
    context_object_name = 'books'
    queryset = Book.objects.filter(category__id=1)


    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context =  super().get_context_data(**kwargs)
        books = Category.objects.all()
        context["categories"] = books
        return context 


    # def get(self, request, *args, **kwargs):
    #     categories = Category.objects.all()
        # books = Book.objects.all().order_by("likes")
    #     data = {"books":books ,"categories":categories}
    #     # for tgadmin in TgAdmin.objects.all():
    #     #     bot.send_message(tgadmin.tg_id , "Saytga kimdur kirdiyooov !")

    #     return render(request, "index.html" )

def category_books(request,pk):
    category = Category.objects.get(id=pk)
    books = Book.objects.filter(category=category)
    categories = Category.objects.all()
    data = {"books":books ,"categories":categories,"category":category}
    return render(request=request, template_name="index.html",context= data )


class BookDetail(DetailView):
    template_name = "book_detail.html"
    model = Book
    

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context =  super().get_context_data(**kwargs)

        context["categories"] = Category.objects.all()
        return context 



def search(request):
    query = request.GET.get("query")
    books = Book.objects.filter(name__icontains=query)
    categories = Category.objects.all()
    data = {"books":books ,"categories":categories}
    return render(request=request, template_name="index.html",context= data )


class AddBook(CreateView):
    model = Book
    template_name = "add_book.html"
    success_url = "/"
    fields = "__all__"
