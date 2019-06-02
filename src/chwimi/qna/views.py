from django.shortcuts import render, get_object_or_404, redirect
from .models import Question, Comment_question
from django.core.paginator import Paginator
from useraccount.models import Profile

# Create your views here.
def qna(request):
    questions = Question.objects.all().order_by('-date')
    paginator = Paginator(questions, 5)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'qna.html', {'questions':questions, 'posts':posts})

def questionDetail(request, question_id):
    question_detail = get_object_or_404(Question, pk=question_id)
    comment = Comment_question.objects.filter(question=question_id)
    
    return render(request, 'questionDetail.html', {'question':question_detail, 'comment':comment})

def new_cmt(request, q_pk):
    if request.method == 'POST':
        question = get_object_or_404(Question, pk=q_pk)
        content = request.POST.get('content')
        user = request.user
        profile = Profile.objects.get(user=user)

        Comment_question.objects.create(question = question, writer = profile, content = content)

        return redirect('/qna')
