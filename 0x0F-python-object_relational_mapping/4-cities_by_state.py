#!/usr/bin/python3
# -*- coding: utf-8 -*-

import MySQLdb
from sys import argv
if __name__ == '__main__':

    db = MySQLdb.connect(host='localhost', port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])

    cur = db.cursor()

    cur.execute('select cities.id, cities.name,states.name from cities\
                 inner join states on cities.state_id = states.id order\
                 by cities.id asc '
                )

    list = cur.fetchall()
    for i in list:
        print(i)

    cur.close()
    db.close()
