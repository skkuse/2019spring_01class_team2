from django.shortcuts import render, get_object_or_404
from .models import Notice
from django.core.paginator import Paginator

# Create your views here.
def notice(request):
    notices = Notice.objects.all().order_by('-id')
    paginator = Paginator(notices, 3)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'notice.html', {'notices':notices, 'posts':posts})

def noticeDetail(request, notice_id):
    notice_detail = get_object_or_404(Notice, pk=notice_id)
    return render(request, 'noticeDetail.html', {'notice':notice_detail})