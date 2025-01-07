from abc import ABC, abstractmethod

class Employe(ABC):
    
    def __init__(self, nom, salaire_base):
        self.nom = nom
        self.salaire_base = salaire_base

    @abstractmethod
    def calculer_salaire(self):
        pass

class EmployeMensuel(Employe):
    
    def calculer_salaire(self):
        return self.salaire_base

class EmployeHoraire(Employe):
    
    def __init__(self, nom, salaire_base, heures_travaillees):
        super().__init__(nom, salaire_base)
        self.heures_travaillees = heures_travaillees

    def calculer_salaire(self):
        return self.salaire_base * self.heures_travaillees

class Entreprise:
    
    def __init__(self):
        self.employes = []

    def ajouter_employe(self, employe):
        self.employes.append(employe)

    def calculer_masse_salariale(self):
        total = sum(employe.calculer_salaire() for employe in self.employes)
        print(f"Masse salariale totale: {total}")

entreprise = Entreprise()

employe1 = EmployeMensuel("Albert", 3000)
employe2 = EmployeHoraire("Marie-Jolie", 20, 160)

entreprise.ajouter_employe(employe1)
entreprise.ajouter_employe(employe2)
entreprise.calculer_masse_salariale()