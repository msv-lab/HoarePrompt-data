def isValid(password):
    digits = []
    letters = []
    for char in password:
        if char.isdigit():
            digits.append(char)
        else:
            letters.append(char)
 
    # Sorting the digits and letters
    digits.sort()
    letters.sort()
 
    # Checking if there is any digit coming after a letter
    for i in range(len(digits)):
        if i < len(digits)-1 and digits[i] > digits[i+1]:
            return False
        if i < len(letters) and digits[-1] > letters[i]:
            return False
 
    # Concatenating the sorted digits and letters
    sortedPassword = ''.join(digits + letters)
 
    # Comparing the sorted password with the original password
    if sortedPassword == password:
        return True
    else:
        return False
 
testCases = int(input())
while testCases:
    length = int(input())
    password = input()
    print('YES') if isValid(password) else print('NO')
    testCases -= 1