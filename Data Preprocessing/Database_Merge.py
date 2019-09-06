#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 16:41:57 2019

@author: miguelreyes
"""

import sqlite3

db1 = r"/Users/miguelreyes/Documents/Miguel Reyes/AKT/04 Semester/QU Projekt /MSD Dataset/Dataset/Match_Test/mxm_dataset.db"
db2 = r"/Users/miguelreyes/Documents/Miguel Reyes/AKT/04 Semester/QU Projekt /MSD Dataset/Dataset/Match_Test/tracks_per_year.db"

conn = sqlite3.connect(db1)
cursor = conn.cursor()
print("Opened database successfully")


for row in cursor.execute("SELECT track_id, word from LYRICS"):
    print("TRACK_ID = ", row[0])
    print("WORD = ", row[1], "\n")



conn.commit()
conn.close()