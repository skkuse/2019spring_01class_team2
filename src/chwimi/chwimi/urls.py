from django.contrib import admin
from django.urls import path, include
import main.views
import account.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main.views.home, name='home'),
    path('account/', include('account.urls')),
]
