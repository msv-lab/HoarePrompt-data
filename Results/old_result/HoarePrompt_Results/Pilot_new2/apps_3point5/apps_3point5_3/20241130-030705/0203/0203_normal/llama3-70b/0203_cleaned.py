n = int(input())
fractions = input()
depublicans = 0
remocrats = 0
for fraction in fractions:
    if fraction == 'D':
        depublicans += 1
    else:
        remocrats += 1
if depublicans > remocrats:
    print('D')
else:
    print('R')