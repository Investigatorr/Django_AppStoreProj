# 웹에 띄울 상품 리스트와 개별 상품의 형태를 정의
from django.shortcuts import render, get_object_or_404
from .models import Category, Product, SpecialDiscounts
from cart.forms import CartAddProductForm   # shop에 cart버튼을 추가하기 위한 임포트


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