list=[
    'František', 'Bruno',
    'Anna', 'Jakub',
    'Klára', 'Anežka',
    'Anežka', 'Anežka'
]
posledni_index = len(list) -1
print("Na indexu 2 je:", list[2])
print('Na <posledni_index> indexu je:', list[posledni_index])
print('V intervalu od 2 do 5 je:', list[2:5])
print('Každý třetí člen je:', list[::3])

jmeno = "Martin"
vaha = 80
vyska = 2
bmi = vaha / vyska **2
print(jmeno, "tvé bmi je:", bmi)
if bmi > 40:
    kategorie = 'těžká obezita'
elif bmi > 30:
    kategorie = 'obezita'
elif bmi >25:
    kategorie = 'mírná nadváha'
elif bmi > 18.5:
    kategorie = 'Zdravá váha'
else:
    kategorie = 'podvýživa'
print(jmeno,"tvé BMI je ", bmi, "což je ", kategorie)


zamestananci = ['František','Anna','Jakub','Klára',]
print("Zaměstnanci na začátku", zamestananci)
zamestnanci_a = ['František','Anna','Jakub','Klára', "Bruno", "Anežka",] 
print('Nová jména přidána: ', zamestnanci_a)   
zamestnanci_b = ['František', "Bruno",'Anna','Jakub','Klára',]
print('Nová jména vložena:', zamestnanci_b)
                 

vstupni_cisla = [1, 2, 3, 4, 5, 6, 7]
vstupni_pismena = ["p", "ú", "s", "č", "p", "s", "n"]
tyden = ('pondělí', 'úterý', 'středa', 'čtvrtek', 'pátek', 'sobota', 'neděle')
cislo_dne = 3
den_tydne = tyden [cislo_dne - 1]
if cislo_dne in vstupni_cisla:
    print("Správná vstupní hodnota!")
    if den_tydne.startswith(vstupni_pismena[cislo_dne - 1]):
     
        print("Správné písmeno")

    else:
        print("Špatné písmeno!")
else:
    print("Špatná vstupní hodnota!")

print(den_tydne)




user_email = {"email": "marek.parek@gmail.com"}

# Vytvoř nový slovník "user_1"
user_1 = dict()

# Doplň klíče "name" a "surname" s hodnotami "Marek" a "Parek"
user_1['name'] = 'Marek'
user_1['surname'] = 'Parek'

# Doplň slovník "user_1" o slovník "user_email"
user_1.update(user_email)

# Vypiš hodnoty ze slovníku "user_1" s doplňujícím textem
print("User #01:", user_1)


jmeno = 'Marek'
heslo = '1234'
uzivatel = {'Marek': '1234'}
if uzivatel.get(jmeno) == heslo:
    print("Ahoj", jmeno, "vítej v aplikaci! Pokračuj...")
else:
    print("Uživatelské jméno nebo heslo nejsou v pořádku!")