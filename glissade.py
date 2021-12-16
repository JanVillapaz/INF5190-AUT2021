class Glissade:
    def __init__(self, id, nom, arrondissement, cle, date_maj,
                 ouvert, deblaye, condition):
        self.id = id
        self.nom = nom
        self.arrondissement = arrondissement
        self.cle = cle
        self.date_maj = date_maj
        self.ouvert = ouvert
        self.deblaye = deblaye
        self.condition = condition



    def as_dictionary(self):
        return {"id": self.id,
                "nom": self.nom,
                "arrondissement": self.arrondissement,
                "cle": self.cle,
                "date_maj": self.date_maj,
                "ouvert": self.ouvert,
                "deblaye": self.deblaye,
                "condition": self.condition}