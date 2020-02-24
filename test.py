#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mysql.connector
import sys

sql_create = """
CREATE TABLE IF NOT EXISTS Produit ( 
   ref INT(6) NOT NULL, 
   nom VARCHAR(100) DEFAULT NULL, 
   stock INT(4) DEFAULT NULL, 
   prix FLOAT(5,2) DEFAULT NULL, 
   PRIMARY KEY(ref), 
   CHECK (stock>=0) ); """

try:
    conn = mysql.connector.connect(host="",
                                   user="", password="",
                                   database="")

    cursor = conn.cursor()
    cursor.execute(sql_create)

    try:
        reference = (321451, "Truffe au chocolat 500g", 20, 7.2)
        cursor.execute("""INSERT INTO Produits (ref, nom, stock, prix) VALUES(%s, %s, %s, %s)""", reference)

        conn.commit()

    except:
        conn.rollback()

    cursor.execute("""SELECT ref, nom, prix FROM Produits WHERE stock > %s """, (0,))
    rows = cursor.fetchall()
    for row in rows:
        print('{0} : {1} - {2}'.format(row[0], row[1], row[2]))


except mysql.connector.errors.InterfaceError as e:
    print("Error %d: %s" % (e.args[0], e.args[1]))
    sys.exit(1)


finally:
    if conn:
        conn.close()
