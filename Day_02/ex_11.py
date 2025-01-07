from datetime import datetime

class Message:
    
    def __init__(self, expediteur, destinataire, contenu, date_envoi):
        self.expediteur = expediteur
        self.destinataire = destinataire
        self.contenu = contenu
        self.date_envoi = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def afficher_message(self):
        print(f"De: {self.expediteur} | À: {self.destinataire} | Date: {self.date_envoi}")
        print(f"Contenu: {self.contenu}")

class Utilisateur:
    
    def __init__(self, nom, messages_envoyes, mesages_recus):
        self.nom = nom
        self.messages_envoyes = []
        self.messages_recus = []

    def envoyer_message(self, destinataire, contenu):
        message = Message(self.nom, destinataire.nom, contenu)
        self.messages_envoyes.append(message)
        destinataire.messages_recus.append(message)
        
        print(f"Message envoyé de {self.nom} à {destinataire.nom}.")

    def lire_boite_reception(self):
        for message in self.messages_recus:
            message.afficher_message()

utilisateur1 = Utilisateur("Malyck")
utilisateur2 = Utilisateur("Nolan")

utilisateur1.envoyer_message(utilisateur2, "Bonjour Nolan! Comment vas-tu?")
utilisateur2.envoyer_message(utilisateur1, "Salut Malyck! Je vais bien, merci. Et toi?")

utilisateur1.lire_boite_reception()
utilisateur2.lire_boite_reception()