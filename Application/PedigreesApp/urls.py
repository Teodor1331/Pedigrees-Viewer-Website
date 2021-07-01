from django.urls import path
from . import views

urlpatterns = [
    path('view_pedigrees/', views.view_pedigrees)
]