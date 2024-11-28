import random

def hod_kockou():
    kocka = random.randint(1, 6)
    if kocka == 6:
        kocka = kocka + hod_kockou()
    return kocka

def vypis_pola(n, hraci, teleporty):
    for i in range(n):
        for j in range(n):
            symbol = "."
            for teleport in teleporty:
                if teleport.x1 == i and teleport.y1 == j:
                    symbol = teleport.pismeno
                if teleport.x2 == i and teleport.y2 == j:
                    symbol = teleport.pismeno
            for hrac in hraci:
                if hrac.x == i and hrac.y == j:
                    symbol = hrac.id
            print(symbol, end=" ")
        print()

class Hrac:
    def __init__(self, id):
        self.id = id
        self.x = 0
        self.y = 0

class Teleport:
    def __init__(self, typ, pismeno, x1, y1, x2, y2):
        self.typ = typ
        self.pismeno = pismeno
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

def main():
    n = 5

    while True:
        hraci = [
            Hrac(1),
            Hrac(2)
        ]

        teleporty = [
            Teleport("pozitivny", "A", 0, 4, 3, 0),
            Teleport("pozitivny", "B", 1, 1, 2, 2),
            Teleport("negativny", "a", 4, 2, 2, 3),
            Teleport("negativny", "b", 3, 4, 0, 2)
        ]

        hraci[1].y = 1

        vypis_pola(n, hraci, teleporty)

        break

main()
