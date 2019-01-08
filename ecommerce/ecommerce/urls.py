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

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [   # shop app의 urls 포함한 url패턴
    path('admin/', admin.site.urls),    
    path('', include('shop.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from shop import views as shop_views

urlpatterns = [   # shop app의 urls 포함한 url패턴
    path('admin/', admin.site.urls),    
    path('', include('shop.urls')),
    path('cart', include('cart.urls')),  # 카트 페이지 url정의한 파일과 연동 !!!! 꼭 shop보다 먼저와야 한다. 그래야 세션이 유지된 상태로 shop가능
    path('accounts/',  include('django.contrib.auth.urls')),
    path('accounts/signup/', shop_views.CreateUserView.as_view(), name='signup'),
    path('accounts/login/done/', shop_views.RegisteredView.as_view(), name='create_user_done'),
    path('analysis/chart/', shop_views.TestT.as_view(), name='chart'),
    path('analysis2/test/', shop_views.testView.as_view(), name='test'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)