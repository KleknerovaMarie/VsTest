"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Marie Kleknerová
email: racanovamarie@gmail.com
"""

import random
import time



def main():
    print("Hi there!")
    if __name__ == "_main_":
        main()

main()


def control_random(random_number: int):      #kontroluje jestli vygenerované číslo  nemá stejné číslice
    random_number = str(random_number)
    if len(random_number) == len(set(random_number)):
        return True
    else:
        return False
    

def generator_number(start: int, stop: int):      #generuje náhodné číslo dokud nejsou číslice unikátní
    generate = random.randint(start, stop)
    while control_random(generate) is False:
        generate = random.randint(start, stop)
        if control_random(generate) is True:
            break
    return generate
    

def control_estimation(estimat: str):        #kontroluje vložené číslo
    if len(estimat) == 4 and estimat[0] != "0" and estimat.isdigit() and len(estimat) == len(set(estimat)):
        return True
    else:
        return False
        
def bulls_cows(number:str, random_n:str):       #zjišťuje počet shodných číslic v čísle = cow a správné umístění = bull
    bull = 0
    cow = 0
    all_index = range(len(number))
    for index_number in all_index:          
        if number[index_number] == random_n[index_number]:
            bull += 1

    for i_number in all_index:
        if number[i_number] in random_n:
            cow += 1
    cow -= bull
    bul = "bull," if bull < 2 else "bulls,"
    cov = "cow" if cow < 2 else "cows"
    print(bull, bul, cow, cov )
    return bull, cow
    
    

separator = "-" * 50

print(separator)
print("I\'ve generated a random 4 digit number for you.\nLet\'s play a bulls and cows game.")
print(separator)


statistics = 0
play_estimate = None
rand_number = generator_number(1000, 9999)
rand_number = str(rand_number)
print("Enter a number:")
print(separator)
start_time = time.time()

while play_estimate != rand_number:         # dokud se neshoduje vložené číslo s generovaným kontroluje input a bull_cow
    play_estimate = input(">>> ")
    statistics += 1
    if control_estimation(play_estimate) is True:
        bulls_cows(play_estimate, rand_number)
        print(separator)
    else:         
        print("Wrong number, try again.")
        print(separator)

guess = "guess!" if statistics == 1 else "guesses!"
print("Correct, you\'ve guessed the right number \nin", statistics, guess)
end_time = time.time()
time_play = end_time - start_time
round_time = round(time_play, 3)
print("You needed", round_time, "seconds to play.")
print(separator)
print("That's amazing!")
