from rest_framework import serializers
from .models import PublisherModel, AuthorModel, BookModel

class PublisherSerializer(serializers.ModelSerializer):

    class Meta:
        model= PublisherModel
        fields = ['id', 'name', 'description', 'created', 'updated']

class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = AuthorModel
        fields = ['id', 'first_name', 'last_name','about', 'created', 'updated']

class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = BookModel
        fields = '__all__'
        