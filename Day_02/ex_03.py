class Animal:
    
    def __init__(self, nom, espece):
        self.nom = nom
        self.espece = espece
        
    def parler(self):
        return "Je suis un animal"

class Chien(Animal):
    def __init__(self, nom):
        super().__init__(nom, "Chien")
        
    def parler(self):
        return "Wouf ! Je suis un chien"

class Chat(Animal):
    def __init__(self, nom):
        super().__init__(nom, "Chat")
        
    def parler(self):
        return "Miaou ! Je suis un chat"
    
class Zoo:
    def __init__(self):
        self.animal = []
        
    def ajouter_animal(self, animal):
        self.animal.append(animal)
        
    def faire_parler_tout_le_monde(self):
        for animal in self.animal:
            print(f"{animal.nom} ({animal.espece}) dit : {animal.parler()}")
            
zoo = Zoo()
zoo.ajouter_animal(Chien("Browly"))
zoo.ajouter_animal(Chat("Praline"))
zoo.ajouter_animal(Chien("Dooglas"))
zoo.ajouter_animal(Chat("Mimosa"))

zoo.faire_parler_tout_le_monde()