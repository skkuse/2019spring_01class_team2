from django.shortcuts import render, get_object_or_404, redirect
from .models import Review, Comment_review
from django.core.paginator import Paginator
from useraccount.models import Profile

# Create your views here.
def review(request):
    reviews = Review.objects.all().order_by('-id')
    paginator = Paginator(reviews, 5)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    return render(request, 'review.html', {'reviews':reviews, 'posts':posts})

def reviewDetail(request, review_id):
    review_detail = get_object_or_404(Review, pk=review_id)
    comment = Comment_review.objects.filter(review=review_id)
    
    product = review_detail.rate_product
    product_none = 5-product

    delivery = review_detail.rate_delivery
    delivery_none = 5-delivery

    price = review_detail.rate_price
    price_none = 5-price

    return render(request, 'reviewDetail.html', {'review':review_detail, 'comment':comment, 'product':range(product), 'nonproduct':range(product_none), 'delivery':range(delivery), 'nondelivery':range(delivery_none),'price':range(price), 'nonprice':range(price_none)}) 

def new_rv(request):
    if request.method == 'POST':
        try:
            review = Review(files = request.FILES['file_review'])
        except:
            review = Review()
        review.user = request.user
        review.title = request.POST['title']
        review.content = request.POST['content']
        review.rate_product = request.POST['rate_product']
        review.rate_delivery = request.POST['rate_delivery']
        review.rate_price = request.POST['rate_price']
        review.save()
        return redirect('/review')
    return render(request, 'new_review.html')

def new_cmt(request, r_pk):
    if request.method == 'POST':
        review = get_object_or_404(Review, pk=r_pk)
        content = request.POST.get('content')
        user = request.user
        profile = Profile.objects.get(user=user)

        Comment_review.objects.create(review = review, writer = profile, content = content)

        return redirect('/review/'+str(r_pk))