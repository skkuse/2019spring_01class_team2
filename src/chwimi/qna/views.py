from django.shortcuts import render, get_object_or_404
from .models import Question, Comment_question
from django.core.paginator import Paginator


# Create your views here.
def qna(request):
    questions = Question.objects.all().order_by('-date')
    paginator = Paginator(questions, 5)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'qna.html', {'questions':questions, 'posts':posts})

def questionDetail(request, question_id):
    question_detail = get_object_or_404(Question, pk=question_id)
    return render(request, 'questionDetail.html', {'question':question_detail})