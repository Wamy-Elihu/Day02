class Reservation:
    
    def __init__(self, id, client, date, place):
        self.id = id
        self.client = client
        self.date = date
        self.place = place
        self.confirmee = False

    def confirmer(self):
        self.confirmee = True

class Client:
    
    def __init__(self, nom, email, reservations):
        self.nom = nom
        self.email = email
        self.reservations = []

    def effectuer_reservation(self, reservation):
        self.reservations.append(reservation)
        print(f"Réservation effectuée pour {self.nom}.")

class SystemeDeReservation:
    
    def __init__(self):
        self.reservations = []

    def ajouter_reservation(self, reservation):
        self.reservations.append(reservation)

    def annuler_reservation(self, reservation):
        if reservation in self.reservations:
            self.reservations.remove(reservation)
            print(f"Réservation {reservation.id} annulée.")

    def afficher_reservations(self):
        for reservation in self.reservations:
            statut = "confirmée" if reservation.confirmee else "en attente"
            print(f"Réservation {reservation.id} pour {reservation.client.nom} - {statut}")

client1 = Client("Lom-Roi", "om.vie@icloud.com")
reservation1 = Reservation(1, client1, "2025-04-20", "w4")

systeme = SystemeDeReservation()
systeme.ajouter_reservation(reservation1)

client1.effectuer_reservation(reservation1)
reservation1.confirmer()
systeme.afficher_reservations()