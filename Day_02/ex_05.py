class Personnage:
    
    def __init__(self, nom, points_de_vie, force):
        self.nom = nom
        self.points_de_vie = points_de_vie
        self.force = force
        
    def attaquer(self, autre_personnage):
        autre_personnage.points_de_vie -= self.force
        print(f"{self.nom} attaque {autre_personnage.nom} pour {self.force}.")
        print(f"{autre_personnage.nom} a maintenant {autre_personnage.points_de_vie} points de vie.")
        
class Guerrier(Personnage):
    
    def __init__(self, nom, points_de_vie, force):
        super().__init__(nom, points_de_vie, force)
        self.force += 14
    
class Mage(Personnage):
    
    def __init__(self, nom, points_de_vie, force):
        super().__init__(nom, points_de_vie, force)
        
    def lancer_sort(self, autre_personnage):
        sort_damage = 10
        autre_personnage.points_de_vie -= sort_damage
        print(f"{self.nom} lance un sort sur {autre_personnage.nom} lui assénant {sort_damage} points de dégâts!!!")
        print(f"{autre_personnage.nom} a maintenant {autre_personnage.points_de_vie} points de vie.")
            
class Combat:
    def _init_(self, personnage1, personnage2):
        self.personnage1 = personnage1
        self.personnage2 = personnage2
        
    def lancer_combat(self):
        print(f"LET'S THE BATTLE BEGIN BETWEEN {self.personnage1.nom} AND {self.personnage2.nom}!!!")
        while self.personnage1.points_de_vie > 0 and self.personnage2.points_de_vie > 0:
            self.personnage1.attaquer(self.personnage2)
            if self.personnage1.points_de_vie <= 0:
                print(f"{self.personnage2.nom} a gagné le combat!!!")
                break
            elif self.personnage2.points_de_vie <= 0:
                print(f"{self.personnage1.nom} a gagné le combat!!!")
                break

guerrier = Guerrier("Yami", 100, 15)
mage = Mage("Yuno", 80, 10)
                
combat = Combat(guerrier, mage)
combat.lancer_combat()