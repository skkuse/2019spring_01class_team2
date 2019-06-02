from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import main.views
import useraccount.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main.views.home, name='home'),
    path('about/', main.views.about, name='about'),
    path('mypage/', main.views.mypage, name='mypage'),
    path('useraccount/', include('useraccount.urls')),
    path('accounts/', include('allauth.urls')),
    path('qna/', include('qna.urls')),
    path('hobbytest/', include('hobbytest.urls')),
    path('subscribe/', include('subscribe.urls')),
    path('review/', include('review.urls')),
    path('notice/', include('notice.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# admin/youngadmin