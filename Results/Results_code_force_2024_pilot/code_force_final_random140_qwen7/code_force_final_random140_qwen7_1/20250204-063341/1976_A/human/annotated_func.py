#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 1000, and test_cases is a list of strings where each string represents a password consisting of lowercase Latin letters and digits, and each string has a length between 1 and 20 inclusive.
def func_1(t, test_cases):
    results = []
    for (n, password) in test_cases:
        letters = ''
        
        digits = ''
        
        for ch in password:
            if ch.isalpha():
                letters += ch
            elif ch.isdigit():
                digits += ch
        
        if list(letters) != sorted(letters) or list(digits) != sorted(digits):
            results.append('NO')
            continue
        
        if letters and digits and password.index(letters[-1]) > password.index(digits
            [0]):
            results.append('NO')
        else:
            results.append('YES')
        
    #State: results is a list containing either 'NO', 'NO' or 'NO', 'YES' for each iteration.
    return results
    #The program returns a list named 'results' which contains either 'NO', 'NO' or 'NO', 'YES' for each iteration.
#Overall this is what the function does:The function accepts two parameters: `t`, a positive integer between 1 and 1000, and `test_cases`, a list of strings representing passwords. For each password in `test_cases`, it checks if the password meets specific criteria. If the password contains both letters and digits that are not in alphabetical or numerical order, it appends 'NO' to the results list; otherwise, it appends 'YES'. The function returns a list of 'NO' and 'YES' values corresponding to each password in `test_cases`.

