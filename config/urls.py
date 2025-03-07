"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# createsuperuser
# username - admin
# password - admin

# username - Ram
# password - ram12345

# username - shyam
# password - shy123456

# username - Sita
# password - sita12345

from django.contrib import admin 
from django.urls import path, include
from django.http import HttpResponse
from blog import views


def test_function(request):
    return HttpResponse("<h1>Aashvin Kumar</h1><p>Hi my name is Aashvin Kumar live in Korba</p>")


def about_function(request):
    return HttpResponse(
        "<label>Name:</label><input type=text></br></br><label>Email:</label><input type=email></br></br><button>Submit</button>")


def home_function(request):
    return HttpResponse("<h1>Home Page</h1>")


urlpatterns = [
    path("admin/", admin.site.urls),
    # path("test/", test_function),
    # path("about/", about_function),
    # path("", home_function),
    path("", include("blog.urls")),
    path("__reload__/", include("django_browser_reload.urls")),
    path("accounts/", include("accounts.urls")), # sign up
    path("accounts/", include("django.contrib.auth.urls")), # login, pasword reset,pasword change

] 
