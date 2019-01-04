from .models import Category, Product, SpecialDiscounts
from django.views.generic.base import TemplateView
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView # 오브젝트를 생성하는 뷰 (form 혹은 model과 연결되서 새로운 데이터를 넣을 때 CreateView - generic view를 사용)
# from django.contrib.auth.forms import UserCreationForm  >>  장고의 기본 회원가입 폼 (ID, PW만 확인한다 - 뒤에서 이메일 추가 커스터미아징 예정)
from .forms import CreateUserForm # 장고의 기본 회원가입 폼을 커스터마이징 한 폼
from django.urls import reverse_lazy # generic view에서는 reverse_lazy를 사용한다.
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.contrib.auth.models import Group, User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout



# CBV (Class Based View 작성!)
class CreateUserView(CreateView): # generic view중에 CreateView를 상속받는다.
    template_name = 'registration/signup.html' # 템플릿은?
    form_class =  CreateUserForm # 푸슨 폼 사용? >> 내장 회원가입 폼을 커스터마지징 한 것을 사용하는 경우
    # form_class = UserCreationForm >> 내장 회원가입 폼 사용하는 경우
    success_url = reverse_lazy('create_user_done') # 성공하면 어디로?

class RegisteredView(TemplateView): # generic view중에 TemplateView를 상속받는다.
    template_name = 'registration/signup_done.html' # 템플릿은?
class IndexView(TemplateView): # TemplateView를 상속 받는다.
    template_name = 'list.html'



def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)  
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category)# SpecialDiscountItem = SpecialDiscounts.objects.filter((category=category)        

    context = {
        'category': category,
        'categories': categories,
        'products': products
    }
    return render(request, 'shop/product/list.html', context)


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    context = {
        'product': product
    }
    return render(request, 'shop/product/detail.html', context)