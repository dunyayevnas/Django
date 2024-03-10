from django.urls import path

from .views import themes_list
urlpatterns = [
    path('themes/', themes_list),
]