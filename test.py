"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Marie Kleknerová
email: racanovamarie@gmail.com
"""


TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]



name = ("bob", "ann", "mike", "liz")
password = ("123", "pass123", "password123", "pass123")

user = {"bob": "123", "ann": "pass123", "mike": "password123", "liz": "pass123", }


names = input("user name:")
passwords = input("password:")
if names in name and passwords == user.get(names):               # pokud je jméno a heslo v dictionary pak vypíše pozdrav
    print("Hello, welcome to the app,", names)
    print("We have 3 texts to be analyzed.")

    number = input("Enter a number btw. 1 and 3 to select:")    #input zádá čísla 1,2,3

    if int(number) not in (1,2,3):                              #pokud není zadaný znak (1,2,3),pak uživatele upozorní
        print("Your symbol was wrong, good bye")

    else:
        if int(number) == 1:                                    #pokud je input 1, pak se vybere 1. část textu
            number_one = TEXTS[0]

            words = len(number_one.split())                     #spočítá počet slov v textu
            print("There are", words, "words in the selected text.")

            first_big = 0                                       #spočítá všechna slova s 1. velkým písmenem
            for title_case in number_one.split():
                if title_case[0].isupper():
                    first_big = first_big +1
            print("Thera are", first_big,"titlecase words.")

           
            every_big = 0                                       #spočítá slova se všemi velkými písmeny
            for big_case in number_one.split():
                if big_case.isupper() and big_case.isalpha():
                    every_big = every_big + 1
            print("There are", every_big, "uppercase words.")
            
            small_sign = 0                                      #spočítá slova s malými písmeny
            for lower_case in number_one.split():
                if lower_case.islower():
                    small_sign = small_sign + 1
            print("There are", small_sign, "lowercase words.")
           

            numeric = 0                                         #spočítá počet cifer v textu
            for ask_number in number_one.replace(".", " ").split():
                if ask_number.isdigit():
                    numeric = numeric + 1
            print("There are",numeric, "numeric string.")
            
            suma_list = 0                                       #sečte všechna čísla
            for x in number_one.replace(".", " ").split():
                if x.isdigit():
                    x = int(x)
                    suma_list += x
            print("The sum of all the numbers", suma_list)
           
            
            frequency = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0 }
            graf = []                                                       #počítá četnost délky slov
            for words_frequency in number_one.replace(",", " ").replace(".", " ").split():     
                if words_frequency.istitle() or words_frequency.isalpha() or words_frequency.isalnum():
                    words_frequency = list(words_frequency)
                    graf.append(words_frequency)
            provisional = []
            all_range = range(0, len(graf)) 
            for unit in all_range : 
                provisional.append(len(graf[unit]))
                unit +=1
            #print(provisional)
            for part_provisional in provisional:
                frequency[int(part_provisional)] += 1
            print(frequency)
                

           
            
            
            
                   




        elif int(number) == 2:                                  #pokud je input 2, pak se vybere 2. část textu
            number_two = TEXTS[1]

            words = len(number_two.split())                     
            print("There are", words, "words in the selected text.")

            first_big = 0
            for title_case in number_two.split():
                if title_case[0].isupper():
                    first_big = first_big +1
            print("Thera are", first_big,"titlecase words.")

            every_big = 0
            for big_case in number_two.split():
                if big_case.isupper() and big_case.isalpha():
                    every_big = every_big + 1
            print("There are", every_big, "uppercase words.")

            small_sign = 0
            for lower_case in number_two.split():
                if lower_case.islower():
                    small_sign = small_sign + 1
            print("There are", small_sign, "lowercase words.")
           

            numeric = 0
            for ask_number in number_two.replace(".", "").split():
                if ask_number.isdigit():
                    numeric = numeric + 1
            print("There are",numeric, "numeric string.")

            every_numeric = []
            every = TEXTS[0] + TEXTS[1] + TEXTS[2]
            for numeric in every:
                if numeric.isdigit():
                    every_numeric.append(numeric)
                    #print(every_numeric)
                    all_numeric = len(every_numeric)
            print("The sum of all the numbers", all_numeric)

            suma_list = 0                                       #sečte všechna čísla
            for x in number_two.replace(".", "").split():
                if x.isdigit():
                    x = int(x)
                    suma_list += x
            print("The sum of all the numbers",suma_list)

            frequency = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0 }
            graf = []                                                       #počítá četnost délky slov
            for words_frequency in number_two.replace(",", " ").replace(".", " ").split():     
                if words_frequency.istitle() or words_frequency.isalpha() or words_frequency.isalnum():
                    words_frequency = list(words_frequency)
                    graf.append(words_frequency)
            provisional = []
            all_range = range(0, len(graf)) 
            for unit in all_range : 
                provisional.append(len(graf[unit]))
                unit +=1
            #print(provisional)
            for part_provisional in provisional:
                frequency[int(part_provisional)] += 1
            print(frequency)

        else:
            number_three = TEXTS[2]                                 #pokud je input 3, pak se vybere 3. část textu
            
            words = len(number_three.split())
            print("There are", words, "words in the selected text.")

            first_big = 0
            for title_case in number_three.split():
                if title_case[0].isupper():
                    first_big = first_big +1
            print("Thera are", first_big,"titlecase words.")

            every_big = 0
            for big_case in number_three.split():
                if big_case.isupper() and big_case.isalpha():
                    every_big = every_big + 1
            print("There are", every_big, "uppercase words.")
            
            small_sign = 0
            for lower_case in number_three.split():
                if lower_case.islower():
                    small_sign = small_sign + 1
            print("There are", small_sign, "lowercase words.")
           
            numeric = 0
            for ask_number in number_three.replace(".", "").split():
                if ask_number.isdigit():
                    numeric = numeric + 1
            print("There are",numeric, "numeric string.")
           
            suma_list = 0                                       #sečte všechna čísla
            for x in number_three.replace(".", "").split():
                if x.isdigit():
                    x = int(x)
                    suma_list += x
            print("The sum of all the numbers", suma_list)

            frequency = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0 }
            graf = []                                                       #počítá četnost délky slov
            for words_frequency in number_three.replace(",", " ").replace(".", " ").split():     
                if words_frequency.istitle() or words_frequency.isalpha() or words_frequency.isalnum():
                    words_frequency = list(words_frequency)
                    graf.append(words_frequency)
            provisional = []
            all_range = range(0, len(graf)) 
            for unit in all_range : 
                provisional.append(len(graf[unit]))
                unit +=1
            #print(provisional)
            for part_provisional in provisional:
                frequency[int(part_provisional)] += 1
            print(frequency)
  
else:
    print("Unregistered user, terminating the program..")

       
   



