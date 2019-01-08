from django.conf.urls import url
from . import views

app_name = 'cart'

urlpatterns = [   # ^는 ^~~로 시작된다는 의미
    url(r'^$', views.cart_detail, name='cart_detail'), # 카트 디테일 페이지 보여주는 코드
    url(r'^add/(?P<product_id>\d+)/$', views.cart_add, name='cart_add'), # 아이템 추가하는 url 정의
    url(r'^remove/(?P<product_id>\d+)/$', views.cart_remove, name='cart_remove'), # 아이템 제거하는 url 정의    
]