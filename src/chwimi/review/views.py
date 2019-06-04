from django.shortcuts import render, get_object_or_404, redirect
from .models import Review, Comment_review
from django.core.paginator import Paginator
from useraccount.models import Profile

# Create your views here.
def review(request):
    reviews = Review.objects.all().order_by('-date')
    paginator = Paginator(reviews, 5)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    return render(request, 'review.html', {'reviews':reviews, 'posts':posts})

def reviewDetail(request, review_id):
    review_detail = get_object_or_404(Review, pk=review_id)
    comment = Comment_review.objects.filter(review=review_id)
    
    return render(request, 'reviewDetail.html', {'review':review_detail, 'comment':comment}) 

def new_cmt(request, r_pk):
    if request.method == 'POST':
        review = get_object_or_404(Review, pk=r_pk)
        content = request.POST.get('content')
        user = request.user
        profile = Profile.objects.get(user=user)

        Comment_review.objects.create(review = review, writer = profile, content = content)

        return redirect('/review')