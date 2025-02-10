def func_1(userString):
    list(userString)
    countA = 0
    countB = 0
    for letter in userString:
        if letter == 'A':
            countA += 1
        elif letter == 'B':
            countB += 1
        else:
            continue
    if countA > countB:
        print('A')
    elif countB > countA:
        print('B')
    else:
        pass
userStrings = ['8', 'ABABB', 'ABABA', 'BBBAB', 'AAAAA', 'BBBBB', 'BABAA', 'AAAAB', 'BAAAA']
for userString in userStrings:
    func_1(userString)