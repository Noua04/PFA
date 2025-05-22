from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Produit, Fournisseur, Categorie, MouvementStock
from .forms import ProduitForm, FournisseurForm
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.db.models import Count
from django.db.models import Q

@login_required
def dashboard(request):
    # Statistiques générales
    stats = {
        'total_produits': Produit.objects.count(),
        'total_fournisseurs': Fournisseur.objects.count(),
        'total_categories': Categorie.objects.count(),
    }
    
    # Produits à faible stock (moins de 10 unités)
    produits_faible_stock = Produit.objects.filter(quantite__lt=10)
    
    # Derniers mouvements de stock
    derniers_mouvements = MouvementStock.objects.all().order_by('-date')[:5]
    
    context = {
        'stats': stats,
        'produits_faible_stock': produits_faible_stock,
        'derniers_mouvements': derniers_mouvements,
    }
    return render(request, 'inventory/dashboard.html', context)

# --- Gestion des Produits ---
@login_required
def liste_produits(request):
    produits = Produit.objects.all()
    
    return render(request, 'inventory/produits/liste.html', {'produits': produits})

@login_required
def ajouter_produit(request):
    if request.method == 'POST':
        form = ProduitForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_produits')
    else:
        form = ProduitForm()
    return render(request, 'inventory/produits/ajouter.html', {'form': form})

@login_required
def modifier_produit(request, pk):
    produit = get_object_or_404(Produit, pk=pk)
    form = ProduitForm(request.POST or None, instance=produit)
    if form.is_valid():
        form.save()
        return redirect('liste_produits')
    return render(request, 'inventory/produits/modifier.html', {'form': form})

@login_required
def supprimer_produit(request, pk):
    produit = get_object_or_404(Produit, pk=pk)
    if request.method == 'POST':
        produit.delete()
        return redirect('liste_produits')
    return render(request, 'inventory/produits/supprimer.html', {'produit': produit})

# --- Gestion des Fournisseurs ---

@login_required
def liste_fournisseurs(request):
    fournisseurs = Fournisseur.objects.all()
    return render(request, 'inventory/fournisseurs/liste.html', {'fournisseurs': fournisseurs})

@login_required
def ajouter_fournisseur(request):
    if request.method == 'POST':
        form = FournisseurForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_fournisseurs')
    else:
        form = FournisseurForm()
    return render(request, 'inventory/fournisseurs/ajouter.html', {'form': form})

@login_required
def modifier_fournisseur(request, pk):
    fournisseur = get_object_or_404(Fournisseur, pk=pk)
    if request.method == 'POST':
        form = FournisseurForm(request.POST, instance=fournisseur)
        if form.is_valid():
            form.save()
            return redirect('liste_fournisseurs')
    else:
        form = FournisseurForm(instance=fournisseur)
    return render(request, 'inventory/fournisseurs/modifier.html', {'form': form})

@login_required
def supprimer_fournisseur(request, pk):
    fournisseur = get_object_or_404(Fournisseur, pk=pk)
    if request.method == 'POST':
        fournisseur.delete()
        return redirect('liste_fournisseurs')
    return render(request, 'inventory/fournisseurs/supprimer.html', {'fournisseur': fournisseur})

def custom_logout(request):
    logout(request)
    return redirect('login')  

@login_required
def liste_categories(request):
    categories = Categorie.objects.all()
    return render(request, 'inventory/categories/liste.html', {'categories': categories})

@login_required
def ajouter_categorie(request):
    if request.method == 'POST':
        form = CategorieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_categories')
    else:
        form = CategorieForm()
    return render(request, 'inventory/categories/ajouter.html', {'form': form})

@login_required
def modifier_categorie(request, pk):
    categorie = get_object_or_404(Categorie, pk=pk)
    if request.method == 'POST':
        form = CategorieForm(request.POST, instance=categorie)
        if form.is_valid():
            form.save()
            return redirect('liste_categories')
    else:
        form = CategorieForm(instance=categorie)
    return render(request, 'inventory/categories/modifier.html', {'form': form})

@login_required
def supprimer_categorie(request, pk):
    categorie = get_object_or_404(Categorie, pk=pk)
    if request.method == 'POST':
        categorie.delete()
        return redirect('liste_categories')
    return render(request, 'inventory/categories/supprimer.html', {'categorie': categorie})
