import mysql.connector as connector
from logConnect import initializeLog
import dbSetupCache as cache

log = initializeLog("oneTimeSetup.log")

hostName = cache.hostname
userName = cache.username
password = cache.password
databaseName = cache.database
config = {
    "host": hostName,
    "user": userName,
    "passwd": password,
    "database": databaseName,
    "auth_plugin": "mysql_native_password"
}

configToCreateDb = {
    "host": hostName,
    "user": userName,
    "passwd": password,
    "auth_plugin": "mysql_native_password"
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
    log.debug("Create Database " + databaseName)
    c = connector.connect(**configToCreateDb)
    cur = c.cursor()
    sql = "CREATE DATABASE IF NOT EXISTS " + databaseName
    cur.execute(sql)
    c.commit()

