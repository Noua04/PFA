from django.contrib import admin
from .models import Categorie, Fournisseur, Produit, MouvementStock, Client, Achat

@admin.register(Categorie)
class CategorieAdmin(admin.ModelAdmin):
    list_display = ('id', 'nom')
    search_fields = ('nom',)

@admin.register(Fournisseur)
class FournisseurAdmin(admin.ModelAdmin):
    list_display = ('id', 'nom', 'telephone', 'email')
    search_fields = ('nom', 'email')

@admin.register(Produit)
class ProduitAdmin(admin.ModelAdmin):
    list_display = ('id', 'nom', 'categorie', 'fournisseur', 'quantite', 'prix_achat', 'prix_vente')
    search_fields = ('nom',)
    list_filter = ('categorie', 'fournisseur')

@admin.register(MouvementStock)
class MouvementStockAdmin(admin.ModelAdmin):
    list_display = ('id', 'produit', 'type', 'quantite', 'date')
    list_filter = ('type', 'date')

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'nom', 'email', 'telephone')
    search_fields = ('nom', 'email')

@admin.register(Achat)
class AchatAdmin(admin.ModelAdmin):
    list_display = ('id', 'client', 'produit', 'quantite', 'date')
    list_filter = ('date',)
