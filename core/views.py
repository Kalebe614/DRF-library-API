from rest_framework import viewsets, mixins
from .models import PublisherModel, AuthorModel
from .serializers import PublisherSerializer, AuthorSerializer

class PublisherViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin,
                       mixins.UpdateModelMixin, mixins.DestroyModelMixin,
                       mixins.ListModelMixin, viewsets.GenericViewSet):
    
    queryset = PublisherModel.objects.all()
    serializer_class = PublisherSerializer

class AuthorViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin, mixins.DestroyModelMixin,
                    mixins.ListModelMixin, viewsets.GenericViewSet):
    
    queryset = AuthorModel.objects.all()
    serializer_class = AuthorSerializer
