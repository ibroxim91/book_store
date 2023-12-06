from django.urls import path
from .views import *
app_name = "books"
from django.views.generic import TemplateView


urlpatterns = [
    path("" , HomeView.as_view() , name="homeView"
         ),
    path("category/<int:pk>" , category_books),
    path("detail/<int:pk>" , BookDetail.as_view() , name="detail" ),

    path("search" , search),
    path("login" , MyLoginView.as_view() ),

    path("add_book/<int:id>", AddBook.as_view() ,name="add_book" )
]


