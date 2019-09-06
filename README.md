# MLNLP
NLP Project

For the slicing of the MSD database please go to the Data Preprocessing folder. The following commands are to be run on Terminal or similar using Mark Greene's implementation of the DTM with NMF. With the following slicing structure:

1920-1930
1931-1940
1941-1950
1951-1954
1955-1958
1959-1960
1961-1962
1963-1964
1965-1966
1967-1968
1969-1970
1971-1972
1973-1974
1975-1976
1977-1978
1979-1980
1981-1982
1983-1984
1985-1986
1987-1988
1989-1990
1991-1992
1993-1994
1995-1996
1997-1998
1999-2000
2001-2002
2003-2004
2005-2006
2007-2008
2009-2010

All files are also found under the following Address https://drive.google.com/drive/folders/1qk54VGaiVR5e0TaxgytCQOCc-zbZXhJA?usp=sharing


Preprocess

python prep-text.py data/sample/1920-1930 data/sample/1931-1940 data/sample/1941-1950 data/sample/1951-1954 data/sample/1955-1958 data/sample/1959-1960 data/sample/1961-1962 data/sample/1963-1964 data/sample/1965-1966 data/sample/1967-1968 data/sample/1969-1970 data/sample/1971-1972 data/sample/1973-1974 data/sample/1975-1976 data/sample/1977-1978 data/sample/1979-1980 data/sample/1981-1982 data/sample/1983-1984 data/sample/1985-1986 data/sample/1987-1988 data/sample/1989-1990 data/sample/1991-1992 data/sample/1993-1994 data/sample/1995-1996 data/sample/1997-1998 data/sample/1999-2000 data/sample/2001-2002 data/sample/2003-2004 data/sample/2005-2006 data/sample/2007-2008 data/sample/2009-2010 -o data --tfidf --norm

Window Topic Modeling

