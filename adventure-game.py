import random

harcos = 100
szorny = random.randint(200, 350)
print(f"A szörny életereje {szorny}")


harcos_dobasok_osszege = 0
def harcos_kore():
    global harcos_dobasok_osszege    
    harcos_dobasok_osszege = 0
    unlucky = 0                       # ha 1-est dob bármikor akkor nem sebez semmit
    global dobasok
    dobasok = int(input("Hány 20 oldalú kockát szeretnél dobni? A szörny ennyi plusz sebzést fog okozni a körében (max 10) "))
    if dobasok > 10:
        print("MAXIMUM 10")
    else:
        for i in range(1, dobasok + 1):
            random_szam = random.randint(1,20)
            print(f"{i}. dobás: {random_szam}")
            if random_szam == 1:
                print("Elestél, az eddigi sebzésed elveszett")
                unlucky += 1
                harcos_dobasok_osszege = 0              # itt lenullázódik a sebzés ha 1-est dob
                break 
            else:
                harcos_dobasok_osszege += random_szam
    if unlucky == 0:
        print(f"Dobásaid összege: {harcos_dobasok_osszege}")

   
szorny_dobasok_osszege = 0
def szorny_kore():
    global szorny_dobasok_osszege
    szorny_dobasok_osszege = 0
    for i in range(1, 3 + 1):
        random_szam = random.randint(1, 8)
        print(f"{i}. dobás: {random_szam}")
        szorny_dobasok_osszege += random_szam
    return print(f"Szörny dobásainak összege: {szorny_dobasok_osszege} + {dobasok}")


while True:
    if harcos <= 0:
        print("A szörny legyőzött")
        break
    else:
        print("Te jössz")
        harcos_kore()
        szorny -= harcos_dobasok_osszege
        if szorny > 0:
            print(f"Szörny hátralévő életereje: {szorny}")
        else:
            break
    if szorny <= 0:
        print("Legyőzted a szörnyet")
        break
    else:
        print("A szörny köre jön")
        szorny_kore()
        harcos -= szorny_dobasok_osszege + dobasok              # hozzáadódik a harcos által dobott kockák száma is a sebzéshez
        if harcos > 0:
            print(f"Maradék életerőd: {harcos}")
