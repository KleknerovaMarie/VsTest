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
separator = "{:^15}".format("-" * 40)
print(separator)

if names != name and passwords != user.get(names):               # pokuj jmeno a heslo není v dict, pak ukončí program
    print("Unregistered user, terminating the program..")
    exit()
else: 
    print("Hello, welcome to the app,", names)                  
    print("We have 3 texts to be analyzed.")
    print(separator)

    number = input("Enter a number btw. 1 and 3 to select:")    #input zádá čísla 1,2,3
    print(separator)
    if number not in ("1","2", "3"):                              #pokud není zadaný znak (1,2,3),pak uživatele upozorní
        print("Your symbol was wrong, good bye")

    else:
        if number == "1":                                    #pokud je input 1, pak se vybere 1. část textu
            number_one = TEXTS[0]

            words = len(number_one.split())                     #spočítá počet slov v textu
            print("There are", words, "words in the selected text.")

        
            first_big = sum(title_case[0].isupper() for title_case in number_one.split())
            print("Thera are", first_big,"titlecase words.")     #spočítá všechna slova s 1. velkým písmenem
           
            
            every_big = sum(big_case.isupper() and big_case.isalpha() for big_case in number_one.split())
            print("There are", every_big, "uppercase words.") #spočítá slova se všemi velkými písmeny

            
            small_sign = sum(lower_case.islower() for lower_case in number_one.split())
            print("There are", small_sign, "lowercase words.") #spočítá slova s malými písmeny                                       
            
            
            numeric = sum(ask_number.isdigit() for ask_number in number_one.replace(".", " ").split() )
            print("There are",numeric, "numeric string.")   #spočítá počet cifer v textu
                                     
        
            suma_list = 0                                  #sečte všechna čísla     
            for x in number_one.replace(".", "").split():
                if x.isdigit():
                    x = int(x)
                    suma_list += x
            print("The sum of all the numbers",suma_list)
            print(separator)
           
            
            graf = []                                                   #počítá četnost délky slov
            for words_frequency in number_one.replace(".", " ").replace(",", " ").split():     
                if words_frequency.istitle() or words_frequency.isascii():
                    words_frequency = list(words_frequency)
                    graf.append(words_frequency)

            provisional = []
            all_range = range(0, len(graf)) 
            for unit in all_range : 
                provisional.append(len(graf[unit]))
                unit +=1
               
            preparation = []
            for sort_preparation in provisional:
                if sort_preparation not in preparation:
                    preparation.append(sort_preparation)
                else:
                    continue
            preparation.sort()
          
            s_frequency = {}
            for s in preparation:
                o = s_frequency.setdefault(s,provisional.count(s))

            print("LEN|".rjust(4) + "OCCURENCES".rjust(15) + "|NR.".rjust(11))
            print(separator)
            for f_key, f_value in s_frequency.items():
                star = "*" * f_value
                print("{:>3}|".format(f_key) + "{: <22}|".format(star) + f"{f_value}")
                   



        elif number == "2":                                  #pokud je input 2, pak se vybere 2. část textu
            number_two = TEXTS[1]

            words = len(number_two.split())                     #spočítá počet slov v textu
            print("There are", words, "words in the selected text.")

        
            first_big = sum(title_case[0].isupper() for title_case in number_two.split())
            print("Thera are", first_big,"titlecase words.")     #spočítá všechna slova s 1. velkým písmenem
           
            
            every_big = sum(big_case.isupper() and big_case.isalpha() for big_case in number_two.split())
            print("There are", every_big, "uppercase words.") #spočítá slova se všemi velkými písmeny

            
            small_sign = sum(lower_case.islower() for lower_case in number_two.split())
            print("There are", small_sign, "lowercase words.") #spočítá slova s malými písmeny                                       
            
            
            numeric = sum(ask_number.isdigit() for ask_number in number_two.replace(".", " ").split() )
            print("There are",numeric, "numeric string.")   #spočítá počet cifer v textu
                                     
        
            suma_list = 0                                  #sečte všechna čísla     
            for x in number_two.replace(".", "").split():
                if x.isdigit():
                    x = int(x)
                    suma_list += x
            print("The sum of all the numbers",suma_list)
            print(separator)
           
            
            graf = []  
            frequency = {}                                                     #počítá četnost délky slov
            for words_frequency in number_two.replace(".", " ").replace(",", " ").split():     
                if words_frequency.istitle() or words_frequency.isascii():
                    words_frequency = list(words_frequency)
                    graf.append(words_frequency)

            provisional = []
            all_range = range(0, len(graf)) 
            for unit in all_range : 
                provisional.append(len(graf[unit]))
                unit +=1
               
            preparation = []
            for sort_preparation in provisional:
                if sort_preparation not in preparation:
                    preparation.append(sort_preparation)
                else:
                    continue
            preparation.sort()
          
            s_frequency = {}
            for s in preparation:
                o = s_frequency.setdefault(s,provisional.count(s))

            print("LEN|".rjust(4) + "OCCURENCES".rjust(15) + "|NR.".rjust(11))
            print(separator)
            for f_key, f_value in s_frequency.items():
                star = "*" * f_value
                print("{:>3}|".format(f_key) + "{: <22}|".format(star) + f"{f_value}")



        else:
            number_three = TEXTS[2]                                 #pokud je input 3, pak se vybere 3. část textu
            
            words = len(number_three.split())                     #spočítá počet slov v textu
            print("There are", words, "words in the selected text.")

        
            first_big = sum(title_case[0].isupper() for title_case in number_three.split())
            print("Thera are", first_big,"titlecase words.")     #spočítá všechna slova s 1. velkým písmenem
           
            
            every_big = sum(big_case.isupper() and big_case.isalpha() for big_case in number_three.split())
            print("There are", every_big, "uppercase words.") #spočítá slova se všemi velkými písmeny

            
            small_sign = sum(lower_case.islower() for lower_case in number_three.split())
            print("There are", small_sign, "lowercase words.") #spočítá slova s malými písmeny                                       
            
            
            numeric = sum(ask_number.isdigit() for ask_number in number_three.replace(".", " ").split() )
            print("There are",numeric, "numeric string.")   #spočítá počet cifer v textu
                                     
        
            suma_list = 0                                  #sečte všechna čísla     
            for x in number_three.replace(".", "").split():
                if x.isdigit():
                    x = int(x)
                    suma_list += x
            print("The sum of all the numbers",suma_list)
            print(separator)
           
            
            graf = []  
            frequency = {}                                                     #počítá četnost délky slov
            for words_frequency in number_three.replace(".", " ").replace(",", " ").split():     
                if words_frequency.istitle() or words_frequency.isascii():
                    words_frequency = list(words_frequency)
                    graf.append(words_frequency)

            provisional = []
            all_range = range(0, len(graf)) 
            for unit in all_range : 
                provisional.append(len(graf[unit]))
                unit +=1
               
            preparation = []
            for sort_preparation in provisional:
                if sort_preparation not in preparation:
                    preparation.append(sort_preparation)
                else:
                    continue
            preparation.sort()
          
            s_frequency = {}
            for s in preparation:
                o = s_frequency.setdefault(s,provisional.count(s))
            
            print("LEN|".rjust(4) + "OCCURENCES".rjust(15) + "|NR.".rjust(11))
            print(separator)
            for f_key, f_value in s_frequency.items():
                star = "*" * f_value
                print("{:>3}|".format(f_key) + "{: <22}|".format(star) + f"{f_value}") 




       
   



