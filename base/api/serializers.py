from rest_framework import serializers
from base.models import Destination

class DestinationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Destination
        fields = ['id', 'name', 'image', 'fare', 'category', 'description']
