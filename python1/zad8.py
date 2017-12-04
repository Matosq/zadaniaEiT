import random

random.seed()
L=[]
for x in range(50):
    L.append(int(random.random()*20))


for i in range(50):
    j=i+1
    index=i
    while j < 50:
        if L[j] > L[index]:
            index=j
        j+=1

    x=L[i]
    L[i]=L[index]
    L[index]=x






