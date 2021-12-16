class Patinoire:
    def __init__(self, id, nom, arrondissement, date_maj,
                 ouvert, deblaye, arrose, resurface):
        self.id = id
        self.nom = nom
        self.arrondissement = arrondissement
        self.date_maj = date_maj
        self.ouvert = ouvert
        self.deblaye = deblaye
        self.arrose = arrose
        self.resurface = resurface


    def as_dictionary(self):
        return {"id": self.id,
                "nom": self.nom,
                "arrondissement": self.arrondissement,
                "date_maj": self.date_maj,
                "ouvert": self.ouvert,
                "deblaye": self.deblaye,
                "arrose": self.arrose,
                "resurface": self.resurface}
