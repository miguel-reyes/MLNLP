#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 09:39:05 2019

@author: miguelreyes
"""

import csv


#root = tk.Tk()
#root.withdraw()

#file_path = filedialog.askopenfilename()


csv_dict = {}
filename='out_2009-2010.csv'
filename2='slice_'+filename
print(filename2)

fields = ['track_id', 'mxm_tid', 'word','count','is_test','track_id:1','Year','Artist','Song']
fields2 = ['track_id2', 'mxm_tid2', 'lyrics','Year2','Artist2','Song2']

#f = open('summary1920.csv', 'w')

with open(filename2, mode='w') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=fields2)
    writer.writeheader()
    
    with open(filename, "r") as csvfile:
        
        reader = csv.DictReader(csvfile,fieldnames=fields)
        header = next(reader)

# We get the first ID in the list 
        count=0
        for row in reader:
           count = count+1
           if count == 2:
               buffertrack_id = row['track_id']
#               print("The first element in the list is: ", buffertrack_id)
#               buffertrack_id = ''
               count = 0
               buffer=''
               break


    with open(filename, "r") as csvfile:
        
        reader = csv.DictReader(csvfile,fieldnames=fields)
        header = next(reader)

        
           
#Scanning the csv        
        for row in reader:
            
            words = row['word']#assign the word to the variable words
            repetitions = int(row['count'])#get the number of repetitions        
            ID_Song=row['track_id']#get current track_id
            
                
#            print("el valor de track_id es ",row ['track_id'])
#            print("el valor del buffer es ",buffertrack_id)

#Getting a variable that shows all the times that the word is repeated


            
            if buffertrack_id != row['track_id']:
                print("Creating entry in file for Track_ID:",buffertrack_id)
                buffer = buffer[:-1]
                writer.writerow({'track_id2':buffertrack_id, 'mxm_tid2':buffermxm_tid, 'lyrics':buffer,'Year2':bufferYear,'Artist2':bufferArtist,'Song2':bufferSong})
 #               print(buffer)
 #               print("inicia una nueva canción")
                
                buffer=''

            for a in range(repetitions):
    
                    buffer2=words+' '+buffer
                    buffer=buffer2
#                    print("Buffer es: ",buffer)
#                    print("Buffer2 es: ",buffer2)

                
            buffertrack_id=row['track_id']
            buffermxm_tid = row['mxm_tid']
            bufferYear = row['Year']
            bufferArtist = row['Artist']
            bufferSong = row['Song']
            
        print("Creating entry in file for Track_ID:",buffertrack_id)
        buffer = buffer[:-1]
        writer.writerow({'track_id2':row['track_id'], 'mxm_tid2':row['mxm_tid'], 'lyrics':buffer,'Year2':row['Year'],'Artist2':row['Artist'],'Song2':row['Song']})            
#        print(buffer)
#        print("canción final")

 #           print(buffer)
