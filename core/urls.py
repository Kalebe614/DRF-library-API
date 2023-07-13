from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core import views
router = DefaultRouter()

router.register(r'publishers', views.PublisherViewSet, basename='publishers')
router.register(r'authors', views.AuthorViewSet, basename='authors')
router.register(r'books', views.BookViewSet, basename='books')

urlpatterns = [
    path('', include(router.urls)),
]
