"""
URL configuration for HostelsdjangoProject project.

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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from application import views


urlpatterns = [
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),



    path('profile/',views.profile,name='profile'),
    path('profile_form/',views.profile_info,name='profile_form'),
    path('delete_user/',views.delete_user,name='delete_user'),
    path('residence/',views.residence,name='residence'),
    path('listing/',views.listing,name='listing'),
    path("book/<int:room_id>", views.book_hostel, name="book_hostel"),
    path('signup/',views.signup,name='signup'),
    path('signin/',views.signin,name='signin'),
    path('logout/',views.logout,name='logout'),
    path('contact/',views.contact,name='contact'),
    path("update_user/", views.update_user, name="update_user"),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
