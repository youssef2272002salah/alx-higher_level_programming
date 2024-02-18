#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb
from sys import argv
if __name__ == '__main__':

    db = MySQLdb.connect(host='localhost', port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])

    cur = db.cursor()
    query = \
        'select cities.id, cities.name from \
            cities inner join states on \
                cities.state_id = states.id \
                    where states.name = %s'
    cur.execute(query, (argv[4], ))

    rows = cur.fetchall()
    j = []
    for i in rows:
        j.append(i[1])
    print(', '.join(j))

    cur.close()
    db.close()
