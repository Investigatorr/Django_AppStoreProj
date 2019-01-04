from django.contrib import admin
from .models import Category, Product, SpecialDiscounts # 모델(db역할)에 있는 클래스 두개 가져옴


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'available', 'created_at', 'updated_at']
    list_filter = ['available', 'created_at', 'updated_at']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Product, ProductAdmin)

###############################################################################################################
class SpecialDiscountsAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'originalPrice', 'available', 'created_at', 'updated_at']
    list_filter = ['available', 'created_at', 'updated_at']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(SpecialDiscounts, SpecialDiscountsAdmin)