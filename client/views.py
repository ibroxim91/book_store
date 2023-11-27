from django.shortcuts import render



# Create your views here.


def client_home(request):
    return render(request=request, template_name="client.html" )

def client_add(request):
    return render(request=request, template_name="client_add.html" )