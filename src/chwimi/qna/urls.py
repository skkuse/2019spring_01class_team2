from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.qna, name='qna'),
    path('<int:question_id>/', views.questionDetail, name='questionDetail'),
]