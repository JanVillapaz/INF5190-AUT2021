CREATE TABLE piscines
(
    ID           INTEGER PRIMARY KEY AUTOINCREMENT,
    ID_UE           INTEGER,
    TYPE_PISCINE    VARCHAR,
    NOM             VARCHAR,
    ARRONDISSEMENT  VARCHAR,
    ADRESSE         VARCHAR,
    PROPRIETE       VARCHAR,
    GESTION         VARCHAR,
    POINT_X         REAL,
    POINT_Y         REAL,
    EQUIPEMENT      VARCHAR,
    LONG            REAL,
    LAT             REAL
);

CREATE TABLE glissades
(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    NOM VARCHAR,
    ARRONDISSEMENT VARCHAR,
    CLE VARCHAR,
    DATE_MAJ VARCHAR,
    OUVERT INTEGER(1),
    DEBLAYE INTEGER(1),
    CONDITION VARCHAR
);

CREATE TABLE patinoires
(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    NOM VARCHAR,
    ARRONDISSEMENT VARCHAR,
    DATE_MAJ VARCHAR,
    OUVERT INTEGER(1),
    DEBLAYE INTEGER(1),
    ARROSE INTEGER(1),
    RESURFACE INTEGER(1)
);