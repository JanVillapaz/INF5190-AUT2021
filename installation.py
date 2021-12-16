class Installation:

    def __init__(self, id, nom, arrondissement):
        self.id = id
        self.nom = nom
        self.arrondissement = arrondissement


    def as_dictionary(self):
        return {"id": self.id,
                "nom": self.nom,
                "arrondissement": self.arrondissement}
