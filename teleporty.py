import random

def hod_kockou():
    kocka = random.randint(1, 6)
    if kocka == 6:
        kocka = kocka + hod_kockou()
    return kocka

for i in 0, 100:
    print(hod_kockou())