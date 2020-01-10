from dbConnect import connection, createDatabase
import booksDetails as book_details

cn = connection()
cur = cn.cursor()


def createBibleBooks(books):
    cur.execute("CREATE TABLE IF NOT EXISTS " + books + " ("
                                                        "translation_id VARCHAR(255),"
                                                        "translation_name VARCHAR(255),"
                                                        "book_id VARCHAR(255), "
                                                        "book_name VARCHAR(255), "
                                                        "chapter VARCHAR(255), "
                                                        "verse VARCHAR(255), "
                                                        "text TEXT(65535))")


def dropBibleBooks(books):
    cur.execute("DROP TABLE " + books)


for x in book_details.books:
    createBibleBooks(x)

# for x in books:
#     dropBibleBooks(x)


def insertIntoBooks(book, translation_id, translation_name, book_id, book_name, chapter, verse, text):
    sql = "INSERT INTO " + book + "(translation_id, translation_name, book_id, book_name, chapter, verse, text) " \
                                  "VALUES (%s, %s, %s, %s, %s, %s, %s)"
    val = (translation_id, translation_name, book_id, book_name, chapter, verse, text)
    cur.execute(sql, val)
    cn.commit()
