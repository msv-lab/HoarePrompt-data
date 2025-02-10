#State of the program right berfore the function call: t is a positive integer such that 1 <= t <= 1000, and test_cases is a list of strings where each string represents a password of length 1 <= n <= 20 consisting of lowercase Latin letters and digits.
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
        
    #State: `results` is either ['NO', 'NO', 'YES'] or ['YES'] based on the conditions met during all iterations.
    return results
    #The program returns a list 'results' which is either ['NO', 'NO', 'YES'] or ['YES'] based on the conditions met during all iterations.
#Overall this is what the function does:The function `func_1` accepts two parameters: `t`, a positive integer between 1 and 1000 (inclusive), and `test_cases`, a list of strings representing passwords. For each password in `test_cases`, it checks if the password meets certain conditions related to the order of letters and digits within the password. If all passwords meet the conditions, it returns a list containing 'YES'; otherwise, it returns a list containing 'NO' repeated `t` times.

