import mysql.connector as connector
from logConnect import initializeLog
import dbSetupCache as cache

log = initializeLog("oneTimeSetup.log")

config = {
    "host": cache.hostname,
    "user": cache.username,
    "passwd": cache.password,
    "database": cache.database,
    "auth_plugin": "mysql_native_password"
}

configToCreateDb = {
    "host": cache.hostname,
    "user": cache.username,
    "password": cache.password
}


def connection():
    log.debug("Initializing MySQL connection.")
    try:
        c = connector.connect(**config)
        log.debug("Connection to MySql successful")
        return c
    except Exception as e:
        log.debug("Connection to MySql unsuccessful")
        print(e)
        exit("Could not connect to MySQL. Check if MySQL server is running")


def createDatabase():
    log.debug(cache.hostname + "," + cache.username + "," + cache.password + "," + cache.database)
    log.debug("Create Database " + cache.database)
    c = connector.connect(**configToCreateDb)
    cur = c.cursor()
    sql = "CREATE DATABASE IF NOT EXISTS " + cache.database
    cur.execute(sql)
    c.commit()

