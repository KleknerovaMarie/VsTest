import random

separator = "-" * 40
print("Hi there")
print(separator)
print("I\'ve generated a random 4 digit number for you.\nLet\'s play a bulls and cows game.")
print(separator)

statistika = 0




def kontrola_nahody(nahoda):
    while nahoda == False:
        for kus in range(0,4):
            if nahoda[kus] in nahoda > 1:
                return False
            else:
                return True
        


def kontrola_odhadu(zadej_odhad:str):
    for cast in zadej_odhad:
        if cast != 4 or cast[0] == 0:
            return False
        elif cast.isdigit():
            return True
        else:
            return False




def nahodne_cislo(zacatek:int, konec:int,):
    zkontrolovane_nahody = random.randint(zacatek, konec)
    while kontrola_nahody == False:
        for kus in range(0,4):
            if zkontrolovane_nahody.count(zkontrolovane_nahody[kus]) > 1:
              False
              zkontrolovane_nahody = random.randint(zacatek, konec) 
              zkontrolovane_nahody = str(zkontrolovane_nahody) 
            else:
                break
    return zkontrolovane_nahody
          
def bul_cow(odhady, hod_nahoda):
    bull = 0
    cow = 0
    for i in len(range(hod_nahoda)):          
        if odhady[i] == hod_nahoda[i]:
            bull += 1
        else:
            continue

    for i_number in range(0, 4):
        if odhady[i_number] in hod_nahoda:
            cow += 1
        else:
            continue
    cow -= bull
    print("bulls:", bull, "cow:", cow )
    return bull, cow
        
   

odhad = input("Zadej číslo:")

while nahodne_cislo(1000, 9999) != odhad:
    statistika += 1
    if kontrola_nahody(odhad) == True:
        continue
    else:
        print("Your number is wrong.")
        
    if nahodne_cislo(1000, 9999) == odhad:
        print("Vyhrál jsi.")
        print(statistika)
    else:
        bul_cow(odhad, nahodne_cislo(1000, 9999))
        statistika += 1

while odhad != 
        

        
        
