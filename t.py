import random

separator = "-" * 40
print("Hi there")
print(separator)
print("I\'ve generated a random 4 digit number for you.\nLet\'s play a bulls and cows game.")
print(separator)




def generate_random(random_number):
    random_number = str(random_number)
    if len(random_number) == len(set(random_number)):
        return True
            
    else:
        return False

def cislo(start, stop):
    snad = random.randint(start, stop)
    while generate_random(snad) == False:
        if generate_random(snad) == False:
            snad = random.randint(start, stop)
        else:
            break
    return snad
    

def kontrola_odhadu(zadej_odhad:str):
    if len(zadej_odhad) == 4 and zadej_odhad[0] != "0" and zadej_odhad.isdigit():
        return True
    else:
        return False
        
def bulls_cows(number:str, random_n:str):
    bull = 0
    cow = 0
    all_index = range(len(number))
    for index_number in all_index:          
        if number[index_number] == random_n[index_number]:
            bull += 1
        else:
            continue

    for i_number in all_index:
        if number[i_number] in random_n:
            cow += 1
        else:
            continue
    cow -= bull
    print("bulls:", bull, "cow:", cow )
    return bull, cow
    
    

statistika = 0
odhad = None
chci = cislo(1000, 9999)
chci = str(chci)
while odhad != chci:
    odhad = input("zadej číslo:")
    statistika += 1
    if kontrola_odhadu(odhad) == False:
        print("špatné číslo.")
    else:
        bulls_cows(odhad, chci)
print("You are winner.")
print("portřeboval jsi", statistika, "tahů.")


    
    
      
            
        

    




