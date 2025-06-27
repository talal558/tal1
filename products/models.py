from django.db import models


class Category(models.Model):
    name = models.CharField("اسم القسم", max_length=100)

    class Meta:
        verbose_name = "قسم"
        verbose_name_plural = "الأقسام"

    def __str__(self):
        # إرجاع اسم القسم فقط
        return self.name


class Product(models.Model):
    title = models.CharField("عنوان المنتج", max_length=255)
    description = models.TextField("وصف المنتج")
    price = models.DecimalField("السعر", max_digits=8, decimal_places=2)
    image = models.ImageField("صورة المنتج", upload_to='products/')
    category = models.ForeignKey(
        Category,
        verbose_name="القسم",
        on_delete=models.CASCADE,
        related_name='products'
    )

    class Meta:
        verbose_name = "منتج"
        verbose_name_plural = "المنتجات"

    def __str__(self):
        return f"{self.title} - {self.price} ريال"
