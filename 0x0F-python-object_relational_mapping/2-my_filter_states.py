#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb
from sys import argv

if __name__ == '__main__':
    db = MySQLdb.connect(host='localhost', port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    cur = db.cursor()
    query = 'SELECT * FROM states WHERE name = %s'
    cur.execute(query, (argv[4], ))
    list = cur.fetchall()
    for i in list:
        print(i)
    cur.close()
    db.close()
