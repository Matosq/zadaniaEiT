import os
import re

sciezka="/home/pythonml/zadania/pliki"
os.chdir(sciezka)
rozszerzenie=".jpg"
noweRozszerzenie="*.png"


for f in os.listdir(sciezka):
    f.replace(r'*jpg',r'*png')

#for f in os.listdir(sciezka):
#    dopasowanie=re.search(rozszerzenie,f)
#       if dopasowanie:
#            print(f)


for f in os.listdir(sciezka):
    print(f)
