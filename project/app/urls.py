from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('stu_list/',StudentList.as_view(),name='stu_list'),
    path('stu_details/<int:pk>',StudentDetail.as_view(),name='stu_detail')
]