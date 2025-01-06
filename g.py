a = [3 , 2, 8, 1, 2, 4, 1, 3, 6, 5, 4, 7, 2, 1]
g = []
for d in a:
    if d not in g:
        g.append(d)
    else:
        continue
g.sort()
print(g)
i = 1
s = []
for x in a:
    if i in range(0,len(g)):
        x = int(x)
        c = s.append(a.count(i))
        i += 1
    else:
        break

print(s)
dk = dict(zip(g,s))
print(dk)