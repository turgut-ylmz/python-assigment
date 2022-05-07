sentence = input()
counted = {}
sayac = 0

for i in sentence:
    if i in counted :  
        counted[i] += 1
    else:
        counted[i] = 1

print(counted)
