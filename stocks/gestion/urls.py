from django.urls import path
from . import views
from .views import custom_logout
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('', views.dashboard, name='dashboard'),  # Page d'accueil
    path('produits/', views.liste_produits, name='liste_produits'),
    path('produits/ajouter/', views.ajouter_produit, name='ajouter_produit'),
    path('produits/modifier/<int:pk>/', views.modifier_produit, name='modifier_produit'),
    path('produits/supprimer/<int:pk>/', views.supprimer_produit, name='supprimer_produit'),
    path('fournisseurs/', views.liste_fournisseurs, name='liste_fournisseurs'),
    path('fournisseurs/ajouter/', views.ajouter_fournisseur, name='ajouter_fournisseur'),
    path('fournisseurs/modifier/<int:pk>/', views.modifier_fournisseur, name='modifier_fournisseur'),
    path('fournisseurs/supprimer/<int:pk>/', views.supprimer_fournisseur, name='supprimer_fournisseur'),
    path('logout/', custom_logout, name='logout'),
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),

     path('categories/', views.liste_categories, name='liste_categories'),
    path('categories/ajouter/', views.ajouter_categorie, name='ajouter_categorie'),
    path('categories/modifier/<int:pk>/', views.modifier_categorie, name='modifier_categorie'),
    path('categories/supprimer/<int:pk>/', views.supprimer_categorie, name='supprimer_categorie'),


]
