from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

app_name = 'shop'

urlpatterns = [ # 우리 app에서 쓸 url패턴을 정의
    url(r'^$', views.product_list, name='product_list'),  # 상품리스트와 url 연결, 모든 상품과도 연결
    url(r'^(?P<category_slug>[-\w]+)/$', views.product_list, name='product_list_by_category'),    # 이것도 상품리스트랑 연결, 카테고리슬러는 지나침
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.product_detail, name='product_detail'), # 상품 디테일과 연결
    url(r'^logout/$', auth_views.LogoutView.as_view(), {'next_page' : '/'}),
    url(r'^login/$', auth_views.LoginView.as_view(),  {'template_name':'shop/login.html'}),


]