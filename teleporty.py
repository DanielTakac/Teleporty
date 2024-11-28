import random
import math

def hod_kockou():
    kocka = random.randint(1, 6)
    if kocka == 6:
        kocka = kocka + hod_kockou()
    return kocka

def vypis_pola(n, hraci, teleporty, vypisat_hracov=True):
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
                if vypisat_hracov and hrac.x == i and hrac.y == j:
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
        
        nove_x = self.x
        nove_y = self.y

        for i in range(kocka):
            if (nove_x + 1) % 2 == 0:
                if nove_y == 0:
                    nove_x = nove_x + 1
                else:
                    nove_y = nove_y - 1
            else:
                if nove_y == n - 1:
                    nove_x = nove_x + 1
                else:
                    nove_y = nove_y + 1

        # todo: check if nove_x/nove_y are the goal/out of bounds/start of a teleport/... and decide wheter to just move there or do something special
            

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
                teleporty.append(Teleport("pozitivny", chr(65 + i), x1, y1, x2, y2)) # pismeno generovane pomocou ASCII tabulky
                break

    for i in range(pocet_neg_tp):
        while True:
            x1 = random.randint(0, n - 1)
            y1 = random.randint(0, n - 1)
            x2 = random.randint(0, n - 1)
            y2 = random.randint(0, n - 1)
            if x2 < x1 and splna_podmienky(x1, y1, x2, y2, teleporty):
                teleporty.append(Teleport("negativny", chr(97 + i), x1, y1, x2, y2)) # pismeno generovane pomocou ASCII tabulky
                break
    
    hraci = []

    for i in range(k):
        hraci.append(Hrac(i + 1))

    # prvy vypis pola bez hracov
    vypis_pola(n, hraci, teleporty, False)

    while True:

        for hrac in hraci:
            hrac.posun(n, teleporty)

        vypis_pola(n, hraci, teleporty)

        break

main()
