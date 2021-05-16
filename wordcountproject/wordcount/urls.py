from django.contrib import admin
from django.urls import path

# views 연결
import wordcountapp.views

urlpatterns = [
    path('admin/', admin.site.urls),

    # wordcountapp 내 view.py 내 home 함수 띄우자, path(url) 이름은 home이다
    path('', wordcountapp.views.home, name = 'home'),
    path('about/', wordcountapp.views.about, name = 'about'),
    path('result/', wordcountapp.views.result, name = 'result'),
]
