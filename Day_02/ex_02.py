from datetime import datetime

class Voiture:
    
    def __init__(self, marque, modele, annee, kilometrage):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.kilometrage = kilometrage

    def afficher_details(self):
        print(f"Marque: {self.marque}, Modèle: {self.modele}, Année: {self.annee}, Kilométrage: {self.kilometrage} km")

    def augmenter_kilometrage(self, kilometres):
        if kilometres > 0:
            self.kilometrage += kilometres
        else:
            print("Il doit être supérieur à 0.")
            
    def calculer_age(self):
        annee_acutelle = datetime.now().year
        return annee_acutelle - self.annee
    
    def est_vieille(self):
        return self.calculer_age() > 10

Ford = Voiture("Ford", "Raptor Edition SVT", 2017, 60000)
Subaru = Voiture("Subaru", "WRX", 2019, 25000)
Brabus = Voiture("Brabus", "G Wagon", 2021, 10000)
Mercedes = Voiture("Mercedes", "Class GLE", 2022, 5000)
Porsche = Voiture("Porsche", "Cayenne Restylé", 2007, 145000)

voitures = [Ford, Subaru, Brabus, Mercedes, Porsche]

for voiture in voitures:
    voiture.afficher_details()
    print(f"Âge de la bagnole: {voiture.calculer_age()} ans")
    print(f"Est-elle vieille cette bagnole? {'Oui' if voiture.est_vieille() else 'Non'}\n")