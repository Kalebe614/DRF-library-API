from rest_framework import serializers
from .models import PublisherModel

class PublisherSerializer(serializers.ModelSerializer):

    class Meta:
        model= PublisherModel
        fields = ['id', 'name', 'description', 'created', 'updated']