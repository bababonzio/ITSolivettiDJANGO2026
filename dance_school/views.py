from django.http import HttpResponse
from django.shortcuts import render

def test_view(request):
    return HttpResponse

def home(request):
    return render(request, template_name="home.html")

    
def about(request):
    return render(request, template_name="about.html")