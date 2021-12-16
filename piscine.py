class Piscine:
    def __init__(self, id, id_ue, type_piscine,
                 nom, arrondissement, adresse,
                 propriete, gestion, point_x, point_y,
                 equipement, long, lat):
        self.id = id
        self.id_ue = id_ue
        self.type_piscine = type_piscine
        self.nom = nom
        self.arrondissement = arrondissement
        self.adresse = adresse
        self.propriete = propriete
        self.gestion = gestion
        self.point_x = point_x
        self.point_y = point_y
        self.equipement = equipement
        self.long = long
        self.lat = lat

    def as_dictionary(self):
        return {"id": self.id, "id_ue": self.id_ue,
                "type_piscine": self.type_piscine,
                "nom": self.nom,
                "arrondissement": self.arrondissement,
                "adresse": self.adresse,
                "propriete": self.propriete,
                "gestion": self.gestion,
                "point_x": self.point_x, "point_y": self.point_y,
                "equipement": self.equipement,
                "long": self.long, "lat": self.lat}
