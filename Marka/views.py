from django.shortcuts import render
from rest_framework.generics import CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAdminUser

from Marka.models import AdminCar
from Marka.serializers import AdminCarSerializer


# Create your views here.

class CarCreate(CreateAPIView):
    permission_classes = [IsAdminUser]
    queryset = AdminCar.objects.all()
    serializer_class = AdminCarSerializer

class CarByIdApiView(RetrieveAPIView):
    permission_classes = [IsAdminUser]
    queryset = AdminCar.objects.all()
    serializer_class = AdminCarSerializer

class CarUpdateApiView(UpdateAPIView):
    permission_classes = [IsAdminUser]
    queryset = AdminCar.objects.all()
    serializer_class = AdminCarSerializer

class CarDeleteApiView(DestroyAPIView):
    permission_classes = [IsAdminUser]
    queryset = AdminCar.objects.all()
    serializer_class = AdminCarSerializer

class CarPagination(PageNumberPagination):

    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 10000

class CarListView(ListAPIView):
    permission_classes = [IsAdminUser]
    queryset = AdminCar.objects.all()
    serializer_class = AdminCarSerializer


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