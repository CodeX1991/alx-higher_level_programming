#!/usr/bin/python3
"""
A script that lists all cities of a state
from the database hbtn_0e_0_usa
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
    cur.execute("""SELECT cities.id, cities.name \
            FROM cities \
            JOIN states \
            ON cities.state_id = states.id \
            WHERE states.name LIKE BINARY %(name)s \
            ORDER BY cities.id""", {'name': argv[4]})
    rows = cur.fetchall()

    if rows is not None:
        print(", ".join([row[1] for row in rows]))
