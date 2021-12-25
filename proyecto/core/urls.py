from django.urls import path
from .views import createArticle, home 

urlpatterns = [
    path('', home, name="home"),
    path('createArticle/', createArticle, name="createArticle"),
]
