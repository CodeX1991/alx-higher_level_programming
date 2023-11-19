#!/usr/bin/python3
"""
A script that lists all states with a name
starting with N from the database hbtn_0e_0_usa
"""
import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    Acessing the database to get all states
    """

    db = MySQLdb.connect(host="localhost", user=argv[1],
                         port=3306, passwd=argv[2], db=argv[3])

    cur = db.cursor()
    cur.execute("SELECT * FROM states \
            WHERE name LIKE BINARY %(name)s \
            ORDER BY states.id", {'name': argv[4]})
    rows = cur.fetchall()
    for row in rows:
        print(row)
