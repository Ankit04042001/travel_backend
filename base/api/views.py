from django.http import HttpResponse
from .serializers import DestinationSerializer
from base.models import Destination, Category
from rest_framework import generics
from rest_framework.response import Response


class DestinationListAPIView(generics.ListAPIView):
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer

    def get(self, request):
        queryset = Destination.objects.all()
        category = Category.objects.all()
        response = {}
        for i in category:
            response[i.name]  = []

        for query in queryset:
            response[query.category.name].append({
                'id' : query.id,
                'name' : query.name,
                'image' : query.image.url,
                'fare' : query.fare,
                'description' : query.description
            })

        return Response(response)

class DestinationDetailAPIView(generics.RetrieveAPIView):
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer

    def get(self, request, pk):
        query = Destination.objects.get(pk=pk)

        return Response({
            'id' : query.id,
            'name' : query.name,
            'image' : query.image.url,
            'fare' : query.fare,
            'category' : query.category.name,
            'description' : query.description
        })
