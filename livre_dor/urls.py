""" livre_dor URL Configuration """

from django.contrib import admin
from django.urls import path
from api import views as apiviews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', apiviews.home)
]

