class Livre:
    
    def __init__(self, titre, auteur):
        self.titre = titre
        self.auteur = auteur
        self.disponible = True

    def emprunter(self):
        if self.disponible:
            self.disponible = False
            return True
        return False

    def rendre(self):
        self.disponible = True

class Utilisateur:
    
    def __init__(self, nom):
        self.nom = nom
        self.livres_empruntes = []

    def emprunter_livre(self, livre):
        if livre.emprunter():
            self.livres_empruntes.append(livre)
            print(f"{self.nom} a emprunté {livre.titre}.")
        else:
            print(f"{livre.titre} n'est pas disponible.")

    def rendre_livre(self, livre):
        if livre in self.livres_empruntes:
            livre.rendre()
            self.livres_empruntes.remove(livre)
            print(f"{self.nom} a rendu {livre.titre}.")

class Bibliotheque:
    
    def __init__(self):
        self.livres = []

    def ajouter_livre(self, livre):
        self.livres.append(livre)

    def afficher_livres(self):
        for livre in self.livres:
            statut = "disponible" if livre.disponible else "emprunté"
            print(f"{livre.titre} par {livre.auteur} - {statut}")

    def gerer_emprunt(self, utilisateur, livre, action):
        if action == "emprunter":
            utilisateur.emprunter_livre(livre)
        elif action == "rendre":
            utilisateur.rendre_livre(livre)

biblio = Bibliotheque()
livre1 = Livre("1984", "George Orwell")
livre2 = Livre("Le Petit Prince", "Antoine de Saint-Exupéry")
biblio.ajouter_livre(livre1)
biblio.ajouter_livre(livre2)

utilisateur1 = Utilisateur("Alice")
biblio.gerer_emprunt(utilisateur1, livre1, "emprunter")
biblio.gerer_emprunt(utilisateur1, livre1, "rendre")
biblio.afficher_livres()