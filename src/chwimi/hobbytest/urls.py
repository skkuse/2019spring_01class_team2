from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.hobbytest, name='hobbytest'),
    path('test_1/', views.test_1, name='test_1'),
    path('test_2/', views.test_2, name='test_2'),
    path('test_2_1/', views.test_2_1, name='test_2_1'),
    path('test_3/', views.test_3, name='test_3'),
    path('test_3_1/', views.test_3_1, name='test_3_1'),
    path('test_4/', views.test_4, name='test_4'),
    path('test_4_1/', views.test_4_1, name='test_4_1'),
    path('test_5/', views.test_5, name='test_5'),
    path('test_5_1/', views.test_5_1, name='test_5_1'),
    path('result/', views.result, name='result'),
]