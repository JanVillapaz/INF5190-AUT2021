import dicttoxml
from flask import Flask, request, jsonify
from flask import g
from flask import render_template
from apscheduler.schedulers.background import BackgroundScheduler
from flask_json_schema import JsonSchema
import pandas as pd
from database import Database
from manage import data_handler
import atexit


app = Flask(__name__)

# A1 + A2
sched = BackgroundScheduler({'apscheduler.timezone': 'Canada/Eastern'}, daemon=True)
sched.add_job(data_handler, 'cron', hour='0')
sched.start()
atexit.register(lambda: sched.shutdown())

app.config['JSON_AS_ASCII'] = False
schema = JsonSchema(app)


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        g._database = Database()
    return g._database


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.disconnect()


@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404


@app.errorhandler(500)
def page_not_found(error):
    return render_template("500.html"), 500


@app.route('/')
def index_page():
    names = get_db().get_name()
    return render_template("index.html", installation_names=names)


@app.route('/doc')
def doc_page():
    return render_template("documentation.html");


# A4
@app.route('/api/installations', methods=['GET'])
def list_installation_arr():
    arrondissement = request.args.get('arrondissement')
    piscines = get_db().get_piscine_arr(arrondissement)
    patinoires = get_db().get_patinoire_arr(arrondissement)
    glissades = get_db().get_glissade_arr(arrondissement)

    dict_piscines = [
        installation.as_dictionary() for installation in piscines]
    dict_patinoires = [
        installation.as_dictionary() for installation in patinoires]
    dict_glissades = [
        installation.as_dictionary() for installation in glissades]

    return jsonify([dict_piscines + dict_patinoires + dict_glissades])


# A6
@app.route('/api/installations-name', methods=['GET'])
def list_installation_name():
    nom = request.args.get('nom')
    installations = get_db().get_installation_name(nom)

    dict_installations = [
        installation.as_dictionary() for installation in installations]

    if len(dict_installations) == 0:
        error = "Invalid Selection"
        return render_template("404.html", error=error), 404

    return jsonify([dict_installations])


# C1
@app.route('/api/installation/date/2021', methods=["GET"])
def mise_a_jour_2021():
    glissades = get_db().get_glissade_maj_2021()
    patinoires = get_db().get_patinoire_maj_2021()

    dict_glissades = [
        installation.as_dictionary() for installation in glissades]
    dict_patinoires = [
        installation.as_dictionary() for installation in patinoires]

    if len(dict_glissades) == 0 and len(dict_patinoires) == 0:
        error = "No result."
        return render_template("404.html", error=error), 404

    return jsonify([dict_glissades + dict_patinoires])


# C2
@app.route('/api/installation/date/2021/XML', methods=["GET"])
def generate_xml():
    glissades = get_db().get_glissade_maj_2021()
    patinoires = get_db().get_patinoire_maj_2021()

    dict_glissades = [
        installation.as_dictionary() for installation in glissades]
    dict_patinoires = [
        installation.as_dictionary() for installation in patinoires]

    if len(dict_glissades) == 0 and len(dict_patinoires) == 0:
        return render_template("404.html"), 404

    xml = dicttoxml.dicttoxml(dict_glissades + dict_patinoires)
    return xml


# C3
@app.route('/api/installation/date/2021/CSV', methods=["GET"])
def generate_csv():
    glissades = get_db().get_glissade_maj_2021()
    patinoires = get_db().get_patinoire_maj_2021()

    dict_glissades = [
        installation.as_dictionary() for installation in glissades]
    dict_patinoires = [
        installation.as_dictionary() for installation in patinoires]

    df = pd.DataFrame(dict_glissades + dict_patinoires)
    csv = df.to_csv('installation_maj_2021.csv', encoding='utf-8-sig')

    return csv


if __name__ == '__main__':
    app.run()
