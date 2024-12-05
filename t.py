#user1 = {}
#user1["name"] = "Marek"
#user1["surname"] = "Parek"
#user1.setdefault("user_email", "marek.parek@gmail.com") 
#print("User #01:", user1)

jmeno = 'Marek'
heslo = '1234'
uzivatel = {'Marek': '1234'}
if uzivatel.get(jmeno) !=heslo:
    print("Uživatelské jméno nebo heslo nejsou v pořádku!")
else:
    print("Ahoj Marek vítej v aplikaci! Pokračuj...")

#cisla_1 = (1, 1, 2, 3, 4)
#cisla_2 = (5, 6, 7, 7, 8)
#sjednocene_hodnoty = set(cisla_1) | set(cisla_2)
#print("Sjednocené hodnoty ze zadání:", sjednocene_hodnoty)

cisla_1 = {1, 2, 3, 4}
cisla_2 = {3, 4, 5, 6}
rozdil_cisel = cisla_1 - cisla_2
print("Rozdílné hodnoty prvního setu oproti druhému:", rozdil_cisel)