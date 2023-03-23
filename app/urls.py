from django.urls import path

from .views import ShowMenu

urlpatterns = [
    path('', ShowMenu.as_view()),
    path('<slug:slug>', ShowMenu.as_view(), name='slug'),
]