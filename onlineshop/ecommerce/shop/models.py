from django.db import models
from django.urls import reverse


'''
!!! 카테고리 !!!
name : 카테고리명
slug : 고유 한 필드. 나중에 표준 URL을 작성하는 데 도움.
created_at : 카테고리 생긴 날짜 기록
updated_at : 카테고리 업뎃 날짜 기록
'''


class Category(models.Model):
    name = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, unique=True ,db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name', )
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):  # shop url에서 seo-friendly url을 만들기 위한 메소드
        return reverse('shop:product_list_by_category', args=[self.slug])


'''
!!! 제품 !!!
'''

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)  # 이 문장 related_name 의미는??
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)
    description = models.TextField(blank=True)
    price = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(blank=True, upload_to='shop')
    # index => id랑 슬러그 특정해준다. 쿼리 날릴때 성능 UP!
    class Meta:
        ordering = ('name', )
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.slug])


###################################################################################################

class SpecialDiscounts(models.Model):
    category = models.ForeignKey(Category, related_name='Salse_products', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)
    description = models.TextField(blank=True)
    price = models.PositiveIntegerField()
    originalPrice = models.DecimalField(max_digits=10, decimal_places=2)    # 기존 품목과는 다른 항목 반영!!!
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(blank=True, upload_to='shop')

    class Meta:
        ordering = ('name', )
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name
        