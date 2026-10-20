from . import views

from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path("home/", view=views.home, name="home"),
    path("about/", view=views.about, name="about"),
    path(route="", view=views.home, name='home'),
    
]
