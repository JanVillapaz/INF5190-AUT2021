"""
 Copyright 2021 Ela El-Heni
   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at
       http://www.apache.org/licenses/LICENSE-2.0
   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""
import smtplib
import xml.etree.ElementTree as ET
import csv
from datetime import date
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import requests
import yaml

import twitter
from database import Database
from create_table import db, Piscines
from twitter import send_tweet

get_db = Database()

piscines_url = "https://data.montreal.ca/dataset/4604afb7-a7c4-4626-a3ca-e136158133f2/resource/cbdca706-569e-4b4a-805d" \
               "-9af73af03b14/download/piscines.csv"
patinoire_url = "https://data.montreal.ca/dataset/225ac315-49fe-476f-95bd-a1ce1648a98c/resource/5d1859cc-2060-4def" \
                "-903f-db24408bacd0/download/l29-patinoire.xml"
glissade_url = "http://www2.ville.montreal.qc.ca/services_citoyens/pdf_transfert/L29_GLISSADE.xml"

file_name = "piscine.csv"
file_name2 = "patinoire.xml"
file_name3 = "glissade.xml"
new_piscine = []
new_glissade = []
new_patinoire = []


def retrieve_data(url, file):
    req = requests.get(url)
    url_content = req.content
    csv_file = open(file, 'wb')
    csv_file.write(url_content)
    csv_file.close()


def xml_patinoire_handler():
    retrieve_data(patinoire_url, file_name2)

    tree = ET.parse(file_name2)
    root = tree.getroot()

    for arrondissement in root.findall('arrondissement'):
        nom_arr = arrondissement.find('nom_arr').text.strip()
        for patinoire in arrondissement.findall('patinoire'):
            nom_pat = patinoire.find('nom_pat').text.strip()
            for condition in patinoire.findall('condition'):
                date_heure = condition.find('date_heure').text.strip()
                ouvert = condition.find('ouvert').text.strip()
                deblaye = condition.find('deblaye').text.strip()
                arrose = condition.find('arrose').text.strip()
                resurface = condition.find('resurface').text.strip()
            patin = [nom_pat, nom_arr, date_heure,
                     ouvert, deblaye, arrose, resurface]
        get_db.insert_patinoire(patin)


def xml_glissades_handler():
    retrieve_data(glissade_url, file_name3)

    tree = ET.parse(file_name3)
    root = tree.getroot()

    for glissade in root.findall('glissade'):
        nom = glissade.find('nom').text
        for arrondissement in glissade.findall('arrondissement'):
            nom_arr = arrondissement.find('nom_arr').text
            cle = arrondissement.find('cle').text
            date_maj = arrondissement.find('date_maj').text
        ouvert = glissade.find('ouvert').text
        deblaye = glissade.find('deblaye').text
        condition = glissade.find('condition').text

        gliss = [nom, nom_arr, cle, date_maj, ouvert, deblaye, condition]
        get_db.insert_glissade(gliss)


def csv_handler():
    retrieve_data(piscines_url, file_name)
    with open(file_name, newline='') as csvfile:
        reader = csv.reader(csvfile, skipinitialspace=True)
        next(reader, None)  # skips the header
        for row in reader:
            # recover variables + remove quotes
            id_ue = row[0].strip('"') if len(row[0].strip(
                ',')) != 0 else "N/A"
            type_piscine = row[1].strip('"') if len(row[1].strip(
                ',')) != 0 else "N/A"
            nom = row[2].strip('"') if len(row[2].strip(
                ',')) != 0 else "N/A"
            arrondissement = row[3].strip('"') if len(row[3].strip(
                ',')) != 0 else "N/A"
            adresse = row[4].strip('"') if len(row[4].strip(
                ',')) != 0 else "N/A"
            propriete = row[5].strip('"') if len(row[5].strip(
                ',')) != 0 else "N/A"
            gestion = row[6].strip('"') if len(row[6].strip(
                ',')) != 0 else "N/A"
            point_x = row[7].strip('"') if len(row[7].strip(
                ',')) != 0 else "N/A"
            point_y = row[8].strip('"') if len(row[8].strip(
                ',')) != 0 else "N/A"
            equipement = row[9].strip('"') if len(row[9].strip(
                ',')) != 0 else "N/A"
            long = row[10].strip('"') if len(row[10].strip(
                ',')) != 0 else "N/A"
            lat = row[11].strip(',') if len(row[11].strip(
                ',')) != 0 else "N/A"

            # Avoid duplicating insert
            verify_db = db.session.query(Piscines).filter_by(
                id_ue=id_ue,
                type_piscine=type_piscine,
                nom=nom,
                arrondissement=arrondissement,
                adresse=adresse,
                propriete=propriete,
                gestion=gestion,
                point_x=point_x, point_y=point_y,
                equipement=equipement,
                long=long, lat=lat).all()
            if len(verify_db) == 0:
                piscines = Piscines(id_ue=id_ue,
                                    type_piscine=type_piscine,
                                    nom=nom,
                                    arrondissement=arrondissement,
                                    adresse=adresse,
                                    propriete=propriete,
                                    gestion=gestion,
                                    point_x=point_x, point_y=point_y,
                                    equipement=equipement,
                                    long=long, lat=lat)
                db.session.add(piscines)
                db.session.commit()
                new_piscine.append(piscines)
            else:
                # print("Exists")
                pass
    csvfile.close()
    email_updates(new_piscine)
    send_tweet()


def email_updates(data):
    today = date.today().strftime("%Y/%m/%d")
    body = ' '.join(map(str, data))
    if len(body) == 0:
        body = "No new installations on : " + today
        subject = "No Updates: Ville de Montreal - Installations"
    else:
        body = "New installations added on : " + today
        subject = "Notice! Ville de Montreal - Installations"

    with open(r'emails.yaml') as file:
        user_list = yaml.load(file, Loader=yaml.FullLoader)
    source_address = "bj091047inf5190@gmail.com"
    password = "Jvillapaz123!"
    destination_address = user_list[0]['User']['Email']

    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = source_address
    msg['To'] = destination_address
    msg['ReplyTo'] = source_address

    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(source_address, password)
    text = msg.as_string()
    server.sendmail(source_address, destination_address, text)
    server.quit()


def data_handler():
    csv_handler()
    xml_patinoire_handler()
    xml_glissades_handler()


if __name__ == '__main__':
    data_handler()
