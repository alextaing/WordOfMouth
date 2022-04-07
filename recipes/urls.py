from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "recipes"
urlpatterns = [
    path('', views.IndexView, name='index'),
    # path('user/', views.UserView, name='user'),
    path('user/<int:pk>/', views.UserView.as_view(), name='user'),
    path('recipes/', views.RecipeGalleryView.as_view(), name='recipeGallery'),
    path('recipes/enter-recipe/', views.EnterRecipeView.as_view(), name='enterRecipe'),
    path('recipes/new-recipe/<int:pkUser>', views.newRecipe, name='newRecipe'),
    path('recipes/<int:pk>/', views.RecipeView.as_view(), name='recipe'),
    path('recipes/favorite-recipe/<int:pkRecipe>/<int:pkUser>', views.favoriteRecipe, name='favoriteRecipe'),
    path('user/follow-user/<int:pkFollow>/<int:pkUser>', views.followUser, name='followUser'),
]