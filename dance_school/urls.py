from . import views

from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path("home/", view=views.test_view, name="home"),
    path(route="", view=views.test_view, name='test'),
    
]
