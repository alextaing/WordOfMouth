# /***************************************************************************************
# *  REFERENCES
# *  Title: multiple parameters url pattern django 2.0
# *  Author: user9723456, philmaweb
# *  Publication Date: 7/22/2018
# *  URL: https://stackoverflow.com/questions/51464131/multiple-parameters-url-pattern-django-2-0
# ***************************************************************************************/

from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "recipes"
urlpatterns = [
    # path('', views.IndexView, name='index'),
    path('', views.IndexView.as_view(), name='index'),
    # path('user/', views.UserView, name='user'),
    path('user/<int:pk>/', views.UserView.as_view(), name='user'),
    path('user/<int:pk>/<tab>/', views.UserView.as_view(), name='userTab'),
    path('user/logout/', views.userLogout, name='userLogout'),
    path('recipes/', views.RecipeGalleryView.as_view(), name='recipeGallery'),
    path('recipes/enter-recipe/', views.EnterRecipeView.as_view(), name='enterRecipe'),
    path('recipes/new-recipe/<int:pkUser>/<int:fork>/<int:pkRecipe>', views.newRecipe, name='newRecipe'),
    # <int:fork> = fork? 1:0; only read <int:pkRecipe> if fork=1
    path('recipes/<int:pk>/', views.RecipeView.as_view(), name='recipe'),
    path('recipes/fork/<int:pk>/', views.forkRecipe, name='fork'),
    path('recipes/favorite-recipe/<int:pkRecipe>/<int:pkUser>', views.favoriteRecipe, name='favoriteRecipe'),
    path('recipes/unfavorite-recipe/<int:pkRecipe>/<int:pkUser>', views.unfavoriteRecipe, name='unfavoriteRecipe'),
    path('recipes/delete/<int:pk>', views.deleteRecipe, name='deleteRecipe'),
    # Citation for <multiple parameters url pattern django 2.0> at top of file
    path('user/follow-user/<int:pkFollow>/<int:pkUser>', views.followUser, name='followUser'),
    path('user/unfollow-user/<int:pkFollow>/<int:pkUser>', views.unfollowUser, name='unfollowUser'),
    path('user/update/name/<int:pkUser>', views.updateUserName, name='updateUserName'),
    path('user/update/cook_exp/<int:pkUser>', views.updateUserCookExp, name='updateUserCookExp'),
    path('user/update/profile_img/<int:pkUser>', views.updateUserProfileImg, name='updateUserProfileImg'),
    
    # pdf generation
    path("recipes/recipe_pdf/<int:pk>/", views.recipe_pdf, name = 'recipe_pdf'),
    
]