"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [   # shop app의 urls 포함한 url패턴
    path('admin/', admin.site.urls),     # 관리자 페이지 url정의한 파일과 연동
    path('cart', include('cart.urls')),  # 카트 페이지 url정의한 파일과 연동 !!!! 꼭 shop보다 먼저와야 한다. 그래야 세션이 유지된 상태로 shop가능
    path('', include('shop.urls')),      # shop페이지 url정의한 파일과 연동 / 아무 url입력 안했을 때 defaul값 => shop에서 url가져와 뿌림
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) # settings.py 밑에 media 즉, 이미지 경로를 지정한 파일과 연동