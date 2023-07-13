from rest_framework import viewsets, mixins
from .models import PublisherModel
from .serializers import PublisherSerializer

class PublisherViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin,
                       mixins.UpdateModelMixin, mixins.DestroyModelMixin,
                       mixins.ListModelMixin, viewsets.GenericViewSet):
    
    queryset = PublisherModel.objects.all()
    serializer_class = PublisherSerializer
