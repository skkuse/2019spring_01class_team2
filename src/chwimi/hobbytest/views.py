from django.shortcuts import render

# Create your views here.
def hobbytest(request):
    return render(request, 'hobbytest.html')