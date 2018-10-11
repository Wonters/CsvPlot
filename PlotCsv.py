
# script qui lit un fichier csv et qui le trace

import csv
import os
import sys
import string
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.cbook as cbook

print("Entrée le chemin absolue du fichier csv à ploter ")
PathCsv ='fichier.csv' #sys.stdin.readline()
#PathCsv = PathCsv.replace("\n","")
X,Y=[],[]
with open(PathCsv, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    print("fichier csv chargé", PathCsv)
    for row in reader:
        print(row['X'],row['Y'])  # row est un dictionnaire
        X.append(row['X'])
        Y.append(row['Y'])
print("donnée chargées:\n",X,Y)
plt.plot(X,Y,'ro')
plt.show()


