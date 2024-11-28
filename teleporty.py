import random
import math

def hod_kockou():
    kocka = random.randint(1, 6)
    if kocka == 6:
        kocka = kocka + hod_kockou()
    return kocka

def vypis_pola(n, hraci, teleporty):
    print("Hracie pole:")
    print(" ", end=" ")
    for i in range(n):
        print(i, end=" ")
    print()
    for i in range(n):
        print(i, end=" ")
        for j in range(n):
            symbol = "."
            if i == 0 and j == 0:
                symbol = "+"
            if i == n - 1 and j == n - 1:
                symbol = "*"
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

    def posun(self, n, teleporty):
        kocka = hod_kockou()
        print(f"Hrac {self.id} hodil {kocka}")

class Teleport:
    def __init__(self, typ, pismeno, x1, y1, x2, y2):
        self.typ = typ
        self.pismeno = pismeno
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

def main():
    n = int(input("Zadajte rozmer hracej plochy: "))

    if n < 5 or n > 10:
        print("Rozmer hracej plochy musi byt v rozsahu 5 az 10")
        return
    
    k = int(input("Zadajte pocet hracov: "))

    if k < 1 or k > 4:
        print("Pocet hracov musi byt v rozsahu 1 az 4")
        return
    
    # Vygenerovanie hraciej plochy

    hraci = [
        Hrac(1),
        Hrac(2)
    ]

    # teleporty = [
    #     Teleport("pozitivny", "A", 0, 4, 3, 0),
    #     Teleport("pozitivny", "B", 1, 1, 2, 2),
    #     Teleport("negativny", "a", 4, 2, 2, 3),
    #     Teleport("negativny", "b", 3, 4, 0, 2)
    # ]

    pocet_poz_tp = math.floor(n / 2)
    pocet_neg_tp = math.floor(n / 2)

    def splna_podmienky(x1, y1, x2, y2, teleporty):
        splna = True
        # kontrola ci nie su teleporty na zaciatku alebo na konci
        if (x1 == 0 and y1 == 0) or (x1 == n - 1 and y1 == n - 1) or (x2 == 0 and y2 == 0) or (x2 == n - 1 and y2 == n - 1):
            splna = False
        
        # kontrola ci nie su teleporty na rovnakych poziciach
        for teleport in teleporty:
            if (teleport.x1 == x1 and teleport.y1 == y1) or (teleport.x1 == x2 and teleport.y1 == y2) or (teleport.x2 == x1 and teleport.y2 == y1) or (teleport.x2 == x2 and teleport.y2 == y2):
                splna = False
        
        return splna
        

    teleporty = []

    for i in range(pocet_poz_tp):
        while True:
            x1 = random.randint(0, n - 1)
            y1 = random.randint(0, n - 1)
            x2 = random.randint(0, n - 1)
            y2 = random.randint(0, n - 1)
            if x2 > x1 and splna_podmienky(x1, y1, x2, y2, teleporty):
                teleporty.append(Teleport("pozitivny", chr(65 + i), x1, y1, x2, y2)) # pismeno generujeme pomocou ASCII tabulky
                break

    for i in range(pocet_neg_tp):
        while True:
            x1 = random.randint(0, n - 1)
            y1 = random.randint(0, n - 1)
            x2 = random.randint(0, n - 1)
            y2 = random.randint(0, n - 1)
            if x2 < x1 and splna_podmienky(x1, y1, x2, y2, teleporty):
                teleporty.append(Teleport("negativny", chr(97 + i), x1, y1, x2, y2)) # pismeno generujeme pomocou ASCII tabulky
                break

    while True:

        vypis_pola(n, hraci, teleporty)

        break

main()
