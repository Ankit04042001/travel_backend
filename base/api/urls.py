from django.urls import path, include
from .views import DestinationListAPIView, DestinationDetailAPIView

urlpatterns = [
    path('destinations/', DestinationListAPIView.as_view(), name='destination_list'),
    path('destination/<pk>', DestinationDetailAPIView.as_view(), name='destination_detail')
]
