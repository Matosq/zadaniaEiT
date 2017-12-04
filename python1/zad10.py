import os

zrodlo=open("/home/pythonml/zadania/text.txt").readlines()
cel=open('/home/pythonml/zadania/text.txt','w')

lista=['i','oraz','nigdy','dlaczego']
zamiana=['oraz','i','prawie nigdy','czemu']

slownik={'i':'oraz','oraz':'i','nigdy':'prawie nigdy','dlaczego':'czemu'}

for s in zrodlo:
    for x in slownik.keys():
        if s == x:
            cel.write(s.replace(x,slownik.get(x)))

cel.close()
