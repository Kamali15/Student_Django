
from django.contrib import admin
from django.urls import path
from django.contrib.auth.decorators import login_required

from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Home,name="home"),
    path('Studentregister',login_required(StudentCreate.as_view()), name="register"),
    path('studentlist',StudentList.as_view(),name='students_list'),

]
