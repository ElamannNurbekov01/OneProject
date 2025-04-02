from django.core.exceptions import ValidationError
from rest_framework import serializers

from app.models import Car, Category
from Marka.models import AdminCar, AdminCategory


class AdminCarSerializer(serializers.ModelSerializer):
    discount_price = serializers.IntegerField(read_only=True)

    def validate_year(self, value):
        """Проверка года выпуска автомобиля."""
        if value < 2012:
            raise ValidationError("Машины младше 2012 года недопустимы.")
        return value


    class Meta:
        model = AdminCar
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = AdminCategory
        fields = "__all__"