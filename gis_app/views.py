from .models import *
from .serializers import *


from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


class LocationCreateListView(ListCreateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class LocationRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
