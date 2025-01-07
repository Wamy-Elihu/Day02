class Voiture:
    
    def __init__(self, marque, modele, annee, kilometrage):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.kilometrage = kilometrage

    def afficher_details(self):
        print(f"Marque: {self.marque}")
        print(f"Modèle: {self.modele}")
        print(f"Année: {self.annee}")
        print(f"Kilométrage: {self.kilometrage} km")

    def augmenter_kilometrage(self, kilometres):
        if kilometres > 0:
            self.kilometrage += kilometres
        else:
            print("Il doit être supérieur à 0.")

Ford = Voiture("Ford", "Raptor Edition SVT", 2017, 60000)
Subaru = Voiture("Subaru", "WRX", 2019, 25000)
Brabus = Voiture("Brabus", "G Wagon", 2021, 10000)
Mercedes = Voiture("Mercedes", "Class GLE", 2022, 5000)

Ford.afficher_details()
Subaru.afficher_details()
Brabus.afficher_details()
Mercedes.afficher_details()

Ford.augmenter_kilometrage(2000)
Subaru.augmenter_kilometrage(3000)
Brabus.augmenter_kilometrage(1500)
Mercedes.augmenter_kilometrage(1000)

print("\nAprès augmentation du kilométrage :")
Ford.afficher_details()
Subaru.afficher_details()
Brabus.afficher_details()
Mercedes.afficher_details()