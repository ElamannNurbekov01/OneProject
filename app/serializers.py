from django.core.exceptions import ValidationError
from rest_framework import serializers

from app.models import Car, Category, Favorite


class CarSerializer(serializers.ModelSerializer):
    discount_price = serializers.IntegerField(read_only=True)

    def validate_year(self, value):
        """Проверка года выпуска автомобиля."""
        if value < 2012:
            raise ValidationError("Машины младше 2012 года недопустимы.")
        return value

    class Meta:
        model = Car
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = "__all__"

class FavoriteSerializer(serializers.Serializer):
    model = Favorite
    fields = "__all__"

