duben = 13
kveten = (10 + 5 + 2 + 1.5 + 7)
cerven = (35 + 7 + 2 + 5 + 2 + 8 + 2 + 13 + 6 + 10)
cervenec = (23 + 18 + 5 + 2 + 3 + 6)
srpen = (3 + 12 + 5 + 9 + 20 + 2 + 23 + 21 + 1.5)
zari = (8 + 3 + 12 + 23 + 8 + 7 + 9)
rijen = (10 + 5 + 5)
print(kveten,srpen)
cely_rok = (duben + kveten + cerven + cervenec + srpen + zari + rijen)
srazky = {"duben": int(duben), "květen": int(kveten), "červen": int(cerven), "červenec": int(cervenec), "srpen": int(srpen), "září": int(zari), "říjen": int(rijen)}

print("měsíc|".rjust(11) + "četnost srážek".rjust(50) + "|NR.".rjust(59))
print("-" * 150)
for f_key, f_value in srazky.items():
    star = "*" * f_value
    print("{:>10}|".format(f_key) + "{: <105}|".format(star) + f"{f_value}")
print("-" * 150)
print("celý rok:", cely_rok)
help(input)