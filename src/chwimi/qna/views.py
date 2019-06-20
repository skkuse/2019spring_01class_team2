from django.shortcuts import render, get_object_or_404, redirect
from .models import Question, Comment_question
from django.core.paginator import Paginator
from useraccount.models import Profile

# 질의응답 페이지 호출
def qna(request):
    questions = Question.objects.all().order_by('-id')
    paginator = Paginator(questions, 5)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'qna.html', {'questions':questions, 'posts':posts})

# 질문 상세보기
def questionDetail(request, question_id):
    question_detail = get_object_or_404(Question, pk=question_id)
    comment = Comment_question.objects.filter(question=question_id)
    
    return render(request, 'questionDetail.html', {'question':question_detail, 'comment':comment})

# 새 질문 등록
def new_question(request):
    if request.method == 'POST':
        try:
            question = Question(files = request.FILES['file_qna'])
        except:
            question = Question()
        question.user = request.user
        question.title = request.POST['title']
        question.content = request.POST['content']
        question.save()
        return redirect('/qna')
    return render(request, 'new_qna.html')

# 새 댓글 남기기
def new_cmt(request, q_pk):
    if request.method == 'POST':
        question = get_object_or_404(Question, pk=q_pk)
        content = request.POST.get('content')
        user = request.user
        profile = Profile.objects.get(user=user)

        Comment_question.objects.create(question = question, writer = profile, content = content)

        return redirect('/qna/'+str(q_pk))
