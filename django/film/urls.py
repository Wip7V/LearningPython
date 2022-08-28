from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('director/<pk>', views.DirectorDetail.as_view(), name='detalle_director'),
    path('film/<pk>', views.FilmDetail.as_view(), name='detalle_film'),
]