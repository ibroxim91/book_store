from django.urls import path
from .views import HomeView ,category_books,BookDetail,search,AddBook
app_name = "books"
from django.views.generic import TemplateView


urlpatterns = [
    path("" , HomeView.as_view() , name="homeView"),
    path("category/<int:pk>" , category_books),
    path("detail/<int:pk>" , BookDetail.as_view() ),

    path("search" , search),

    path("add_book", AddBook.as_view()  )
]


