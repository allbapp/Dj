# myapp/views.py

from django.http import HttpResponse

def data_view(request):
    return HttpResponse("This is the data page.")

def test_view(request):
    return HttpResponse("This is the test page.")

def home_view(request):
    return HttpResponse("Welcome to the home page.")
