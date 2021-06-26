from django.contrib import admin
from django.urls import path
from .views import AreaList, PointList, area_points

urlpatterns = [
    path('areas/', AreaList.as_view()),
    path('points/', PointList.as_view()),
    path('areas/<int:pk>/points/', area_points)
]
