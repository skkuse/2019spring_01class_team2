from django.contrib import admin
from .models import Question, Comment_question
# Register your models here.


admin.site.register(Question)
admin.site.register(Comment_question)