from django.urls import path
from .views import client_home,client_add

app_name = "client"


urlpatterns = [
    path("" , client_home),
    path("add" , client_add),

    
]