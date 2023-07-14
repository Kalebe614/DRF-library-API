from rest_framework import viewsets, mixins
from .models import PublisherModel, AuthorModel, BookModel
from .serializers import PublisherSerializer, AuthorSerializer, BookSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import permissions

class PublisherViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin,
                       mixins.UpdateModelMixin, mixins.DestroyModelMixin,
                       mixins.ListModelMixin, viewsets.GenericViewSet):
    
    queryset = PublisherModel.objects.all()
    serializer_class = PublisherSerializer

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [permissions.AllowAny]  # Acesso público para listar
        else:
            permission_classes = [permissions.IsAuthenticated]  # Outras ações exigem autenticação
        return [permission() for permission in permission_classes]
    

    @action(detail=True, methods=['get'])
    def books(self, request, pk=None):
        publisher = self.get_object()
        books = BookModel.objects.filter(publisher=publisher)
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

class AuthorViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin, mixins.DestroyModelMixin,
                    mixins.ListModelMixin, viewsets.GenericViewSet):
    
    queryset = AuthorModel.objects.all()
    serializer_class = AuthorSerializer

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [permissions.AllowAny]  # Acesso público para listar
        else:
            permission_classes = [permissions.IsAuthenticated]  # Outras ações exigem autenticação
        return [permission() for permission in permission_classes]

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

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [permissions.AllowAny]  # Acesso público para listar
        else:
            permission_classes = [permissions.IsAuthenticated]  # Outras ações exigem autenticação
        return [permission() for permission in permission_classes]