python find-window-topics.py data/*.pkl -k 5 -o out

When the process has completed, we can view the descriptiors (i.e. the top ranked terms) for the resulting window topics as follows:

python display-topics.py out/1920-1930_windowtopics_k05.pkl out/1931-1940_windowtopics_k05.pkl out/1941-1950_windowtopics_k05.pkl out/1951-1954_windowtopics_k05.pkl out/1955-1958_windowtopics_k05.pkl out/1959-1960_windowtopics_k05.pkl out/1961-1962_windowtopics_k05.pkl out/1963-1964_windowtopics_k05.pkl out/1965-1966_windowtopics_k05.pkl out/1967-1968_windowtopics_k05.pkl out/1969-1970_windowtopics_k05.pkl out/1971-1972_windowtopics_k05.pkl out/1973-1974_windowtopics_k05.pkl out/1975-1976_windowtopics_k05.pkl out/1977-1978_windowtopics_k05.pkl out/1979-1980_windowtopics_k05.pkl out/1981-1982_windowtopics_k05.pkl out/1983-1984_windowtopics_k05.pkl out/1985-1986_windowtopics_k05.pkl out/1987-1988_windowtopics_k05.pkl out/1989-1990_windowtopics_k05.pkl out/1991-1992_windowtopics_k05.pkl out/1993-1994_windowtopics_k05.pkl out/1995-1996_windowtopics_k05.pkl out/1997-1998_windowtopics_k05.pkl out/1999-2000_windowtopics_k05.pkl out/2001-2002_windowtopics_k05.pkl out/2003-2004_windowtopics_k05.pkl out/2005-2006_windowtopics_k05.pkl out/2007-2008_windowtopics_k05.pkl out/2009-2010_windowtopics_k05.pkl


The top terms and document IDs can be exported from a NMF results file

python export-csv.py out/1920-1930_windowtopics_k05.pkl out/1931-1940_windowtopics_k05.pkl out/1941-1950_windowtopics_k05.pkl out/1951-1954_windowtopics_k05.pkl out/1955-1958_windowtopics_k05.pkl out/1959-1960_windowtopics_k05.pkl out/1961-1962_windowtopics_k05.pkl out/1963-1964_windowtopics_k05.pkl out/1965-1966_windowtopics_k05.pkl out/1967-1968_windowtopics_k05.pkl out/1969-1970_windowtopics_k05.pkl out/1971-1972_windowtopics_k05.pkl out/1973-1974_windowtopics_k05.pkl out/1975-1976_windowtopics_k05.pkl out/1977-1978_windowtopics_k05.pkl out/1979-1980_windowtopics_k05.pkl out/1981-1982_windowtopics_k05.pkl out/1983-1984_windowtopics_k05.pkl out/1985-1986_windowtopics_k05.pkl out/1987-1988_windowtopics_k05.pkl out/1989-1990_windowtopics_k05.pkl out/1991-1992_windowtopics_k05.pkl out/1993-1994_windowtopics_k05.pkl out/1995-1996_windowtopics_k05.pkl out/1997-1998_windowtopics_k05.pkl out/1999-2000_windowtopics_k05.pkl out/2001-2002_windowtopics_k05.pkl out/2003-2004_windowtopics_k05.pkl out/2005-2006_windowtopics_k05.pkl out/2007-2008_windowtopics_k05.pkl out/2009-2010_windowtopics_k05.pkl -t 50



Step 3: Dynamic Topic Modeling

python find-dynamic-topics.py out/1920-1930_windowtopics_k05.pkl out/1931-1940_windowtopics_k05.pkl out/1941-1950_windowtopics_k05.pkl out/1951-1954_windowtopics_k05.pkl out/1955-1958_windowtopics_k05.pkl out/1959-1960_windowtopics_k05.pkl out/1961-1962_windowtopics_k05.pkl out/1963-1964_windowtopics_k05.pkl out/1965-1966_windowtopics_k05.pkl out/1967-1968_windowtopics_k05.pkl out/1969-1970_windowtopics_k05.pkl out/1971-1972_windowtopics_k05.pkl out/1973-1974_windowtopics_k05.pkl out/1975-1976_windowtopics_k05.pkl out/1977-1978_windowtopics_k05.pkl out/1979-1980_windowtopics_k05.pkl out/1981-1982_windowtopics_k05.pkl out/1983-1984_windowtopics_k05.pkl out/1985-1986_windowtopics_k05.pkl out/1987-1988_windowtopics_k05.pkl out/1989-1990_windowtopics_k05.pkl out/1991-1992_windowtopics_k05.pkl out/1993-1994_windowtopics_k05.pkl out/1995-1996_windowtopics_k05.pkl out/1997-1998_windowtopics_k05.pkl out/1999-2000_windowtopics_k05.pkl out/2001-2002_windowtopics_k05.pkl out/2003-2004_windowtopics_k05.pkl out/2005-2006_windowtopics_k05.pkl out/2007-2008_windowtopics_k05.pkl out/2009-2010_windowtopics_k05.pkl -k 5 -o out


When the process has completed, we can view the dynamic topic descriptiors using 'display-topics.py':


python display-topics.py out/dynamictopics_k05.pkl



Advanced Usage

Step 1: Build Word2Vec Model

python prep-word2vec.py data/sample -o out -m sg
	

Step 2: Window Topic Modeling

python find-window-topics.py data/*.pkl -k 4,10 -o out -m out/w2v-model.bin -w selected.csv


Step 3: Dynamic Topic Modeling


python find-dynamic-topics.py out/1920-1930_windowtopics_k05.pkl out/1931-1940_windowtopics_k07.pkl out/1941-1950_windowtopics_k04.pkl out/1951-1954_windowtopics_k08.pkl out/1955-1958_windowtopics_k04.pkl out/1959-1960_windowtopics_k04.pkl out/1961-1962_windowtopics_k04.pkl out/1963-1964_windowtopics_k04.pkl out/1965-1966_windowtopics_k04.pkl out/1967-1968_windowtopics_k05.pkl out/1969-1970_windowtopics_k04.pkl out/1971-1972_windowtopics_k04.pkl out/1973-1974_windowtopics_k04.pkl out/1975-1976_windowtopics_k04.pkl out/1977-1978_windowtopics_k04.pkl out/1979-1980_windowtopics_k04.pkl out/1981-1982_windowtopics_k04.pkl out/1983-1984_windowtopics_k04.pkl out/1985-1986_windowtopics_k04.pkl out/1987-1988_windowtopics_k04.pkl out/1989-1990_windowtopics_k04.pkl out/1991-1992_windowtopics_k04.pkl out/1993-1994_windowtopics_k04.pkl out/1995-1996_windowtopics_k05.pkl out/1997-1998_windowtopics_k04.pkl out/1999-2000_windowtopics_k04.pkl out/2001-2002_windowtopics_k04.pkl out/2003-2004_windowtopics_k04.pkl out/2005-2006_windowtopics_k04.pkl out/2007-2008_windowtopics_k04.pkl out/2009-2010_windowtopics_k04.pkl -k 4,10 -o out -m out/w2v-model.bin 

Applying this to the sample corpus for the range [4,10] results in the recommendation of 5 topics:

- Top recommendations for number of dynamic topics: 4,5,6

The corresponding results will be written to 'out/dynamictopics_k05.pkl'. When the process has completed, we can view the dynamic topic descriptiors using:

python display-topics.py out/dynamictopics_k05.pkl

Top 10 terms for 5 topics:

￼


Reviewing Results


Note that multiple topics in a single time window can be related to a single dynamic topic. Following on from the example the above, to see the tracking for all dynamic topics, run:

python track-dynamic-topics.py  out/dynamictopics_k05.pkl out/1920-1930_windowtopics_k05.pkl out/1931-1940_windowtopics_k07.pkl out/1941-1950_windowtopics_k04.pkl out/1951-1954_windowtopics_k08.pkl out/1955-1958_windowtopics_k04.pkl out/1959-1960_windowtopics_k04.pkl out/1961-1962_windowtopics_k04.pkl out/1963-1964_windowtopics_k04.pkl out/1965-1966_windowtopics_k04.pkl out/1967-1968_windowtopics_k05.pkl out/1969-1970_windowtopics_k04.pkl out/1971-1972_windowtopics_k04.pkl out/1973-1974_windowtopics_k04.pkl out/1975-1976_windowtopics_k04.pkl out/1977-1978_windowtopics_k04.pkl out/1979-1980_windowtopics_k04.pkl out/1981-1982_windowtopics_k04.pkl out/1983-1984_windowtopics_k04.pkl out/1985-1986_windowtopics_k04.pkl out/1987-1988_windowtopics_k04.pkl out/1989-1990_windowtopics_k04.pkl out/1991-1992_windowtopics_k04.pkl out/1993-1994_windowtopics_k04.pkl out/1995-1996_windowtopics_k05.pkl out/1997-1998_windowtopics_k04.pkl out/1999-2000_windowtopics_k04.pkl out/2001-2002_windowtopics_k04.pkl out/2003-2004_windowtopics_k04.pkl out/2005-2006_windowtopics_k04.pkl out/2007-2008_windowtopics_k04.pkl out/2009-2010_windowtopics_k04.pkl


To view tracking for only a subset of dynamic topics, specify one or more topic numbers comma separated!!!: Quite interesting! 

python track-dynamic-topics.py out/dynamictopics_k05.pkl out/1920-1930_windowtopics_k05.pkl out/1931-1940_windowtopics_k07.pkl out/1941-1950_windowtopics_k04.pkl out/1951-1954_windowtopics_k08.pkl out/1955-1958_windowtopics_k04.pkl out/1959-1960_windowtopics_k04.pkl out/1961-1962_windowtopics_k04.pkl out/1963-1964_windowtopics_k04.pkl out/1965-1966_windowtopics_k04.pkl out/1967-1968_windowtopics_k05.pkl out/1969-1970_windowtopics_k04.pkl out/1971-1972_windowtopics_k04.pkl out/1973-1974_windowtopics_k04.pkl out/1975-1976_windowtopics_k04.pkl out/1977-1978_windowtopics_k04.pkl out/1979-1980_windowtopics_k04.pkl out/1981-1982_windowtopics_k04.pkl out/1983-1984_windowtopics_k04.pkl out/1985-1986_windowtopics_k04.pkl out/1987-1988_windowtopics_k04.pkl out/1989-1990_windowtopics_k04.pkl out/1991-1992_windowtopics_k04.pkl out/1993-1994_windowtopics_k04.pkl out/1995-1996_windowtopics_k05.pkl out/1997-1998_windowtopics_k04.pkl out/1999-2000_windowtopics_k04.pkl out/2001-2002_windowtopics_k04.pkl out/2003-2004_windowtopics_k04.pkl out/2005-2006_windowtopics_k04.pkl out/2007-2008_windowtopics_k04.pkl out/2009-2010_windowtopics_k04.pkl -d 1,4

To create a partition file (i.e. a single membership topic model) for all documents in the complete corpus relative to the dynamic topics, run:



python create-dynamic-partition.py -o out/dynamic-combined.pkl out/dynamictopics_k05.pkl out/1920-1930_windowtopics_k05.pkl out/1931-1940_windowtopics_k07.pkl out/1941-1950_windowtopics_k04.pkl out/1951-1954_windowtopics_k08.pkl out/1955-1958_windowtopics_k04.pkl out/1959-1960_windowtopics_k04.pkl out/1961-1962_windowtopics_k04.pkl out/1963-1964_windowtopics_k04.pkl out/1965-1966_windowtopics_k04.pkl out/1967-1968_windowtopics_k05.pkl out/1969-1970_windowtopics_k04.pkl out/1971-1972_windowtopics_k04.pkl out/1973-1974_windowtopics_k04.pkl out/1975-1976_windowtopics_k04.pkl out/1977-1978_windowtopics_k04.pkl out/1979-1980_windowtopics_k04.pkl out/1981-1982_windowtopics_k04.pkl out/1983-1984_windowtopics_k04.pkl out/1985-1986_windowtopics_k04.pkl out/1987-1988_windowtopics_k04.pkl out/1989-1990_windowtopics_k04.pkl out/1991-1992_windowtopics_k04.pkl out/1993-1994_windowtopics_k04.pkl out/1995-1996_windowtopics_k05.pkl out/1997-1998_windowtopics_k04.pkl out/1999-2000_windowtopics_k04.pkl out/2001-2002_windowtopics_k04.pkl out/2003-2004_windowtopics_k04.pkl out/2005-2006_windowtopics_k04.pkl out/2007-2008_windowtopics_k04.pkl out/2009-2010_windowtopics_k04.pkl


Display
python display-topics.py out/dynamic-combined.pkl


For all other analysis mentioned in the report please refer to the Jupiter notebook.
