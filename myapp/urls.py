
from django.contrib import admin
from django.urls import path
from app1.views import mymethod

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',mymethod)
]
