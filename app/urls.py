from django.urls import path

from account import views
from app.views import create_car, get_all_car, get_car_by_id, CarUpdateApiView, CarDeleteApiView, CarListView, \
    add_to_favorite, view_favorites, remove_from_favorite

urlpatterns = [
    path('create/', create_car),
    path('get/', get_all_car),
    path('get/<int:car_id>', get_car_by_id),
    path('update/<pk>', CarUpdateApiView.as_view()),
    path('car/delete/<pk>', CarDeleteApiView.as_view()),
    path('pagination/', CarListView.as_view()),
    path('favorite/add/<int:car_id>/', add_to_favorite),
    path('favorite/view/', view_favorites),
    path('favorite/remove/<int:car_id>/', remove_from_favorite),
]

