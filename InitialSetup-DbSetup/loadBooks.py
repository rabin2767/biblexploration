from logConnect import initializeLog
from dbOps import insertIntoBooks, books, createDatabase
import requests
import booksDetails as book_details

log = initializeLog("loadbooks.log")

def getDataFromBibleApi(book_name, chapters):
    URL = "https://bible-api.com/" + book_name + " " + chapters
    r = requests.get(url=URL)
    data = r.json()
    for x in data['verses']:
        insertIntoBooks(book_name, data['translation_id'], data['translation_name'], x['book_id'],
                        x['book_name'], x['chapter'], x['verse'], x['text'])


for x in books:
    createDatabase()
    i = 1
    while i <= int(book_details.booksAndChapters[x]):
        print("Book :- " + x + " : " + str(i))
        log.info("Book :- " + x + " : " + str(i))
        getDataFromBibleApi(x, str(i))
        i += 1