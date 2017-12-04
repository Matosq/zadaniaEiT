print("Podaj kod zamka. Wprowadz dowolna iosc cyfr")
szyfr=int(input())

for x in range(10):
    print("podaj kod aby otworzyc zamek")
    kod=int(input())

    if kod == szyfr:
        print("Kod prawidlowy. Zamek zostal otwarty")
        break
    else:
        print("Kod nie prawidlowy. To byla ",x+1," proba")
