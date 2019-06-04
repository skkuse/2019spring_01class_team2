from django.contrib import admin
from .models import Review, Comment_review
# Register your models here.

admin.site.register(Review)
admin.site.register(Comment_review)