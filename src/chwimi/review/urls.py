from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.review, name='review'),
    path('<int:review_id>/', views.reviewDetail, name='reviewDetail'),
    path('new/<int:r_pk>', views.new_cmt, name='newRv'),
    path('new/', views.new_rv, name='new_review_post')
]