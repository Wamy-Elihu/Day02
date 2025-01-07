class Article:
    
    def __init__(self, nom, prix, quantite_en_stock):
        self.nom = nom
        self.prix = prix
        self.quantite_en_stock = quantite_en_stock

    def retirer_stock(self, quantite):
        if self.quantite_en_stock >= quantite:
            self.quantite_en_stock -= quantite
            return True
        return False

class Commande:
    
    def __init__(self, client, articles_commandes):
        self.client = client
        self.articles_commandes = []

    def ajouter_article(self, article, quantite):
        if article.retirer_stock(quantite):
            self.articles_commandes.append((article, quantite))
            print(f"{quantite} {article.nom} ajoutés à la commande.")
        else:
            print(f"Stock insuffisant pour {article.nom}.")

    def calculer_total(self):
        total = sum(article.prix * quantite for article, quantite in self.articles_commandes)
        print(f"Total de la commande: {total}")

article1 = Article("Effaceur Tipex", 1.5, 100)
article2 = Article("Livert", 3.0, 50)

commande = Commande("Gaston")
commande.ajouter_article(article1, 10)
commande.ajouter_article(article2, 5)
commande.calculer_total()