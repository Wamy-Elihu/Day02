class Plat:
    
    def __init__(self, nom, prix, temps_preparation):
        self.nom = nom
        self.prix = prix
        self.temps_preparation = temps_preparation

    def afficher_details(self):
        print(f"Plat: {self.nom}, Prix: {self.prix}, Temps de préparation: {self.temps_preparation} min")

class Serveur:
    
    def __init__(self, nom, commandes_prises):
        self.nom = nom
        self.commandes_prises = []

    def prendre_commande(self, plat):
        self.commandes_prises.append(plat)
        print(f"{self.nom} a pris la commande de {plat.nom}.")

class Restaurant:
    
    def __init__(self):
        self.plats = []
        self.serveurs = []

    def ajouter_plat(self, plat):
        self.plats.append(plat)

    def ajouter_serveur(self, serveur):
        self.serveurs.append(serveur)

    def afficher_menu(self):
        for plat in self.plats:
            plat.afficher_details()

    def gerer_commandes(self, serveur, plat):
        serveur.prendre_commande(plat)

restaurant = Restaurant()
plat1 = Plat("Pizza", 11, 22)
plat2 = Plat("Lasagne", 34, 4)

serveur1 = Serveur("Pierre")

restaurant.ajouter_plat(plat1)
restaurant.ajouter_plat(plat2)
restaurant.ajouter_serveur(serveur1)
restaurant.afficher_menu()
restaurant.gerer_commandes(serveur1, plat1)