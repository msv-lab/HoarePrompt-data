def func_1(password):
    digits = []
    letters = []
    for char in password:
        if char.isdigit():
            digits.append(char)
        else:
            letters.append(char)
    digits.sort()
    letters.sort()
    for i in range(len(digits)):
        if i < len(digits) - 1 and digits[i] > digits[i + 1]:
            return False
        if i < len(letters) and digits[-1] > letters[i]:
            return False
    sortedPassword = ''.join(digits + letters)
    if sortedPassword == password:
        return True
    else:
        return False
testCases = int(input())
while testCases:
    length = int(input())
    password = input()
    print('YES') if func_1(password) else print('NO')
    testCases -= 1