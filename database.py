import sqlite3

from installation import Installation
from patinoire import Patinoire
from piscine import Piscine
from glissade import Glissade


class Database:
    def __init__(self):
        self.connection = None

    def get_connection(self):
        if self.connection is None:
            self.connection = sqlite3.connect('db/db.db')
        return self.connection

    def disconnect(self):
        if self.connection is not None:
            self.connection.close()
            self.connection = None

    # Piscine
    def get_piscine(self):
        cursor = self.get_connection().cursor()
        cursor.execute("SELECT * FROM piscines")
        piscine = cursor.fetchall()
        return piscine

    def get_piscine_arr(self, arrondissement):
        connection = self.get_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM piscines WHERE arrondissement = ? COLLATE NOCASE;",
                       (arrondissement,))
        piscines = cursor.fetchall()
        return [Piscine(piscine[0], piscine[1], piscine[2], piscine[3], piscine[4], piscine[5], piscine[6], piscine[7],
                        piscine[8], piscine[9], piscine[10], piscine[11], piscine[12]
                        ) for piscine in piscines]

    # Patinoire
    def get_patinoire_arr(self, arrondissement):
        connection = self.get_connection()
        cursor = connection.cursor()
        cursor.execute(
            "SELECT * FROM patinoires "
            "WHERE arrondissement LIKE ? COLLATE NOCASE;",
            ("%" + arrondissement + "%",))
        patinoires = cursor.fetchall()
        return [Patinoire(patinoire[0], patinoire[1], patinoire[2],
                          patinoire[3], patinoire[4], patinoire[5],
                          patinoire[6], patinoire[7]) for patinoire in patinoires]

    def insert_patinoire(self, row):
        connection = self.get_connection()
        cursor = connection.cursor()
        cursor.execute("INSERT INTO patinoires (nom, arrondissement, date_maj, ouvert, deblaye, arrose,"
                       " resurface) VALUES (?,?,?,?,?,?,?);",
                       (row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
        connection.commit()

    def get_patinoire_maj_2021(self):
        connection = self.get_connection()
        cursor = connection.cursor()
        cursor.execute(
            "SELECT * FROM patinoires WHERE date_maj LIKE '%2021%' ORDER BY nom;")
        patinoires = cursor.fetchall()
        return [Glissade(patinoire[0], patinoire[1], patinoire[2],
                         patinoire[3], patinoire[4], patinoire[5],
                         patinoire[6], patinoire[7]) for patinoire in patinoires]

    # Retrieve glissade by district
    def get_glissade_arr(self, arrondissement):
        connection = self.get_connection()
        cursor = connection.cursor()
        cursor.execute(
            "SELECT * FROM glissades "
            "WHERE arrondissement LIKE ? COLLATE NOCASE;",
            ("%" + arrondissement + "%",))
        glissades = cursor.fetchall()
        return [Glissade(glissade[0], glissade[1], glissade[2],
                         glissade[3], glissade[4], glissade[5],
                         glissade[6], glissade[7]) for glissade in glissades]

    # Insert xml data into table
    def insert_glissade(self, row):
        connection = self.get_connection()
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO glissades (nom, arrondissement, cle, date_maj, "
            "ouvert, deblaye, condition) VALUES (?, ?, ?, ?, ?, ?, ?);",
            (row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
        connection.commit()

    #  Glissade updated in 2021
    def get_glissade_maj_2021(self):
        connection = self.get_connection()
        cursor = connection.cursor()
        cursor.execute(
            "SELECT * FROM glissades WHERE date_maj LIKE '%2021%' ORDER BY nom;")
        glissades = cursor.fetchall()
        return [Glissade(glissade[0], glissade[1], glissade[2],
                         glissade[3], glissade[4], glissade[5],
                         glissade[6], glissade[7]) for glissade in glissades]

    # Retrieve installations by name
    def get_installation_name(self, nom):
        connection = self.get_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT id, nom, arrondissement FROM piscines WHERE nom=?"
                       "UNION SELECT id, nom, arrondissement FROM glissades WHERE nom=?"
                       "UNION SELECT id, nom, arrondissement FROM patinoires WHERE nom=?;",
                       (nom, nom, nom,))
        installations = cursor.fetchall()
        return [Installation(installation[0], installation[1], installation[2]) for installation in installations]

    def installation_maj_2021(self):
        connection = self.get_connection()
        cursor = connection.cursor()
        cursor.execute(
            "SELECT id, nom, nom_arrondissement FROM patinoires "
            "WHERE date_maj LIKE '%2021%' "
            "UNION SELECT id, nom, nom_arrondissement FROM glissades "
            "WHERE date_maj_arrondissement LIKE '%2021%' "
            "ORDER BY nom;")
        installations = cursor.fetchall()
        return [Installation(installation[0], installation[1], installation[2])
                for installation in installations]

    # retrieve all name of installations
    def get_name(self):
        connection = self.get_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT nom FROM piscines UNION "
                       "SELECT nom FROM glissades UNION "
                       "SELECT nom FROM patinoires "
                       "ORDER BY nom;")
        noms = cursor.fetchall()
        return [nom[0] for nom in noms]
