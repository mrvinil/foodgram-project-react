from django.urls import include, path
from rest_framework.routers import DefaultRouter

from backend.recipes.views import CustomUserViewSet

app_name = 'users'

router = DefaultRouter()
router.register(r'users', CustomUserViewSet, basename='users')

urlpatterns = [
    path('', include(router.urls))
]
