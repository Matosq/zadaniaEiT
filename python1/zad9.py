import os

lista=["sie","nigdy","dlaczego","i","oraz"]
sciezka="/home/pythonml/zadania/textfiles/poland"

for x in os.listdir(sciezka):
    plik=open(x).readlines()
    cel=open(x,'w')

    for f in plik:
        if f in lista:
            cel.write(f.replace(f,""))
    cel.close()
