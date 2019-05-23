from django.contrib import admin
from django.urls import path, include
import main.views
import account.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main.views.home, name='home'),
    path('account/', include('account.urls')),
    path('qna/', include('qna.urls')),
    path('hobbytest/', include('hobbytest.urls')),
    path('subscribe/', include('subscribe.urls')),
    path('review/', include('review.urls')),
]

# admin/youngadmin