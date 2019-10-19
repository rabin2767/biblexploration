from logConnect import initializeLog
from dbOps import insertIntoBooks, books, createDatabase
import requests

log = initializeLog("loadbooks.log")

booksAndChapters = {
    "Genesis": "50",
    "Exodus": "40",
    "Leviticus": "27",
    "Numbers": "36",
    "Deuteronomy": "34",
    "Joshua": "24",
    "Judges": "21",
    "Ruth": "4",
    "1Samuel": "31",
    "2Samuel": "24",
    "1Kings": "22",
    "2Kings": "25",
    "1Chronicles": "29",
    "2Chronicles": "36",
    "Ezra": "10",
    "Nehemiah": "13",
    "Esther": "10",
    "Job": "42",
    "Psalms": "150",
    "Proverbs": "31",
    "Ecclesiastes": "12",
    "SongOfSolomon": "8",
    "Isaiah": "66",
    "Jeremiah": "52",
    "Lamentations": "5",
    "Ezekiel": "48",
    "Daniel": "12",
    "Hosea": "14",
    "Joel": "3",
    "Amos": "9",
    "Obadiah": "1",
    "Jonah": "4",
    "Micah": "7",
    "Nahum": "3",
    "Habakkuk": "3",
    "Zephaniah": "3",
    "Haggai": "2",
    "Zechariah": "14",
    "Malachi": "4",
    "Matthew": "28",
    "Mark": "16",
    "Luke": "24",
    "John": "21",
    "Acts": "28",
    "Romans": "16",
    "1Corinthians": "16",
    "2Corinthians": "13",
    "Galatians": "6",
    "Ephesians": "6",
    "Philippians": "4",
    "Colossians": "4",
    "1Thessalonians": "5",
    "2Thessalonians": "3",
    "1Timothy": "6",
    "2Timothy": "4",
    "Titus": "3",
    "Philemon": "1",
    "Hebrews": "13",
    "James": "5",
    "1Peter": "5",
    "2Peter": "3",
    "1John": "5",
    "2John": "1",
    "3John": "1",
    "Jude": "1",
    "Revelation": "22"
}


def getDataFromBibleApi(book_name, chapters):
    URL = "https://bible-api.com/" + book_name + " " + chapters

    r = requests.get(url=URL)

    data = r.json()

    for x in data['verses']:
        insertIntoBooks(book_name, x['book_id'], x['book_name'], x['chapter'], x['verse'], x['text'])


for x in books:
    createDatabase()
    i = 1
    while i <= int(booksAndChapters[x]):
        print("Book :- " + x + " : " + str(i))
        log.info("Book :- " + x + " : " + str(i))
        getDataFromBibleApi(x, str(i))
        i += 1
