
# script qui lit un fichier csv et qui le trace

import csv
import os
import sys
import string
#from matplotlib.py import pyplot as plt


print("Entrée le chemin absolue du fichier csv à ploter ")
PathCsv ='test.csv' #sys.stdin.readline()
#PathCsv = PathCsv.replace("\n","")
with open(PathCsv, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    print("fichier csv chargé", PathCsv)
    for row in reader:
        print(row['Y'],row['X'])
        
        

