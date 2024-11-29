# Skript riesi vsetky casti projektu (A + B + C), cize vykresli hracie pole a spusti simulaciu hry pre k hracov

import random
import math

# funkcia na generovanie nahodneho cisla od 1 po 6, ak padne 6 tak sa funkcia zavola znova a cisla sa scitaju
def hod_kockou():
    kocka = random.randint(1, 6)
    if kocka == 6:
        kocka = kocka + hod_kockou()
    return kocka

# funkcia na vykreslenie hracieho pola
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
            if (n % 2 == 0 and i == n - 1 and j == 0) or (n % 2 != 0 and i == n - 1 and j == n - 1):
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
    print("============")

# funkcia na vypis pozicii hracov
def vypis_pozicii(hraci):
    print("Pozicie hracov:")
    for hrac in hraci:
        print(f"Hrac c. {hrac.id} [{hrac.x}, {hrac.y}]")
    print("---")

# funkcia na kontrolu ci je hrac v cieli
def hrac_je_v_cieli(hrac, n):
    # ciel je v prvom stlpci ak je n parne a v poslednom stlpci ak je n neparne
    if (n % 2 == 0 and hrac.x == n - 1 and hrac.y == 0) or (n % 2 != 0 and hrac.x == n - 1 and hrac.y == n - 1):
        return True
    return False

# funkcia na kontrolu ci nahodne vygenerovane suradnice teleportu splnaju podmienky 
def splna_podmienky(x1, y1, x2, y2, teleporty, n):
    splna = True
    # kontrola ci nie su teleporty na zaciatku alebo na konci hracej plochy
    if (x1 == 0 and y1 == 0) or (x1 == n - 1 and y1 == n - 1) or (x2 == 0 and y2 == 0) or (x2 == n - 1 and y2 == n - 1):
        splna = False
    
    # kontrola ci nie su teleporty na rovnakych poziciach
    for teleport in teleporty:
        if (teleport.x1 == x1 and teleport.y1 == y1) or (teleport.x1 == x2 and teleport.y1 == y2) or (teleport.x2 == x1 and teleport.y2 == y1) or (teleport.x2 == x2 and teleport.y2 == y2):
            splna = False
    
    return splna

class Hrac:
    # konstruktor triedy Hrac
    def __init__(self, id):
        self.id = id
        self.x = 0
        self.y = 0

    # funkcia na simulovanie jedneho kola hry pre hraca
    def posun(self, n, teleporty):
        kocka = hod_kockou()
        print(f"Hrac c. {self.id} hodil spolu na kocke: {kocka} bodov")
        
        # pomocne premenne aby sme nepohli priamo hracom kym este nevieme kam sa ma posunut
        nove_x = self.x
        nove_y = self.y

        for i in range(kocka):
            # if na zistenie ktorym smerom sa ma hrac posunut
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
        
        if nove_x >= n:
            print(f"Hrac c. {self.id} hodil viac bodov nez je vzdialenost do ciela!")
            return
        
        print(f"Hrac c. {self.id} sa posuva na policko: [{nove_x}, {nove_y}]")

        self.x = nove_x
        self.y = nove_y

        for teleport in teleporty:
            # ak hrac stoji na zaciatku teleportu tak ho presunieme na jeho koniec
            if teleport.x1 == self.x and teleport.y1 == self.y:
                self.x = teleport.x2
                self.y = teleport.y2
                print(f"Hrac c. {self.id} sa cez {teleport.typ} teleport '{teleport.pismeno}' posuva na policko: [{self.x}, {self.y}]")
                return

class Teleport:
    # konstruktor triedy Teleport
    def __init__(self, typ, pismeno, x1, y1, x2, y2):
        self.typ = typ # pozitivny/negativny
        self.pismeno = pismeno # oznacenie teleportu pri vypise hracieho pola
        # suradnice zaciatku teleportu
        self.x1 = x1
        self.y1 = y1
        # suradnice konca teleportu
        self.x2 = x2
        self.y2 = y2

def main():
    n = int(input("Zadaj parameter n (velkost hracieho pola): "))

    if n < 5 or n > 10:
        print("Rozmer hracej plochy musi byt v rozsahu 5 az 10")
        return
    
    k = int(input("Zadaj parameter k (pocet hracov): "))

    if k < 1 or k > 4:
        print("Pocet hracov musi byt v rozsahu 1 az 4")
        return
    
    # Generovanie hraciej plochy

    # pocet pozitivnych a negativnych teleportov
    pocet_poz_tp = math.floor(n / 2)
    pocet_neg_tp = math.floor(n / 2)
    
    teleporty = []

    for i in range(pocet_poz_tp):
        while True:
            x1 = random.randint(0, n - 1)
            y1 = random.randint(0, n - 1)
            x2 = random.randint(0, n - 1)
            y2 = random.randint(0, n - 1)
            if x2 > x1 and splna_podmienky(x1, y1, x2, y2, teleporty, n):
                teleporty.append(Teleport("pozitivny", chr(65 + i), x1, y1, x2, y2)) # pismeno generovane pomocou ASCII kodu
                break

    for i in range(pocet_neg_tp):
        while True:
            x1 = random.randint(0, n - 1)
            y1 = random.randint(0, n - 1)
            x2 = random.randint(0, n - 1)
            y2 = random.randint(0, n - 1)
            if x2 < x1 and splna_podmienky(x1, y1, x2, y2, teleporty, n):
                teleporty.append(Teleport("negativny", chr(97 + i), x1, y1, x2, y2)) # pismeno generovane pomocou ASCII kodu
                break
    
    hraci = []

    for i in range(k):
        hraci.append(Hrac(i + 1))

    # prvy vypis pola bez hracov
    vypis_pola(n, hraci, teleporty, False)
    vypis_pozicii(hraci)

    while True:
        for hrac in hraci:
            hrac.posun(n, teleporty)

            if hrac_je_v_cieli(hrac, n):
                vypis_pola(n, hraci, teleporty)
                print(f"Hrac c. {hrac.id} VYHRAL!")
                return
            
            vypis_pola(n, hraci, teleporty)
            vypis_pozicii(hraci)

main()
