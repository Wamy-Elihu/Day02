class Produit:
    def __init__(self, nom, prix, quantite):
        self.nom = nom
        self.prix = prix
        self.quantite = quantite
        
    def afficher_produit(self):
        print(f"Produit: {self.nom}, Prix: {self.prix}€, Quantité: {self.quantite}")
        
class Magasin:
    def __init__(self):
        self.produits = []
        
    def ajouter_produit(self, produit):
        self.produits.append(produit)
        
    def rechercher_produit(self, nom):
        for produit in self.produits:
            if produit.nom == nom:
                return produit
        return None
    
    def afficher_inventaire(self):
        for produit in self.produits:
            if not self.produits:
                print("Inventaire vide")
            else:
                for produit in self.produits:
                    produit.afficher_produit()
        
    def vendre_produit(self, nom, quantite):
        produit = self.rechercher_produit(nom)
        if produit:
            if produit.quantite >= quantite:
                produit.quantite -= quantite
                print(f"Vente de {quantite} {nom} effectuée avec succès.")
            else:
                print(f"Quantité insuffisante pour {nom}, il ne reste que {produit.quantite} exemplaires.")
        else:
            print(f"Produit {nom} non trouvé dans le magasin.")
            
magasin = Magasin()
magasin.ajouter_produit(Produit("Ananas", 2.5, 2))
magasin.ajouter_produit(Produit("Pain", 3.0, 20))
magasin.ajouter_produit(Produit("Fromage", 1.8, 5))
magasin.ajouter_produit(Produit("Orange", 2.2, 150))

print("Inventaire du magasin :")
magasin.afficher_inventaire()


magasin.vendre_produit("Ananas", 1)
magasin.vendre_produit("Pain", 50)
magasin.vendre_produit("Fromage", 2)
magasin.vendre_produit("Orange", 20)

print("\nInventaire après ventes :")
magasin.afficher_inventaire()