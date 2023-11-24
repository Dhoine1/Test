
from django.contrib import admin
from django.urls import path
from file.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index)
]
