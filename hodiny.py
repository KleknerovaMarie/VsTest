import random

separator = "-" * 40
print("Hi there")
print(separator)
print("I\'ve generated a random 4 digit number for you.\nLet\'s play a bulls and cows game.")
print(separator)

start = 1000
stop = 9999
nahodne_cislo = random.randint(start, stop)
nahodne_cislo = str(nahodne_cislo)
print(nahodne_cislo)

odhad = input("Zadej číslo:")

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
            return False
        else:
            return True
    
       
def bulls_cows(number:str, random_n:str):
    bull = 0
    cow = 0
    for index_number in range(len(random_n)):          
        if number[index_number] == random_n[index_number]:
            bull += 1
        else:
            continue

    for i_number in range(len(random_n)):
        if number[i_number] in random_n:
            cow += 1
        else:
            continue
    cow -= bull
    print("bulls:", bull, "cow:", cow )
    return bull, cow





bulls_cows(number=odhad, random_n=nahodne_cislo)