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
                 