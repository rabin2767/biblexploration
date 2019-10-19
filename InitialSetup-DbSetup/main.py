from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from logConnect import initializeLog
import dbSetupCache as cache

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
    log.debug(cache.hostname)
    return "terst"


@app.route('/')
def index():
    return "Rabin"


if __name__ == '__main__':
    app.run(debug=True)
