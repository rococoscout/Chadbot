# Form to handle logging into the MySQL db
# Gregory Polmatier

import pymysql

# Open database connection and return cursor and connection object
def connection():
    db = pymysql.connect(host="midn.cs.usna.edu",
                         user = "m215394",
                         passwd = "greg1018",
                         db = "m215394")
    cursor = db.cursor()
    return cursor, db
