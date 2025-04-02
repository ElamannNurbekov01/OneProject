from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.exceptions import NotFound
from rest_framework.generics import UpdateAPIView, DestroyAPIView, ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from rest_framework.response import Response

from app.models import Car
from app.serializers import CarSerializer
from app.tg_bot import send_group_message, Changing_machines, Car_deleted


# Create your views here.

@api_view(["POST"])
@permission_classes([IsAuthenticated])

def create_car(request):
    serializer = CarSerializer(data=request.data)
    if serializer.is_valid():
        send_group_message()
        serializer.save()
        return Response({
            "status": "CREATED",
            'data': serializer.data,
        }, status=200)
    return Response(serializer.errors, status=400)


@api_view(["GET"])
def get_all_car(request):
    cars = Car.objects.all()
    serializer = CarSerializer(cars, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET"])
def get_car_by_id(request, car_id):
    car = Car.objects.filter(id=car_id).first()
    if not car:
        return Response({"message": "not found"}, status=status.HTTP_404_NOT_FOUND)
    serializer = CarSerializer(car)
    return Response(serializer.data, status=status.HTTP_200_OK)

@permission_classes([IsAuthenticated])
class CarUpdateApiView(UpdateAPIView):

    queryset = Car.objects.all()
    serializer_class = CarSerializer

    def perform_update(self, serializer):
        super().perform_update(serializer)
        Changing_machines()

    def update(self, request, *args, **kwargs):
        try:
            return super().update(request, *args, **kwargs)
        except NotFound:
            return Response("Объект не найден")




@permission_classes([IsAuthenticated])
class CarDeleteApiView(DestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

    def perform_destroy(self, instance):
        super().perform_destroy(instance)  # Удаляем объект
        Car_deleted()



class CarPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 10000

# GET
class CarListView(ListAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    pagination_class = CarPagination



    def get_queryset(self):
        queryset = super().get_queryset()
        brand = self.request.query_params.get('brand')
        year = self.request.query_params.get('year')
        price = self.request.query_params.get('price')

        if brand:
            queryset = queryset.filter(brand=brand)
        if year:
            queryset = queryset.filter(year=year)
        if price:
            queryset = queryset.filter(price__gte=price)

        return queryset


from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Car, Favorite


@api_view(["POST"])
def add_to_favorite(request, car_id):

    car = get_object_or_404(Car, id=car_id)
    favorite, created = Favorite.objects.get_or_create(user=request.user, car=car)

    if created:
        return JsonResponse({ 'message': 'Авто добавлено в избранное'})
    else:
        return JsonResponse({'message': 'Авто уже в избранном'})


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def view_favorites(request):

    Featured = Favorite.objects.filter(user=request.user)
    favorite_list = [
        {
            'id': fav.car.id,
            'name': fav.car.name,
            'brand': fav.car.brand,
            'year': fav.car.year,
            'full_price': fav.car.full_price,
            'discount_price': fav.car.discount_price,
            'is_sold': fav.car.is_sold,
            'image': fav.car.img.url if fav.car.img else None
        } for fav in Featured
    ]
    return JsonResponse({'favorites': favorite_list})

@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def remove_from_favorite(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    favorite = Favorite.objects.filter(user=request.user, car=car)

    if favorite.exists():
        favorite.delete()
        return JsonResponse({'message': 'Авто удалено из избранного'})
    else:
        return JsonResponse({'message': 'Авто не найдено в избранном'})
