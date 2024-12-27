letters = raw_input()
temp = 0
temp2 = 0

for i in letters:
    if i in "AEIOUY":
        temp += 1
        if(temp > temp2):
            temp2 = temp
        temp = 0
    else:
        temp += 1
temp += 1
if(temp > temp2):
    temp2 = temp
print(temp2)