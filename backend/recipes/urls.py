from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (CustomUserViewSet, IngredientsViewSet, RecipeViewSet,
                    TagViewSet)

app_name = 'recipes'

router = DefaultRouter()

router.register(r'tags', TagViewSet, basename='tags')
router.register(r'recipes', RecipeViewSet, basename='recipes')
router.register(r'ingredients', IngredientsViewSet, basename='ingredients')

urlpatterns = [
    path('v1/', include(router.urls))
]
