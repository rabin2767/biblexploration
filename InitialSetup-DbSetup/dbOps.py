from dbConnect import connection, createDatabase

createDatabase()
cn = connection()
cur = cn.cursor()


books = [
    "Genesis",
    "Exodus",
    "Leviticus",
    "Numbers",
    "Deuteronomy",
    "Joshua",
    "Judges",
    "Ruth",
    "1Samuel",
    "2Samuel",
    "1Kings",
    "2Kings",
    "1Chronicles",
    "2Chronicles",
    "Ezra",
    "Nehemiah",
    "Esther",
    "Job",
    "Psalms",
    "Proverbs",
    "Ecclesiastes",
    "SongOfSolomon",
    "Isaiah",
    "Jeremiah",
    "Lamentations",
    "Ezekiel",
    "Daniel",
    "Hosea",
    "Joel",
    "Amos",
    "Obadiah",
    "Jonah",
    "Micah",
    "Nahum",
    "Habakkuk",
    "Zephaniah",
    "Haggai",
    "Zechariah",
    "Malachi",
    "Matthew",
    "Mark",
    "Luke",
    "John",
    "Acts",
    "Romans",
    "1Corinthians",
    "2Corinthians",
    "Galatians",
    "Ephesians",
    "Philippians",
    "Colossians",
    "1Thessalonians",
    "2Thessalonians",
    "1Timothy",
    "2Timothy",
    "Titus",
    "Philemon",
    "Hebrews",
    "James",
    "1Peter",
    "2Peter",
    "1John",
    "2John",
    "3John",
    "Jude",
    "Revelation"
]


def createBibleBooks(books):
    cur.execute("CREATE TABLE IF NOT EXISTS " + books + " ("
                                                        "book_id VARCHAR(255), "
                                                        "book_name VARCHAR(255), "
                                                        "chapter VARCHAR(255), "
                                                        "verse VARCHAR(255), "
                                                        "text TEXT(65535))")


def dropBibleBooks(books):
    cur.execute("DROP TABLE " + books)


for x in books:
    createBibleBooks(x)

# for x in books:
#     dropBibleBooks(x)

def insertIntoBooks(book, book_id, book_name, chapter, verse, text):
    sql = "INSERT INTO " + book + "(book_id, book_name, chapter, verse, text) VALUES (%s, %s, %s, %s, %s)"
    val = (book_id, book_name, chapter, verse, text)
    cur.execute(sql, val)
    cn.commit()
