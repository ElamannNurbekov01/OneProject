from django.urls import path
from django.conf.urls.static import static

from project import settings
from Marka import views
from Marka.views import CarCreate, CarByIdApiView, CarDeleteApiView, CarUpdateApiView, CarListView

urlpatterns = [
    path('Car/Create/', CarCreate.as_view()),
    path('Car/id/<pk>/', CarByIdApiView.as_view()),
    path('Update/Car/<pk>/',CarUpdateApiView.as_view()),
    path('Delete/Car/<pk>', CarDeleteApiView.as_view()),
    path('Car/list/', CarListView.as_view()),
]