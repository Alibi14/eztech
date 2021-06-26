from django.http import JsonResponse
from rest_framework import generics
from .models import Area, Point
from .serializers import AreaSerializer, PointSerializer


class AreaList(generics.ListCreateAPIView):
    queryset = Area.objects.all()
    serializer_class = AreaSerializer


class PointList(generics.ListCreateAPIView):
    queryset = Point.objects.all()
    serializer_class = PointSerializer


def area_points(request, pk):
    try:
        area = Area.objects.get(id=pk)
    except Exception as e:
        return JsonResponse({'error', str(e)})

    points = area.points.all()
    points_json = [point.to_json() for point in points]
    return JsonResponse(
        {area.name:
             points_json
         })
