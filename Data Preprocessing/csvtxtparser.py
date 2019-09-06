#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 19:45:20 2019

@author: miguelreyes
"""

from os import listdir
import pandas as pd

def find_csv_filenames( path_to_dir, suffix=".csv" ):
    filenames = listdir(path_to_dir)
    return [ filename for filename in filenames if filename.endswith( suffix ) ]

filenames = find_csv_filenames("/Users/miguelreyes/Documents/Miguel Reyes/AKT/04 Semester/QU Projekt /MSD Dataset/Dataset")

for name in filenames:
  print (name)
  #We read the database coming from the kaggle project https://www.kaggle.com/rakannimer/billboard-lyrics
  
  
Pd_song_read= pd.read_csv(name)  

print(Pd_song_read)
lyrics = Pd_song_read['lyrics'].astype('str')

for columna in lyrics:
 print(lyrics[columna])


direccion=name+str(column)

#print(name)
print(column)

