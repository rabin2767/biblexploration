from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from logConnect import initializeLog
import dbSetupCache as cache
from dbConnect import connection, createDatabase


log = initializeLog("setup.log")

app = Flask(__name__)
bootstrap = Bootstrap(app)


@app.route('/setup')
def setup():
    log.debug("Database Setup Main")
    return render_template("index.html")


@app.route('/setup_continue')
def setup_continue():
    log.debug("Database Setup Continue")
    return render_template("setup.html")


@app.route('/initialize_db', methods=['POST'])
def initialize_db():
    log.debug("Saving details for database setup")
    cache.hostname = request.form['hostname']
    cache.username = request.form['username']
    cache.password = request.form['passcode']
    cache.database = request.form['database']
    return render_template("select_options.html")


@app.route('/select_lang', methods=['POST'])
def select_lang():
    log.debug("Saving details for languages")
    cache.language = request.form.getlist('language')

    createDatabase()

    return render_template("index.html")


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/select_lang')
def select_lang_render():
    return render_template("select_options.html")


if __name__ == '__main__':
    app.run(debug=True)
