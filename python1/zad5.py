import os


biezacyKatalog=os.getcwd()


sciezka="/home/"
os.chdir(sciezka)


def fun(powrot):
    katalog=os.getcwd()
    print("KATALOG: ",katalog)
    for f in os.listdir(katalog):
        print(f)

    for k in os.listdir(katalog):
        if os.path.isdir(k):
            os.chdir(k)
            fun(katalog)

        if katalog == biezacyKatalog:
            print("koniec")
            return
        else:
            os.chdir(powrot)

    return


fun(sciezka)
