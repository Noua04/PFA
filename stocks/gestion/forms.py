from django import forms
from .models import Produit
from .models import Fournisseur
from .models import Categorie

class CategorieForm(forms.ModelForm):
    class Meta:
        model = Categorie
        fields = ['nom']
class ProduitForm(forms.ModelForm):
    class Meta:
        model = Produit
        fields = ['nom', 'quantite', 'prix_achat', 'prix_vente', 'categorie', 'fournisseur']
class FournisseurForm(forms.ModelForm):
    class Meta:
        model = Fournisseur
        fields = ['nom', 'adresse', 'telephone', 'email']