
#Tengo lista de items
A = [] #Digamos que tiene cosas
HT = {} #HT vacia
for item in A:
    if item in HT.keys():
        HT[item] += 1
    else:
        HT[item] = 1

# Ahora para checar
item = None
count = 0
for i in t.items():
    if i[1] >= count:
        count = i[1]
        item = i[0]
return item

#Para la b:

if count >= n/2 +1:
    return item
else:
    return None