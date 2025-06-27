from django.contrib import admin
from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    ordering = ('name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'category', 'display_image')
    list_filter = ('category',)
    search_fields = ('title', 'description')
    ordering = ('-id',)

    def display_image(self, obj):
        if obj.image:
            # عرض اسم ملف الصورة فقط بدون رابط أو HTML
            return f"📷 {obj.image.name.split('/')[-1]}"
        return "لا توجد صورة"

    display_image.short_description = 'صورة المنتج'
