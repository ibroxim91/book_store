from typing import Any
from django.shortcuts import render
from .models import Book,Category,TgAdmin
import datetime
from django.core.mail import send_mail
import telebot
bot = telebot.TeleBot(token="")

from django.views import View
from django.views.generic import TemplateView,ListView ,CreateView
from django.views.generic.detail import DetailView
from .forms import BookForm
from django.contrib import messages
from django.contrib.auth.views import LoginView,LogoutView

def send():
    send_mail("Registratsiya", "Registratsiya bajarildi",
               "navbaxor2016@mail.ru",["ulugbek.husain@gmail.com"])

class HomeView(ListView):
    template_name = "index.html"
    model = Book
    context_object_name = 'books'
    # queryset = Book.objects.filter(category__id=1)


    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        print( self.request.COOKIES.get("username") )
        context =  super().get_context_data(**kwargs)
        categories = Category.objects.all()
        context["categories"] = categories
        context["trend_books"] = 0
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
    data = {"kitoblar":books ,"categories":categories,"category":category}
    response =  render(request=request, template_name="index.html",context= data )
    print( request.COOKIES.get("username") )
    response.set_cookie("username" , "Alex")
    return response


class BookDetail(DetailView):
    template_name = "shop-details.html"
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


class AddBook(View):
    def get(self ,request):
        form = BookForm()
        context = {"form":form}
        return render(request , "add_book.html", context=context)
    
    def post(self ,request):
        form = BookForm(request.POST, request.FILES)
        obj = None
        if form.is_valid():
            name = form.cleaned_data['name']
            if len(name) < 4:
                messages.add_message(request, messages.WARNING, "Kitob nomi 4 ta belgidan kam")
            obj = form.save()
        context = {"obj":obj,"form":form}
        return render(request , "add_book.html", context=context)


class MyLoginView(LoginView):
    template_name = "login.html"
    success_url = "/"

   