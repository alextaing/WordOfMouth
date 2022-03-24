from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "recipes"
urlpatterns = [
    path('', views.IndexView, name='index'),
    path('user/', views.UserView, name='user'),
    path('recipes/', views.RecipeGalleryView.as_view(), name='recipeGallery'),
    # path('recipe/', views.RecipeView, name='recipe'), # this is the individual recipe page; should figure out how to add recipe_id as part of url later
    path('recipe/<int:pk>/', views.RecipeView.as_view(), name='recipe')
]