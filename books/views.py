from django.shortcuts import render
from .models import Book,Category,TgAdmin
import datetime
from django.core.mail import send_mail
import telebot
bot = telebot.TeleBot(token="6587656270:AAGEV4MFsrvoypdstkZoEFwjw7fgXBv6S9w")

from django.views import View


def send():
    send_mail("Registratsiya", "Registratsiya bajarildi",
               "navbaxor2016@mail.ru",["ulugbek.husain@gmail.com"])

class Home(View):
    def get(request, *args, **kwargs):
        books = Book.objects.all().order_by("likes")
        categories = Category.objects.all()
        data = {"books":books ,"categories":categories}
        for tgadmin in TgAdmin.objects.all():
            bot.send_message(tgadmin.tg_id , "Saytga kimdur kirdiyooov !")

        return render(request=request, template_name="index.html",context= data )

def category_books(request,pk):
    category = Category.objects.get(id=pk)
    books = Book.objects.filter(category=category)
    categories = Category.objects.all()
    data = {"books":books ,"categories":categories,"category":category}
    return render(request=request, template_name="index.html",context= data )


def book_detail(request,pk):
    book = Book.objects.get(id=pk)
    # book.views += 1
    # book.save()
    data = {"book":book }
    return render(request=request, template_name="book_detail.html",context= data )


def search(request):
    query = request.GET.get("query")

    books = Book.objects.filter(name__icontains=query)
    categories = Category.objects.all()
    data = {"books":books ,"categories":categories}
    return render(request=request, template_name="index.html",context= data )
