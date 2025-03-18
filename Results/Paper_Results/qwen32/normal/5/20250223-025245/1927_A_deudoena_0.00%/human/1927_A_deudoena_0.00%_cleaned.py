inpstr = input()
ind1 = 0
ind2 = 0
outind = 0
for (i, j) in enumerate(inpstr):
    if j == 'B':
        ind1 = i
        break
for i in range(len(inpstr)):
    if inpstr[-i - 1] == 'B':
        ind2 = i
        break
print(len(inpstr) - ind2 - ind1)