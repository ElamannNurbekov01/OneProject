from django.db import models

# Create your models here.
from django.core.exceptions import ValidationError
from django.db import models



# Create your models here.
class AdminCategory(models.Model):
    full_name = models.CharField(max_length=20, verbose_name="Полное название Категорий")
    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Category'


class AdminCar(models.Model):
    name = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)
    year = models.IntegerField()
    description = models.TextField()
    discount_price = models.IntegerField(default=0)
    is_sold = models.BooleanField(default=False)
    quantity = models.PositiveIntegerField(default=0)
    full_price = models.IntegerField()
    date = models.DateField()

    is_take_away = models.BooleanField(default=False)
    img = models.ImageField(upload_to='admin_car/')
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(AdminCategory, related_name="categories",on_delete=models.CASCADE)
    discount = models.IntegerField()

    def save(self, *args, **kwargs):
        if self.discount == 0:
            self.discount = self.full_price
        else:
            self.discount_price = self.full_price * (1 - self.discount / 100)
        super().save(*args, **kwargs)