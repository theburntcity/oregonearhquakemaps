from json import dump, load
import os
from pprint import pprint

# find files in os
file1 = os.path.join(r'datawrangling\usgsdata', '1019usgs.json')
file2 = os.path.join(r'datawrangling\usgsdata', '0010usgs.json')
file3 = os.path.join(r'datawrangling\usgsdata', '8900usgs.json')

# make of a list of files 
filenames = [file1, file2, file3]
# open  and merge files
with open(r'datawrangling\usgsdata\newusgs.json', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)
    

