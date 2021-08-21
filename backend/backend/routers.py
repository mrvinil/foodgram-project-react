from rest_framework.routers import DefaultRouter

from backend.recipes.views import (CustomUserViewSet, IngredientsViewSet,
                                   RecipeViewSet, TagViewSet)

v1_router = DefaultRouter()

v1_router.register(r'tags', TagViewSet, basename='tags')
v1_router.register(r'recipes', RecipeViewSet, basename='recipes')
v1_router.register(r'ingredients', IngredientsViewSet, basename='ingredients')
v1_router.register(r'users', CustomUserViewSet, basename='users')
