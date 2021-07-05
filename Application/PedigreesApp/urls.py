from django.urls import path
from . import views

urlpatterns = [
    path('view_pedigrees/', views.view_pedigrees),
    path('view_pedigrees/<str:pedigree_name>', views.view_pedigrees_new)
]