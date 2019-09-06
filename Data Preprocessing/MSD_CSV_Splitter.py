#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 21:23:58 2019

@author: miguelreyes
"""

import csv
import sqlite3

conn = sqlite3.connect('merged_mxm_year_one_table_final.db')
c = conn.cursor()

#def create_table():
 #   c.execute("CREATE TABLE IF NOT EXISTS stuffToPlot(unix REAL, datestamp TEXT, keyword TEXT, value REAL)")


#def data_entry():
#    c.execute("INSERT INTO stuffToPlot VALUES(1452549219,'2016-01-11 13:53:39','Python',6)")
    
#    conn.commit()
#    c.close()
#    conn.close()

#def dynamic_data_entry():

#    unix = int(time.time())
#    date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
#    keyword = 'Python'
#    value = random.randrange(0,10)

#    c.execute("INSERT INTO stuffToPlot (unix, datestamp, keyword, value) VALUES (?, ?, ?, ?)",
#          (unix, date, keyword, value))

#    conn.commit()
#    time.sleep(1)
 
 
def add_tfidf():
     # Add a new column to student table

    addColumn = "ALTER TABLE merged_mxm_year_one_table ADD COLUMN tfidf DECIMAL"
    c.execute(addColumn)
    
def delete_from_db():
    #Deletes the rows with no year information
    sql = 'DELETE FROM merged_mxm_year_one_table WHERE track_id is NULL'
    c.execute(sql)
    #Deletes the rows with the main non-english words found in the database
    sql_command2 = """delete from merged_mxm_year_one_table where track_id in (select distinct track_id from merged_mxm_year_one_table where word is "sur" or word is "quiero" or word is "tu" or word is "se" or word is "mi" or word is "es" or word is "le" or word is "ich" or word is "du" or word is "si" or word is "und" or word is "je" or word is "et" or word is "amor" or word is "una" or word is "pas" or word is "ma" or word is "nicht" or word is "das" or word is "ist" or word is "cest" or word is "ne" or word is "vida" or word is "eu" or word is "zu" or word is "esta" or word is "wir" or word is "ja" or word is "mir" or word is "dich" or word is "um" or word is "au" or word is "jag" or word is "nos" or word is "nos" or word is "pero" or word is "auf" or word is "não" or word is "moi" or word is "une" or word is "é" or word is "sur" or word is "mein");"""
    c.execute(sql_command2)
    conn.commit()

def prueba():
    unavar = 'i'
    c.execute("Select count (track_id) from merged_mxm_year_one_table WHERE year between ? and ? and word is ?",(1920,1925,unavar))
    data = c.fetchall()
    print(data)
    
def tfidf_calc():
    #c.execute("Select count (track_id) from merged_mxm_year_one_table WHERE year between 1920 and 1925")
    c.execute("Select * from merged_mxm_year_one_table WHERE year between 1920 and 1925")
    data = c.fetchall()
    datas = data
#    print(data)
#    print("fin de uno")
#    print (datas)

    for row in data:
        count=0
        palabra = row[2]
        for rows in datas:
            palabras = rows[2]
#            print("entra a for 2")
            if palabra == palabras:
                count=count+1
                print (palabras)
                print (palabra)
                print("entra a if - match!")


#        print(palabra)
        print (count)
        if count > 1:c.execute('UPDATE merged_mxm_year_one_table SET tfidf = ? WHERE word = ?',(count, palabra))
    conn.commit()
    
def tfidf_calc2():
    
    c.execute("Select * from merged_mxm_year_one_table WHERE year between 1920 and 1925")
    data = c.fetchall()
#    print(data)
#    print("termina uno /n")
    for row in data:
        palabra=row[2] 
        c.execute("select count (track_id) where word is 'near'")
        print("termina uno /n")
        print(palabra)
    
#    with open("out_1920-1925.csv", "w", newline='') as csv_file:  # Python 3 version    
#        csv_writer = csv.writer(csv_file)
#        csv_writer.writerow([i[0] for i in c.description]) # write headers
#        csv_writer.writerows(data)    
    
def slice_db():
#    year_list_start=(1921,1926,1931,1936,1941,1946,1951,1953,1955,1957,1959,1961,1963,1965,1967,1969,1971,1973,1975,1977,1979,1981,1983,1985, 1987, 1989, 1991, 1993, 1995, 1997, 1999, 2001, 2003, 2005, 2007, 2009)
#    year_list_end=(1925,1930,1935,1940,1945,1950,1952,1954,1956,1958,1960,1962,1964,1966,1968,1970,1972,1974,1976,1978,1980,1982,1984,1986,1988,1990,1992,1994,1996,1998,2000,2002,2004,2006,2008,2010)
    #sql_command = 'select * from merged_mxm_year_one_table WHERE track_id is NULL'


    c.execute("Select * from merged_mxm_year_one_table WHERE year between 1920 and 1925")
    data = c.fetchall()
#    print(data)
#    print("termina uno /n")
    
    with open("out_1920-1925.csv", "w", newline='') as csv_file:  # Python 3 version    
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow([i[0] for i in c.description]) # write headers
        csv_writer.writerows(data)
    
    
    c.execute("Select * from merged_mxm_year_one_table WHERE year between 1926 and 1930;")
    data = c.fetchall()
#    print(data)
#    print("termina uno /n")
    with open("out_1926-1930.csv", "w", newline='') as csv_file:  # Python 3 version    
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow([i[0] for i in c.description]) # write headers
        csv_writer.writerows(data)
        
            
    c.execute("Select * from merged_mxm_year_one_table WHERE year between 1931 and 1935;")
    data = c.fetchall()
#    print(data)
#    print("termina uno /n")
    with open("out_1931-1935.csv", "w", newline='') as csv_file:  # Python 3 version    
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow([i[0] for i in c.description]) # write headers
        csv_writer.writerows(data)
        
            
    c.execute("Select * from merged_mxm_year_one_table WHERE year between 1936 and 1940;")
    data = c.fetchall()
#    print(data)
#    print("termina uno /n")
    with open("out_1936-1940.csv", "w", newline='') as csv_file:  # Python 3 version    
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow([i[0] for i in c.description]) # write headers
        csv_writer.writerows(data)
        
            
    c.execute("Select * from merged_mxm_year_one_table WHERE year between 1941 and 1945;")
    data = c.fetchall()
#    print(data)
#    print("termina uno /n")
    with open("out_1941-1945.csv", "w", newline='') as csv_file:  # Python 3 version    
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow([i[0] for i in c.description]) # write headers
        csv_writer.writerows(data)
        
            
    c.execute("Select * from merged_mxm_year_one_table WHERE year between 1946 and 1950;")
    data = c.fetchall()
#    print(data)
#    print("termina uno /n")
    with open("out_1946-1950.csv", "w", newline='') as csv_file:  # Python 3 version    
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow([i[0] for i in c.description]) # write headers
        csv_writer.writerows(data)
        
                    
    c.execute("Select * from merged_mxm_year_one_table WHERE year between 1951 and 1952;")
    data = c.fetchall()
#    print(data)
#    print("termina uno /n")
    with open("out_1951-1952.csv", "w", newline='') as csv_file:  # Python 3 version    
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow([i[0] for i in c.description]) # write headers
        csv_writer.writerows(data)
        
                    
    c.execute("Select * from merged_mxm_year_one_table WHERE year between 1953 and 1954;")
    data = c.fetchall()
#    print(data)
#    print("termina uno /n")
    with open("out_1953-1954.csv", "w", newline='') as csv_file:  # Python 3 version    
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow([i[0] for i in c.description]) # write headers
        csv_writer.writerows(data)
        
                
                    
    c.execute("Select * from merged_mxm_year_one_table WHERE year between 1955 and 1956;")
    data = c.fetchall()
#    print(data)
#    print("termina uno /n")
    with open("out_1955-1956.csv", "w", newline='') as csv_file:  # Python 3 version    
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow([i[0] for i in c.description]) # write headers
        csv_writer.writerows(data)
        
                    
    c.execute("Select * from merged_mxm_year_one_table WHERE year between 1957 and 1958;")
    data = c.fetchall()
#    print(data)
#    print("termina uno /n")
    with open("out_1957-1958.csv", "w", newline='') as csv_file:  # Python 3 version    
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow([i[0] for i in c.description]) # write headers
        csv_writer.writerows(data)
        
                
                    
    c.execute("Select * from merged_mxm_year_one_table WHERE year between 1959 and 1960;")
    data = c.fetchall()
#    print(data)
#    print("termina uno /n")
    with open("out_1959-1960.csv", "w", newline='') as csv_file:  # Python 3 version    
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow([i[0] for i in c.description]) # write headers
        csv_writer.writerows(data)
        
                    
    c.execute("Select * from merged_mxm_year_one_table WHERE year between 1961 and 1962;")
    data = c.fetchall()
#    print(data)
#    print("termina uno /n")
    with open("out_1962-1962.csv", "w", newline='') as csv_file:  # Python 3 version    
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow([i[0] for i in c.description]) # write headers
        csv_writer.writerows(data)
        
                
                    
    c.execute("Select * from merged_mxm_year_one_table WHERE year between 1963 and 1964;")
    data = c.fetchall()
#    print(data)
#    print("termina uno /n")
    with open("out_1963-1964.csv", "w", newline='') as csv_file:  # Python 3 version    
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow([i[0] for i in c.description]) # write headers
        csv_writer.writerows(data)
        
                    
    c.execute("Select * from merged_mxm_year_one_table WHERE year between 1965 and 1966;")
    data = c.fetchall()
#    print(data)
#    print("termina uno /n")
    with open("out_1965-1966.csv", "w", newline='') as csv_file:  # Python 3 version    
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow([i[0] for i in c.description]) # write headers
        csv_writer.writerows(data)
        
                
                    
    c.execute("Select * from merged_mxm_year_one_table WHERE year between 1967 and 1968;")
    data = c.fetchall()
#    print(data)
#    print("termina uno /n")
    with open("out_1967-1968.csv", "w", newline='') as csv_file:  # Python 3 version    
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow([i[0] for i in c.description]) # write headers
        csv_writer.writerows(data)
        
                    
    c.execute("Select * from merged_mxm_year_one_table WHERE year between 1969 and 1970;")
    data = c.fetchall()
#    print(data)
#    print("termina uno /n")
    with open("out_1969-1970.csv", "w", newline='') as csv_file:  # Python 3 version    
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow([i[0] for i in c.description]) # write headers
        csv_writer.writerows(data)
        
                
                    
    c.execute("Select * from merged_mxm_year_one_table WHERE year between 1971 and 1972;")
    data = c.fetchall()
#    print(data)
#    print("termina uno /n")
    with open("out_1971-1972.csv", "w", newline='') as csv_file:  # Python 3 version    
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow([i[0] for i in c.description]) # write headers
        csv_writer.writerows(data)
        
                    
    c.execute("Select * from merged_mxm_year_one_table WHERE year between 1973 and 1974;")
    data = c.fetchall()
#    print(data)
#    print("termina uno /n")
    with open("out_1973-1974.csv", "w", newline='') as csv_file:  # Python 3 version    
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow([i[0] for i in c.description]) # write headers
        csv_writer.writerows(data)
        
                
    c.execute("Select * from merged_mxm_year_one_table WHERE year between 1975 and 1976;")
    data = c.fetchall()
#    print(data)
#    print("termina uno /n")
    with open("out_1975-1976.csv", "w", newline='') as csv_file:  # Python 3 version    
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow([i[0] for i in c.description]) # write headers
        csv_writer.writerows(data)
        
                
                    
    c.execute("Select * from merged_mxm_year_one_table WHERE year between 1977 and 1978;")
    data = c.fetchall()
#    print(data)
#    print("termina uno /n")
    with open("out_1977-1978.csv", "w", newline='') as csv_file:  # Python 3 version    
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow([i[0] for i in c.description]) # write headers
        csv_writer.writerows(data)
        
                    
    c.execute("Select * from merged_mxm_year_one_table WHERE year between 1979 and 1980;")
    data = c.fetchall()
#    print(data)
#    print("termina uno /n")
    with open("out_1979-1980.csv", "w", newline='') as csv_file:  # Python 3 version    
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow([i[0] for i in c.description]) # write headers
        csv_writer.writerows(data)
        
                 
                    
    c.execute("Select * from merged_mxm_year_one_table WHERE year between 1981 and 1982;")
    data = c.fetchall()
#    print(data)
#    print("termina uno /n")
    with open("out_1981-1982.csv", "w", newline='') as csv_file:  # Python 3 version    
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow([i[0] for i in c.description]) # write headers
        csv_writer.writerows(data)
        
                    
    c.execute("Select * from merged_mxm_year_one_table WHERE year between 1983 and 1984;")
    data = c.fetchall()
#    print(data)
#    print("termina uno /n")
    with open("out_1983-1984.csv", "w", newline='') as csv_file:  # Python 3 version    
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow([i[0] for i in c.description]) # write headers
        csv_writer.writerows(data)
        
                
    c.execute("Select * from merged_mxm_year_one_table WHERE year between 1985 and 1986;")
    data = c.fetchall()
#    print(data)
#    print("termina uno /n")
    with open("out_1985-1986.csv", "w", newline='') as csv_file:  # Python 3 version    
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow([i[0] for i in c.description]) # write headers
        csv_writer.writerows(data)
        
                
                    
    c.execute("Select * from merged_mxm_year_one_table WHERE year between 1987 and 1988;")
    data = c.fetchall()
#    print(data)
#    print("termina uno /n")
    with open("out_1987-1988.csv", "w", newline='') as csv_file:  # Python 3 version    
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow([i[0] for i in c.description]) # write headers
        csv_writer.writerows(data)
        
                    
    c.execute("Select * from merged_mxm_year_one_table WHERE year between 1989 and 1990;")
    data = c.fetchall()
#    print(data)
#    print("termina uno /n")
    with open("out_1989-1990.csv", "w", newline='') as csv_file:  # Python 3 version    
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow([i[0] for i in c.description]) # write headers
        csv_writer.writerows(data)
        
                
                
                    
    c.execute("Select * from merged_mxm_year_one_table WHERE year between 1991 and 1992;")
    data = c.fetchall()
#    print(data)
#    print("termina uno /n")
    with open("out_1991-1992.csv", "w", newline='') as csv_file:  # Python 3 version    
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow([i[0] for i in c.description]) # write headers
        csv_writer.writerows(data)
        
                    
    c.execute("Select * from merged_mxm_year_one_table WHERE year between 1993 and 1994;")
    data = c.fetchall()
#    print(data)
#    print("termina uno /n")
    with open("out_1993-1994.csv", "w", newline='') as csv_file:  # Python 3 version    
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow([i[0] for i in c.description]) # write headers
        csv_writer.writerows(data)
        
                
    c.execute("Select * from merged_mxm_year_one_table WHERE year between 1995 and 1996;")
    data = c.fetchall()
#    print(data)
#    print("termina uno /n")
    with open("out_1995-1996.csv", "w", newline='') as csv_file:  # Python 3 version    
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow([i[0] for i in c.description]) # write headers
        csv_writer.writerows(data)
        
                
                    
    c.execute("Select * from merged_mxm_year_one_table WHERE year between 1997 and 1998;")
    data = c.fetchall()
#    print(data)
#    print("termina uno /n")
    with open("out_1997-1998.csv", "w", newline='') as csv_file:  # Python 3 version    
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow([i[0] for i in c.description]) # write headers
        csv_writer.writerows(data)
        
                    
    c.execute("Select * from merged_mxm_year_one_table WHERE year between 1999 and 2000;")
    data = c.fetchall()
#    print(data)
#    print("termina uno /n")
    with open("out_1999-2000.csv", "w", newline='') as csv_file:  # Python 3 version    
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow([i[0] for i in c.description]) # write headers
        csv_writer.writerows(data)
        
                
                
                    
    c.execute("Select * from merged_mxm_year_one_table WHERE year between 2001 and 2002;")
    data = c.fetchall()
#    print(data)
#    print("termina uno /n")
    with open("out_2001-2002.csv", "w", newline='') as csv_file:  # Python 3 version    
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow([i[0] for i in c.description]) # write headers
        csv_writer.writerows(data)
        
                    
    c.execute("Select * from merged_mxm_year_one_table WHERE year between 2003 and 2004;")
    data = c.fetchall()
#    print(data)
#    print("termina uno /n")
    with open("out_2003-2004.csv", "w", newline='') as csv_file:  # Python 3 version    
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow([i[0] for i in c.description]) # write headers
        csv_writer.writerows(data)
        
                
    c.execute("Select * from merged_mxm_year_one_table WHERE year between 2005 and 2006;")
    data = c.fetchall()
#    print(data)
#    print("termina uno /n")
    with open("out_2005-2006.csv", "w", newline='') as csv_file:  # Python 3 version    
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow([i[0] for i in c.description]) # write headers
        csv_writer.writerows(data)
        
                
                    
    c.execute("Select * from merged_mxm_year_one_table WHERE year between 2007 and 2008;")
    data = c.fetchall()
#    print(data)
#    print("termina uno /n")
    with open("out_2007-2008.csv", "w", newline='') as csv_file:  # Python 3 version    
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow([i[0] for i in c.description]) # write headers
        csv_writer.writerows(data)
        
                    
    c.execute("Select * from merged_mxm_year_one_table WHERE year between 2009 and 2010;")
    data = c.fetchall()
#    print(data)
#    print("termina uno /n")
    with open("out_2009-2010.csv", "w", newline='') as csv_file:  # Python 3 version    
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow([i[0] for i in c.description]) # write headers
        csv_writer.writerows(data)
        
                
                
                    
        
    
def read_from_db():
    
    # SQL command to create a table in the database 
    sql_command = """select * from merged_mxm_year_one_table
    where track_id is NULL or track_id in
    (Select distinct track_id from merged_mxm_year_one_table
    where word is "sur" or word is "quiero" or word is "tu" or word is "se" or word is "mi" or word is "es" or word is "le" or word is "ich" or word is "du" or word is "si" or word is "und" or word is "je" or word is "et" or word is "amor" or word is "una" or word is "pas" or word is "ma" or word is "nicht" or word is "das" or word is "ist" or word is "cest" or word is "ne" or word is "vida" or word is "eu" or word is "zu" or word is "esta" or word is "wir" or word is "ja" or word is "mir" or word is "dich" or word is "um" or word is "au" or word is "jag" or word is "nos" or word is "nos" or word is "pero" or word is "auf" or word is "não" or word is "moi" or word is "une" or word is "é" or word is "sur" or word is "mein");"""

    c.executescript(sql_command)
    data = c.fetchall()
    print(data)
#    conn.commit()
    
#    c.execute('SELECT * FROM merged_mxm_year_one_table WHERE count = 12')
#    data = c.fetchall()
#    print(data)
#    for row in data:
#         print(row)

#    c.execute('SELECT * FROM merged_mxm_year_one_table WHERE count = 12')
#    data = c.fetchall()
#    print(data)
#    for row in data:
#         print(row)





#    c.execute('SELECT * FROM stuffToPlot WHERE value = 3')
#    data = c.fetchall()
#    print(data)
#    for row in data:
#        print(row)

#    c.execute('SELECT * FROM stuffToPlot WHERE unix > 1452554972')
#    data = c.fetchall()
#    print(data)
#    for row in data:
#        print(row)

#    c.execute('SELECT value, datestamp FROM stuffToPlot WHERE unix > 1452554972')
#    data = c.fetchall()
#    print(data)
#    for row in data:
#        print(row[0])
#    print("end of read")

#def del_and_update():
#    c.execute('SELECT * FROM stuffToPlot')
#    data = c.fetchall()
#    [print(row) for row in data]
#    predato = 8
#    dato = (predato,)
#    c.execute('UPDATE stuffToPlot SET value = 99 WHERE value = ?',dato)
#    conn.commit()

#    c.execute('SELECT * FROM stuffToPlot')
#    data = c.fetchall()
#    [print(row) for row in data]
 
prueba()
#add_tfidf()
#tfidf_calc()
#read_from_db()   
#del_and_update()
#delete_from_db()
#slice_db()
c.close
conn.close()