import _thread
import time
import random

# indeks widelca:  0  1  2  3  4  0
#                    |  |  |  |  |
# indeks filozowa:   0  1  2  3  4
# 1 oznacza wolny widelec, 0 to widelec zajety
# w programie wystepuje losowanie, czy filozof podnosi najpierw lewy czy prawy widelec

random.seed()
widelce=[1,1,1,1,1]

def jedzenie(nazwa, nr):
    while True:
        print("start")

        lewy = False
        prawy = False

        rzut = random.randint(1, 2)

        if nr == 4:
            if widelce[0] == 1:
                widelce[0] = 0
                print(nazwa, " podnosi prawy widelec.")
                prawy=True
            else:
                print(nazwa, " ma prawy widelec zajęty.")
                prawy=False

            if widelce[4] == 1:
                widelce[4] = 0
                print(nazwa, " podnosi lewy widelec.")
                lewy = True
            else:
                print(nazwa, " ma lewy widelec zajęty.")

        elif rzut % 2 == 1:

            if widelce[nr+1] == 1:
                widelce[nr+1] = 0
                print(nazwa, " podnosi prawy widelec.")
                prawy = True

            else:
                print(nazwa, " ma prawy widelec zajęty.")
                prawy=False

            if widelce[nr] == 1:
                widelce[nr] = 0
                print(nazwa, " podnosi lewy widelec.")
                lewy = True
            else:
                print(nazwa, " ma lewy widelec zajęty.")
                lewy = False
        else:
            if widelce[nr] == 1:
                widelce[nr] = 0
                print(nazwa, " podnosi lewy widelec.")
                lewy = True
            else:
                print(nazwa, " ma lewy widelec zajęty.")
                lewy = False

            if widelce[nr+1] == 1:
                widelce[nr+1] = 0
                print(nazwa, " podnosi prawy widelec.")
                prawy=True

            else:
                print(nazwa, " ma prawy widelec zajęty.")
                prawy=False

        delay = random.randint(1,5)

        if lewy is True and prawy is True:
            print(nazwa, " je.")
            time.sleep(delay)
            print(nazwa, " skończył jeść. Odkłada widelce.")

        else:
            print(nazwa, "nie ma dwóch wolnych widelców. Odkłada i czeka.")

        lewy = False
        prawy = False

        if nr == 4:
            widelce[0]=1
        else:
            widelce[nr+1]=1

        widelce[nr]=1
        delay = random.randint(1, 5)
        time.sleep(delay)

try:
    _thread.start_new_thread(jedzenie, ("Platon", 0))
    _thread.start_new_thread(jedzenie, ("Arystoteles",1))
    _thread.start_new_thread(jedzenie, ("Sokrates", 2))
    _thread.start_new_thread(jedzenie, ("Tales", 3))
    _thread.start_new_thread(jedzenie, ("Pitagoras", 4))
except:
    print("ERROR!")

while True:
    pass

print("Koniec programu")
