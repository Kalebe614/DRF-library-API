from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core import views
router = DefaultRouter()

router.register(r'publisher', views.PublisherViewSet, basename='publisher')
router.register(r'author', views.AuthorViewSet, basename='author')

urlpatterns = [
    path('', include(router.urls)),
]
