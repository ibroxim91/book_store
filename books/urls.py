from django.urls import path
from .views import home ,category_books,book_detail,search
app_name = "books"


urlpatterns = [
    path("" , home),
    path("category/<int:pk>" , category_books),
    path("detail/<int:pk>" , book_detail),

    path("search" , search),
]


