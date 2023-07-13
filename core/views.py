from rest_framework import viewsets, mixins
from .models import PublisherModel, AuthorModel, BookModel
from .serializers import PublisherSerializer, AuthorSerializer, BookSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

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

    @action(detail=True, methods=['get'])
    def books(self,request, pk=None):
        author = self.get_object()
        books = BookModel.objects.filter(author=author)
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)


class BookViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin, mixins.DestroyModelMixin,
                  mixins.ListModelMixin, viewsets.GenericViewSet):
    
    queryset = BookModel.objects.all()
    serializer_class = BookSerializer