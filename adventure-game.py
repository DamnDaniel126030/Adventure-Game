import random

harcos = 50
szorny = random.randint(200, 350)
print(f"A szörny életereje {szorny}")


armory = []
while len(armory) != 3:
    while True:
        fegyver = input("Milyen fegyvert szeretnél? (Sword, Halberd, Mace, Bow) Nyomj entert hogy információkat kapj a fegyverekről ")
        if fegyver == "":
            print("------------------------\nSword: Minden dobáshoz hozzáad 3-t\nHalberd: Nagyobb esélye van kisebbett dobni, de minden dobáshoz hozzáad 5-t\nMace: A szörny 3 dobásából elvesz 1-et, de minden dobásból levon 2-t\nBow: Nagyobb esélye van nagyobbat dobni, de minden dobásból levon 3-t")
        else:
            armory.append(fegyver)
            break
    while True:
        armor = input("Milyen armort szeretnél? (Light, Medium, Heavy) Nyomj entert hogy információkat kapj az armorokról ")
        if armor == "":
            print("------------------------\nLight: +15 életerőt ad és dobsz +1 10 oldalú kockával a sebzéshez amikor te jössz\nMedium: +30 életerőt ad és dobsz +1 5 oldalú kockával a sebzéshez amikor te jössz\nHeavy: +50 életerőt ad")
        else:
            armory.append(armor)
            break
    while True:
        glove = input("Milyen kesztyűt szeretnél? (Lucky, Cheating, Stronghand, Steady hand) Nyomj entert hogy információkat kapj a kesztyűkről ")
        if glove == "":
            print("------------------------\nLucky Gloves: Minden dobáshoz hozzáad 1-et\nCheating Gloves: Hozzáad +1 20 oldalú kockát a sebzéshez\nStronghand Gloves: Minden kockád 24 oldalú lesz de levon 3-t minden dobásból\nSteady hand Gloves: Nem lehet vele egyest dobni")
        else:
            armory.append(glove)
            break
 
print(f"Felszerelésed: {armory[0]}, {armory[1]} armor, {armory[2]} gloves")
  
def halberd():                                    #ezt minden kockához hozzá kell adni
    if random.random() <= 0.5:
        return random.randint(1,5)
    elif random.random() <= 0.3:
        return random.randint(6,12)
    else:
        return random.randint(13,20)

def bow():                                        #ezt minden kockához hozzá kell adni
    if random.random() <= 0.7:
        return random.randint(11,20)
    else:
        return random.randint(1,10)



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
